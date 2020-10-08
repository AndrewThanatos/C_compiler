import sys


class Lexer:

    def __init__(self, file):
        self.file = file

    TYPE = 'TYPE'
    INT = 'INT'
    FLOAT = 'FLOAT'
    STRING = 'STRING'

    NUM = 'NUM'
    ID = 'ID'

    IF = 'IF'
    ELSE = 'ELSE'
    WHILE = 'WHILE'
    DO = 'DO'

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

    LESS = 'LESS'
    MORE = 'MORE'
    LESS_EQUAL = 'LESS_EQUAL'
    MORE_EQUAL = 'MORE_EQUAL'
    EQUAL = 'EQUAL'

    EOF = 'EOF'

    SYMBOLS = {'{': LBRA, '}': RBRA, '=': ASSIGN, ';': SEMICOLON, '(': LPAR, ')': RPAR, '+': PLUS, '-': MINUS,
               '*': MULTIPLY, '/': DEVIDE, '<': LESS, '>': MORE}

    TEST_SYMBOLS_LONG = {'==': EQUAL, '>=': MORE_EQUAL, '<=': LESS_EQUAL}
    TEST_SYMBOLS_SHORT = {'=': ASSIGN, '>': MORE, '<': LESS}
    TEST_SMB_SHORT = {'LESS': '<', 'MORE': '>', 'ASSIGN': '='}

    WORDS = {'if': IF, 'else': ELSE, 'do': DO, 'while': WHILE}
    TYPES = {'int': INT, 'float': FLOAT, 'str': STRING}

    ch = ' '  # допустим, первый символ - это пробел

    def error(self, msg):
        print('Lexer error: ', msg)
        sys.exit(1)

    def getc(self):
        self.ch = self.file.read(1)

    def next_tok(self):
        self.value = None
        self.type = None
        self.sym = None
        while self.sym is None:
            if len(self.ch) == 0:
                self.sym = Lexer.EOF
            elif self.ch.isspace():
                self.getc()
            elif self.ch in Lexer.SYMBOLS:
                self.sym = Lexer.SYMBOLS[self.ch]
                self.getc()
                if self.sym in Lexer.TEST_SMB_SHORT and self.ch in Lexer.TEST_SYMBOLS_SHORT:
                    self.sym = Lexer.TEST_SYMBOLS_LONG[Lexer.TEST_SMB_SHORT[self.sym] + self.ch]
                    self.getc()
            elif self.ch.isdigit():
                intval = 0
                while self.ch.isdigit():
                    intval = intval * 10 + int(self.ch)
                    self.getc()
                self.value = intval
                self.sym = Lexer.NUM
            elif self.ch.isalpha():
                ident = ''
                while self.ch.isalpha():
                    ident = ident + self.ch.lower()
                    self.getc()
                if ident in Lexer.WORDS:
                    self.sym = Lexer.WORDS[ident]
                if ident in Lexer.TYPES:
                    self.sym = Lexer.TYPE
                    self.type = Lexer.TYPES[ident]
                elif len(ident) == 1:
                    self.sym = Lexer.ID
                    self.value = ord(ident) - ord('a')
                else:
                    self.error('Unknown identifier: ' + ident)
            else:
                self.error('Unexpected symbol: ' + self.ch)
