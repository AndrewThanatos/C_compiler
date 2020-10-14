from parcer import Parser
from lexer import Lexer
from compiler import Compiler, VirtualMachine



if __name__ == '__main__':
    file = open('main.c', 'r')
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VirtualMachine()
    n = P.parse()
    comp = C.compile(n)
    V.run(comp)



