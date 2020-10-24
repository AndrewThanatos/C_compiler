from parcer import Parser
from lexer import Lexer, VARIABLES

IPUSH = 'IPUSH'
IPOP = 'IPOP'

HALT = 'HALT'


class Compiler:
    program = []
    pc = 0

    def gen(self, command):
        self.program.append(command)
        self.pc = self.pc + 1

    def compile(self, node):
        if node.kind == Parser.CONST:
            self.gen(IPUSH)
            self.gen(node.value)
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
        'IPUSH': lambda x: f'mov eax, {x} \npush eax \n',
        'IPOP': lambda: f'pop eax \n',
    }

    def run(self, program):
        file = open('1-01-Python-IV-82-Berezhniuk.asm', 'w+')
        count = 0
        if 'main' in VARIABLES:
            del VARIABLES['main']

        while program[count] != HALT:
            command = program[count]
            next_command = program[count + 1]
            if command == IPUSH:
                file.write(VirtualMachine.ASSEMBLY[command](next_command))
                count += 2
            else:
                file.write(VirtualMachine.ASSEMBLY[command]())
                count += 1

        file.close()






