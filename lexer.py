import sys
import hashlib


def hash_var(var_name):
    hash_object = hashlib.sha1(var_name.encode())
    hex_dig = hash_object.hexdigest()
    return hex_dig


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

    IF = 'IF'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    DO = 'DO'
    RETURN = 'RETURN'

    LBRA = 'LBRA'
    RBRA = 'RBRA'
    LPAR = 'LPAR'
    RPAR = 'RPAR'

    SEMICOLON = 'SEMICOLON'
    ASSIGN = 'ASSIGN'
    PLUS = 'PLUS'
    MINUS = 'MINUS'
    MULTIPLY = 'MULTIPLY'
    DEVIDE = 'DEVIDE'
    EXCL_MARK = 'EXCL_MARK'
    B_AND = 'B_AND'
    L_AND = 'L_AND'

    LESS = 'LESS'
    MORE = 'MORE'
    LESS_EQUAL = 'LESS_EQUAL'
    MORE_EQUAL = 'MORE_EQUAL'
    EQUAL = 'EQUAL'
    NOT_EQUAL = 'NOT_EQUAL'

    EOF = 'EOF'

    SYMBOLS = {'{': LBRA, '}': RBRA, '=': ASSIGN, ';': SEMICOLON, '(': LPAR, ')': RPAR, '+': PLUS, '-': MINUS,
               '*': MULTIPLY, '/': DEVIDE, '<': LESS, '>': MORE, '!': EXCL_MARK, '&': B_AND}

    QUOTES = '\"'
    QUOTE = '\''
    DOT = '.'

    TEST_SYMBOLS_LONG = {'==': EQUAL, '>=': MORE_EQUAL, '<=': LESS_EQUAL, '!=': NOT_EQUAL, '&&': L_AND}
    TEST_SYMBOLS_SHORT = {'=': ASSIGN, '>': MORE, '<': LESS}
    TEST_SMB_SHORT = {'LESS': '<', 'MORE': '>', 'ASSIGN': '=', 'B_AND': '&'}

    BOOLEAN = [MINUS, B_AND]

    WORDS = {'if': IF, 'else': ELSE, 'do': DO, 'while': WHILE, 'return': RETURN}
    TYPES = {'int': INT, 'float': FLOAT, 'char': CHAR, 'string': STRING}

    ch = ' '

    def error(self, msg, type='lexer'):
        print(f'{type.title()} error: {msg}')
        print(f'Error in line {self.line}:')

        read_file = open('2-01-Python-IV-82-Berezhniuk.txt', 'r')
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
                if self.sym in Lexer.TEST_SMB_SHORT \
                        and Lexer.TEST_SMB_SHORT[self.sym] + self.ch in Lexer.TEST_SYMBOLS_LONG:
                    self.sym = Lexer.TEST_SYMBOLS_LONG[Lexer.TEST_SMB_SHORT[self.sym] + self.ch]
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
            elif self.ch == Lexer.QUOTES:
                str_val = ''
                self.getc()
                while self.ch != Lexer.QUOTES and len(self.ch) != 0:
                    if len(self.ch) == 0:
                        self.error("(SyntaxError) expected \'")
                    str_val += self.ch
                    self.getc()
                self.sym = Lexer.VALUE
                self.value = str_val
                self.getc()
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
