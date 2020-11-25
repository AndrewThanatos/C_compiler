from parcer import Parser
from lexer import Lexer
from compiler import Compiler, VM
from utils import print_block
import sys

if __name__ == '__main__':
    try:
        file = open('1-01-Python-IV-82-Berezhniuk.txt', 'r')
    except:
            print('Please create file "1-01-Python-IV-82-Berezhniuk.txt"')
            input('\nPress Enter to exit')
            sys.exit(1)
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VM()
    n = P.parse()
    comp = C.compile(n)
    # print_block(n)
    V.run(comp, C.call_func_count)
    input('\nPress Enter to exit')



