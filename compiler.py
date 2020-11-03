from parcer import Parser, VARIABLES
from lexer import Lexer

IFETCH = 'IFETCH'
ISTORE = 'ISTORE'
IPUSH = 'IPUSH'
IPOP = 'IPOP'
IADD = 'IADD'
ISUB = 'ISUB'
IMUL = 'IMUL'
IAND = 'IAND'
IDIV = 'IDIV'
IMINUS = 'IMINUS'
# todo
ILT = 'ILT'
JZ = 'JZ'
JNZ = 'JNZ'
JMP = 'JMP'
HALT = 'HALT'


class Compiler:
    program = []
    pc = 0

    def gen(self, command):
        self.program.append(command)
        self.pc = self.pc + 1

    def compile(self, node):
        if node.kind == Parser.VAR:
            self.gen(IFETCH)
            self.gen(node.value)
        elif node.kind == Parser.CONST:
            self.gen(IPUSH)
            self.gen(node.value)
        elif node.kind == Parser.ADD:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(IADD)
        elif node.kind == Parser.SUB:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(ISUB)
        elif node.kind == Parser.MULT:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(IMUL)
        elif node.kind == Parser.DIV:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(IDIV)
        elif node.kind == Parser.L_AND:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(IADD)
        elif node.kind == Parser.U_MINUS:
            self.compile(node.op1)
            self.gen(IMINUS)
        # todo
        elif node.kind == Parser.LESS:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(ILT)
        # todo
        elif node.kind == Parser.MORE:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(ILT)
        # todo
        elif node.kind == Parser.LESS_EQUAL:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(ILT)
        # todo
        elif node.kind == Parser.MORE_EQUAL:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(ILT)
        # todo
        elif node.kind == Parser.EQUAL:
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(ILT)
        elif node.kind == Parser.SET:
            self.compile(node.op2)
            self.gen(ISTORE)
            self.gen(node.op1.value)
        # todo
        elif node.kind == Parser.IF1:
            self.compile(node.op1)
            self.gen(JZ)
            addr = self.pc
            self.gen(0)
            self.compile(node.op2)
            self.program[addr] = self.pc
        # todo
        elif node.kind == Parser.IF2:
            self.compile(node.op1)
            self.gen(JZ)
            addr1 = self.pc
            self.gen(0)
            self.compile(node.op2)
            self.gen(JMP)
            addr2 = self.pc
            self.gen(0)
            self.program[addr1] = self.pc
            self.compile(node.op3)
            self.program[addr2] = self.pc
        # todo
        elif node.kind == Parser.WHILE:
            addr1 = self.pc
            self.compile(node.op1)
            self.gen(JZ)
            addr2 = self.pc
            self.gen(0)
            self.compile(node.op2)
            self.gen(JMP)
            self.gen(addr1)
            self.program[addr2] = self.pc
        # todo
        elif node.kind == Parser.DO:
            addr = self.pc
            self.compile(node.op1)
            self.compile(node.op2)
            self.gen(JNZ)
            self.gen(addr)
        elif node.kind == Parser.SEQ:
            self.compile(node.op1)
            self.compile(node.op2)
        elif node.kind == Parser.EXPR:
            self.compile(node.op1)
            self.gen(IPOP)
        elif node.kind == Parser.RETURN:
            self.compile(node.op1)
            if self.program:
                self.program.pop()
        elif node.kind == Parser.FUNC:
            self.compile(node.op2)
        elif node.kind == Parser.PROG:
            self.compile(node.op1)
            self.gen(HALT)
        return self.program


class VirtualMachine:

    ASSEMBLY = {
        'IFETCH': lambda x: f'\tpush dword ptr [{x}] \n',
        'ISTORE': lambda x: f'\tpop dword ptr [{x}] \n',
        'IPUSH': lambda x: f'\tmov eax, {x} \n\tpush eax \n',
        'IPOP': lambda: f'\tpop eax \n',
        'IADD': lambda: f'\tpop ebx \n\tpop eax \n\tadd eax, ebx \n\tpush eax \n',
        'ISUB': lambda: f'\tpop ebx \n\tpop eax \n\tsub eax, ebx \n\tpush eax \n',
        'IMUL': lambda: f'\tpop ebx \n\tpop eax \n\timul eax, ebx \n\tpush eax \n',
        'IDIV': lambda: f'\tpop ebx \n\tpop eax \n\tcdq \n\tidiv ebx \n\tpush eax \n',
        'IAND': lambda: f'\tpop eax \n\tpop ebx \n\tand edx, edx \n\tpush eax \n',
        'IMINUS': lambda: f'\tpop eax \n\tmov ebx, -1 \n\timul eax, ebx \n\tpush eax \n',
        'HALT': lambda: f'',
        # todo
        'ILT': lambda: f'',
        'JZ': lambda x: f'',
        'JNZ': lambda x: f'',
        'JMP': lambda x: f''
    }

    def run(self, program):
        file = open('1-01-Python-IV-82-Berezhniuk.asm', 'w+')
        count = 0
        if 'main' in VARIABLES:
            del VARIABLES['main']

        file.write('.data\n')
        file.write('\tCaption1 db "Andrew Berezhniuk", 0\n\tbuf dw ? \n')
        for var_name in VARIABLES[1:]:
            file.write(f'\t{var_name} dword 0, 0 \n')

        flag = True
        if len(program) == 1:
            flag = False

        file.write('\n.code \n')
        file.write('otherfunc proc \n')
        while program[count] != HALT:
            command = program[count]
            next_command = program[count + 1]
            if command in [IFETCH, ISTORE, IPUSH, JZ, JNZ, JMP]:
                file.write(VirtualMachine.ASSEMBLY[command](next_command))
                count += 2
            else:
                file.write(VirtualMachine.ASSEMBLY[command]())
                count += 1
            if command == ISTORE:
                count += 1
        if flag:
            file.write('\tpop eax \n')
            file.write('\tfn MessageBox, 0, str$(eax), ADDR Caption1, MB_OK \n\tret \n')
        file.write('otherfunc endp \n')
        file.close()






