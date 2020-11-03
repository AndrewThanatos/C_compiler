from parcer import Parser
from lexer import Lexer
from compiler import Compiler, VirtualMachine
from utils import print_block
import sys

if __name__ == '__main__':
    try:
        file = open('2-03-Python-IV-82-Borozenets.txt', 'r')
    except:
        with open('error.txt', 'w+') as f:
            f.write('Please create file "2-03-Python-IV-82-Borozenets.txt"')
            sys.exit()
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VirtualMachine()
    n = P.parse()
    comp = C.compile(n)
    print_block(n)
    V.run(comp)



