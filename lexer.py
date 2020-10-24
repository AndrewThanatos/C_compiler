import sys

VARIABLES = {}


class Lexer:

    def __init__(self, file):
        self.file = file
        self.line = 1
        self.row = -1

    TYPE = 'TYPE'
    INT = 'INT'
    FLOAT = 'FLOAT'
    CHAR = 'CHAR'
    STRING = 'STRING'

    VALUE = 'VALUE'
    ID = 'ID'

    RETURN = 'RETURN'

    LBRA = 'LBRA'
    RBRA = 'RBRA'
    LPAR = 'LPAR'
    RPAR = 'RPAR'

    SEMICOLON = 'SEMICOLON'

    EOF = 'EOF'

    SYMBOLS = {'{': LBRA, '}': RBRA, ';': SEMICOLON, '(': LPAR, ')': RPAR}

    QUOTES = '\"'
    DOT = '.'

    WORDS = {'return': RETURN}
    TYPES = {'int': INT, 'float': FLOAT, 'char': CHAR, 'string': STRING}

    ch = ' '

    def error(self, msg, type='lexer'):
        print(f'{type.title()} error: {msg}')
        print(f'Error in line {self.line}:')

        read_file = open('1-01-Python-IV-82-Berezhniuk.txt', 'r')
        data = read_file.readline()
        for i in range(self.line - 1):
            data = read_file.readline()

        with open('error.txt', 'w+') as f:
            f.write(f'{type.title()} error: {msg}\n')
            f.write(f'Error in line {self.line}:\n')
            f.write(f'\t{data}')

        print(f'\t{data}')
        read_file.close()
        sys.exit(1)

    def add_var(self, var_name, var_type):
        VARIABLES.update({var_name: var_type})

    def getc(self):
        self.ch = self.file.read(1)
        self.row += 1

    def next_tok(self):
        self.value = None
        self.var_name = None
        self.sym = None
        while self.sym is None:
            if len(self.ch) == 0:
                self.sym = Lexer.EOF
            elif self.ch.isspace():
                if self.ch == '\n':
                    self.line += 1
                    self.row = -1
                self.getc()
            elif self.ch in Lexer.SYMBOLS:
                self.sym = Lexer.SYMBOLS[self.ch]
                self.getc()
            elif self.ch.isdigit():
                flag = True
                value = 0
                intval = 0
                while self.ch.isdigit():
                    value = value * 10 + int(self.ch)
                    self.getc()
                    if self.ch == Lexer.DOT:
                        if not flag:
                            self.error('(SyntaxError) invalid expression')
                        intval = value
                        value = 0
                        flag = False
                        self.getc()

                if value == 0 and self.ch == 'b':
                    self.getc()
                    while self.ch.isdigit():
                        value = value * 2 + int(self.ch)
                        self.getc()

                if not flag:
                    value = intval + value / pow(10, len(str(value)))
                self.value = value
                self.sym = Lexer.VALUE
            elif self.ch.isalpha():
                ident = ''
                while self.ch.isalpha():
                    ident = ident + self.ch.lower()
                    self.getc()
                if ident in Lexer.WORDS:
                    self.sym = Lexer.WORDS[ident]
                elif ident in Lexer.TYPES:
                    self.sym = Lexer.TYPE
                    self.value = Lexer.TYPES[ident]
                else:
                    self.sym = Lexer.ID
                    self.value = ident
                    self.var_name = ident
            elif self.ch == Lexer.QUOTE:
                self.getc()
                self.sym = Lexer.VALUE
                self.value = self.ch
                self.getc()
                if self.ch != Lexer.QUOTE:
                    self.error('(SyntaxError) expected \'')
                self.getc()
            else:
                self.error(f'(SyntaxError) unexpected symbol {self.ch}')
