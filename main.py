from parcer import Parser
from lexer import Lexer
from compiler import Compiler, VM

import sys

if __name__ == '__main__':
    try:
        file = open('3-03-Python-IV-82-Borozenets.txt', 'r')
    except:
        print('Create input file"')
        input('\nPress Enter to exit')
        sys.exit()
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VM()
    n = P.parse()
    comp = C.compile(n)

    V.run(comp)




