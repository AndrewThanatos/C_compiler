from parcer import Parser

IFETCH = 'IFETCH'
ISTORE = 'ISTORE'
IPUSH = 'IPUSH'
IPOP = 'IPOP'
IADD = 'IADD'
ISUB = 'ISUB'
IMUL = 'IMUL'
IDIV = 'IDIV'
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
            self.program.pop()
        elif node.kind == Parser.FUNC:
            self.compile(node.op2)
        elif node.kind == Parser.PROG:
            self.compile(node.op1)
            self.gen(HALT)
        return self.program


class VirtualMachine:

    with_argument = ['IFETCH', 'ISTORE', 'IPUSH', 'JZ', 'JNZ', 'JMP']

    ASSEMBLY = {
        'IFETCH': lambda x: f'push dword ptr [{x}] \n',
        'ISTORE': lambda x: f'pop dword ptr [{x}] \n',
        'IPUSH': lambda x: f'mov eax, {x} \npush eax \n',
        'IPOP': lambda: f'pop eax \n',
        'IADD': lambda: f'pop ebx \npop eax \nadd eax, ebx \npush eax \n',
        'ISUB': lambda: f'pop ebx \npop eax \nsub eax, ebx \npush eax \n',
        'IMUL': lambda: f'pop ebx \npop eax \nimul eax, ebx \npush eax \n',
        'IDIV': lambda: f'pop eax \npop ebx \nxor edx, edx \ndiv ebx \npush eax \n',
        # todo
        'ILT': lambda: f'',
        'JZ': lambda x: f'',
        'JNZ': lambda x: f'',
        'JMP': lambda x: f'',
        'HALT': lambda: f''
    }

    def run(self, program):
        file = open('output.txt', 'w+')
        count = 0
        while program[count] != HALT:
            command = program[count]
            next_command = program[count + 1]
            if command in VirtualMachine.with_argument:
                file.write(VirtualMachine.ASSEMBLY[command](next_command))
                count += 2
            else:
                file.write(VirtualMachine.ASSEMBLY[command]())
                count += 1






