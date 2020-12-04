from parcer import Parser
from lexer import Lexer
from compiler import Compiler, VM
from utils import print_block
import sys

if __name__ == '__main__':
    try:
        file = open('5-03-Python-IV-82-Borozenets.txt', 'r')
    except:
            print('Please create input file')
            input('')
            sys.exit(1)
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VM()
    n = P.parse()
    comp = C.compile(n)
    print_block(n)
    V.run(comp, C.call_func_count)
    input('')



