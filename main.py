from parcer import Parser
from lexer import Lexer



if __name__ == '__main__':
    file = open('input.txt', 'r')
    L = Lexer(file)
    P = Parser(L)
    n = P.parse()
    print(n)