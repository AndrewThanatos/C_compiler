from parcer import Parser
from lexer import Lexer
# from utils import print_block
from compiler import Compiler, VM

import sys

if __name__ == '__main__':
    try:
        file = open('4-03-Python-IV-82-Borozenets.txt', 'r')
    except:
        print('Create input file"')
        input('\nPress Enter to exit')
        sys.exit()
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VM()
    n = P.parse()
    # print_block(n)
    comp = C.compile(n)

    V.run(comp)




