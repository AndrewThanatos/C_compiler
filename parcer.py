import sys
from lexer import Lexer


class Node:
    def __init__(self, kind, value=None, op1=None, op2=None, op3=None):
        self.kind = kind
        self.h_kind = Parser.KEY_WORDS[kind]
        self.value = value
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3


class Parser:
    VAR, CONST, ADD, SUB, MULT, DIV, LESS, MORE, LESS_EQUAL, MORE_EQUAL, EQUAL, SET, IF1, IF2, WHILE, DO, \
    EMPTY, SEQ, EXPR, PROG = range(20)
    KEY_WORDS = ['VAR', 'CONST', 'ADD', 'SUB', 'MULT', 'DIV', 'LESS', 'MORE', 'LESS_EQUAL', 'MORE_EQUAL', 'EQUAL',
                 'SET', 'IF1', 'IF2', 'WHILE', 'DO', 'EMPTY', 'SEQ', 'EXPR', 'PROG']

    def __init__(self, lexer):
        self.lexer = lexer

    def error(self, msg):
        print('Parser error:', msg)
        sys.exit(1)

    def term(self):
        if self.lexer.sym == Lexer.ID:
            n = Node(Parser.VAR, self.lexer.value)
            self.lexer.next_tok()
            return n
        elif self.lexer.sym == Lexer.NUM:
            n = Node(Parser.CONST, self.lexer.value)
            self.lexer.next_tok()
            return n
        else:
            return self.paren_expr()

    def multy(self):
        n = self.term()
        if self.lexer.sym == Lexer.MULTIPLY or self.lexer.sym == Lexer.DEVIDE:
            if self.lexer.sym == Lexer.MULTIPLY:
                kind = Parser.MULT
            else:
                kind = Parser.DIV
            self.lexer.next_tok()
            n = Node(kind, op1=n, op2=self.multy())
        return n

    def math(self):
        n = self.multy()
        if self.lexer.sym == Lexer.PLUS or self.lexer.sym == Lexer.MINUS:
            if self.lexer.sym == Lexer.PLUS:
                kind = Parser.ADD
            else:
                kind = Parser.SUB
            self.lexer.next_tok()
            n = Node(kind=kind, op1=n, op2=self.math())
        return n

    def test(self):
        n = self.math()
        if self.lexer.sym == Lexer.LESS or self.lexer.sym == Lexer.MORE or self.lexer.sym == Lexer.LESS_EQUAL \
                or self.lexer.sym == Lexer.MORE_EQUAL or self.lexer.sym == Lexer.EQUAL:
            if self.lexer.sym == Lexer.LESS:
                kind = Parser.LESS
            elif self.lexer.sym == Lexer.MORE:
                kind = Parser.MORE
            elif self.lexer.sym == Lexer.LESS_EQUAL:
                kind = Parser.LESS_EQUAL
            elif self.lexer.sym == Lexer.MORE_EQUAL:
                kind = Parser.MORE_EQUAL
            else:
                kind = Parser.EQUAL
            self.lexer.next_tok()
            n = Node(kind=kind, op1=n, op2=self.math())
        return n

    def expr(self):
        if self.lexer.sym != Lexer.ID:
            return self.test()
        n = self.test()
        if n.kind == Parser.VAR and self.lexer.sym == Lexer.ASSIGN:
            self.lexer.next_tok()
            n = Node(kind=Parser.SET, op1=n, op2=self.expr())
        return n

    def paren_expr(self):
        if self.lexer.sym != Lexer.LPAR:
            self.error('"(" expected')
        self.lexer.next_tok()
        n = self.expr()
        if self.lexer.sym != Lexer.RPAR:
            self.error('")" expected')
        self.lexer.next_tok()
        return n

    def statement(self):
        if self.lexer.sym == Lexer.IF:
            self.lexer.next_tok()
            n = Node(kind=Parser.IF1, op1=self.paren_expr(), op2=self.statement())
            if self.lexer.sym == Lexer.ELSE:
                n.kind = Parser.IF2
                self.lexer.next_tok()
                n.op3 = self.statement()
        elif self.lexer.sym == Lexer.WHILE:
            self.lexer.next_tok()
            n = Node(kind=Parser.WHILE, op1=self.paren_expr(), op2=self.statement())
        elif self.lexer.sym == Lexer.DO:
            self.lexer.next_tok()
            n = Node(kind=Parser.DO, op1=self.statement())
            if self.lexer.sym != Lexer.WHILE:
                self.error('"while" expected')
            self.lexer.next_tok()
            n.op2 = self.paren_expr()
            if self.lexer.sym != Lexer.SEMICOLON:
                self.error('";" expected')
        elif self.lexer.sym == Lexer.SEMICOLON:
            n = Node(Parser.EMPTY)
            self.lexer.next_tok()
        elif self.lexer.sym == Lexer.LBRA:
            n = Node(Parser.EMPTY)
            self.lexer.next_tok()
            while self.lexer.sym != Lexer.RBRA:
                n = Node(Parser.SEQ, op1=n, op2=self.statement())
            self.lexer.next_tok()
        else:
            n = Node(Parser.EXPR, op1=self.expr())
            if self.lexer.sym != Lexer.SEMICOLON:
                self.error('";" expected')
            self.lexer.next_tok()
        return n

    def parse(self):
        self.lexer.next_tok()
        node = Node(Parser.PROG, op1=self.statement())
        if (self.lexer.sym != Lexer.EOF):
            self.error("Invalid statement syntax")
        return node
