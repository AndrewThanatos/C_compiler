from parcer import Parser
from lexer import Lexer
from compiler import Compiler, VM
from utils import print_block
import sys

if __name__ == '__main__':
    try:
        file = open('kr-01-Python-IV-82-Berezhniuk.txt', 'r')
    except:
            print('Please create file "kr-01-Python-IV-82-Berezhniuk.txt"')
            input('\nPress Enter to exit')
            sys.exit(1)
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VM()
    n = P.parse()
    comp = C.compile(n)
    V.run(comp, C.call_func_count)

    print_block(n)
    print()
    print('=====================================')
    print()
    print('ASM Code')
    with open('kr-01-Python-IV-82-Berezhniuk.asm', 'r') as f:
        print(f.read())
    input('\nPress Enter to exit')



