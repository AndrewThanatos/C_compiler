from parcer import Parser
from lexer import Lexer
from compiler import Compiler, VirtualMachine
import sys

if __name__ == '__main__':
    try:
        file = open('2-01-Python-IV-82-Berezhniuk.txt', 'r')
    except:
        with open('error.txt', 'w+') as f:
            f.write('Please create file "2-01-Python-IV-82-Berezhniuk.txt"')
            sys.exit()
    L = Lexer(file)
    P = Parser(L)
    C = Compiler()
    V = VirtualMachine()
    n = P.parse()
    comp = C.compile(n)
    V.run(comp)



