from parcer import Parser
from lexer import Lexer
from compiler import Compiler, VM
import sys

if __name__ == '__main__':
    try:
        file = open('4-15-Python-IV-82-Motora.txt', 'r')
    except:
            print('')
            input('')
            sys.exit(1)
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VM()
    n = P.parse()
    comp = C.compile(n)
    V.run(comp, C.call_func_count)
    with open('4-15-Python-IV-82-Motora.asm', 'r') as f:
        print(f.read())
    input('')



