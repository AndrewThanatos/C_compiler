import sys
from lexer import Lexer, VARIABLES


class Node:
    def __init__(self, kind, value=None, ex_type=None, op1=None, op2=None, op3=None):
        self.kind = kind
        self.value = value
        self.ex_type = ex_type
        self.op1 = op1
        self.op2 = op2
        self.op3 = op3


class Parser:
    VAR = 'VAR'
    CONST = 'CONST'
    TYPE = 'TYPE'

    ADD = 'ADD'
    SUB = 'SUB'
    MULT = 'MULT'
    DIV = 'DIV'

    B_AND = 'B_AND'
    L_AND = 'L_AND'
    U_MINUS = 'U_MINUS'

    LESS = 'LESS'
    MORE = 'MORE'
    LESS_EQUAL = 'LESS_EQUAL'
    MORE_EQUAL = 'MORE_EQUAL'
    EQUAL = 'EQUAL'
    NO_EQUAL = 'NO_EQUAL'

    SET = 'SET'
    IF1 = 'IF1'
    IF2 = 'IF2'
    WHILE = 'WHILE'
    DO = 'DO'
    EMPTY = 'EMPTY'
    RETURN = 'RETURN'

    SEQ = 'SEQ'
    EXPR = 'EXPR'
    RETURN_EXPR = 'RETURN_EXPR'
    FUNC = 'FUNC'
    PROG = 'PROG'

    def __init__(self, lexer):
        self.lexer = lexer

    def error(self, msg):
        with open('output.txt', 'w+') as f:
            f.write(f'Lexer error: {msg}\n')
            f.write(f'Line: {self.lexer.line} Row: {self.lexer.row}')
        print('Parser error:', msg)
        print(f'Line: {self.lexer.line} Row: {self.lexer.row}')
        sys.exit(1)

    def check_types(self, node):
        type_1 = node.op1.ex_type
        type_2 = node.op2.ex_type
        if type_1 != type_2 and Lexer.STRING in [type_1, type_2]:
            self.lexer.error(f'cannot do {type_1} to {type_2}')

    def term(self):
        if self.lexer.sym == Lexer.ID:
            if self.lexer.value not in VARIABLES:
                self.lexer.error('Unknown identifier: ' + self.lexer.var_name)
            n = Node(kind=Parser.VAR, value=self.lexer.value, ex_type=VARIABLES[self.lexer.value])
            self.lexer.next_tok()
            return n
        elif self.lexer.sym == Lexer.VALUE:
            val_type = None
            if type(self.lexer.value) is int:
                val_type = Lexer.INT
            if type(self.lexer.value) is float:
                val_type = Lexer.FLOAT
            if type(self.lexer.value) is str:
                val_type = Lexer.STRING
            n = Node(kind=Parser.CONST, value=self.lexer.value, ex_type=val_type)
            self.lexer.next_tok()
            return n
        elif self.lexer.sym == Lexer.TYPE:
            var_type = self.lexer.value
            self.lexer.next_tok()
            if self.lexer.sym != Lexer.ID:
                self.lexer.error('variable expected')
            elif self.lexer.value in VARIABLES:
                self.lexer.error(f'variable "{self.lexer.var_name}" already declared')
            n = Node(kind=Parser.VAR, value=self.lexer.value, ex_type=var_type)
            self.lexer.add_var(var_name=self.lexer.value, var_type=var_type)
            self.lexer.next_tok()
            return n
        elif self.lexer.sym in Lexer.BOOLEAN:
            self.lexer.next_tok()
            op1 = self.expr()
            n = Node(kind=Parser.U_MINUS, op1=op1, ex_type=op1.ex_type)
            return n
        elif self.lexer.sym == Lexer.LPAR:
            return self.paren_expr()
        else:
            self.lexer.error('unexpected expresion')

    def multy(self):
        n = self.term()
        if self.lexer.sym == Lexer.MULTIPLY or self.lexer.sym == Lexer.DEVIDE:
            if self.lexer.sym == Lexer.MULTIPLY:
                kind = Parser.MULT
            else:
                kind = Parser.DIV
            self.lexer.next_tok()
            n = Node(kind=kind, op1=n, op2=self.multy())
            self.check_types(n)
            n.ex_type = n.op1.ex_type
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
            self.check_types(n)
            n.ex_type = n.op1.ex_type
        return n

    def boolean(self):
        n = self.math()
        if self.lexer.sym == Lexer.L_AND or self.lexer.sym == Lexer.B_AND:
            if self.lexer.sym == Lexer.L_AND:
                kind = Parser.L_AND
            elif self.lexer.sym == Lexer.B_AND:
                kind = Parser.B_AND
            elif self.lexer.sym == Lexer.MINUS:
                kind = Parser.B_AND
            self.lexer.next_tok()
            n = Node(kind=kind, op1=n, op2=self.boolean())
            self.check_types(n)
            n.ex_type = n.op1.ex_type
        return n

    def test(self):
        n = self.boolean()
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
            self.check_types(n)
            n.ex_type = n.op1.ex_type
        return n

    def expr(self):
        if self.lexer.sym != Lexer.ID and self.lexer.sym not in Lexer.TYPE:
            return self.test()
        n = self.test()
        if n.kind == Parser.VAR and self.lexer.sym == Lexer.ASSIGN:
            self.lexer.next_tok()
            n = Node(kind=Parser.SET, op1=n, op2=self.expr())
            self.check_types(n)
            n.ex_type = n.op1.ex_type
        elif n.kind == Parser.VAR and self.lexer.sym == Lexer.LPAR:
            n = Node(kind=Parser.FUNC, ex_type=n.ex_type, op1=self.paren_expr(), op2=self.statement())
        return n

    def paren_expr(self):
        if self.lexer.sym != Lexer.LPAR:
            self.error('"(" expected')
        self.lexer.next_tok()
        if self.lexer.sym == Lexer.RPAR:
            self.lexer.next_tok()
            return Node(kind=Parser.EMPTY)

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
        elif self.lexer.sym == Lexer.RETURN:
            self.lexer.next_tok()
            n = Node(kind=Parser.RETURN, op1=self.statement())
        elif self.lexer.sym == Lexer.SEMICOLON:
            n = Node(kind=Parser.EMPTY)
            self.lexer.next_tok()
        elif self.lexer.sym == Lexer.LBRA:
            n = Node(kind=Parser.EMPTY)
            self.lexer.next_tok()
            while self.lexer.sym != Lexer.RBRA:
                n = Node(kind=Parser.SEQ, op1=n, op2=self.statement())
            self.lexer.next_tok()
        else:
            n = Node(kind=Parser.EXPR, op1=self.expr())
            if self.lexer.sym != Lexer.SEMICOLON:
                self.error('";" expected')
            self.lexer.next_tok()
        return n

    def parse(self):
        self.lexer.next_tok()
        node = Node(kind=Parser.PROG, op1=self.expr())
        if (self.lexer.sym != Lexer.EOF):
            self.error("Invalid statement syntax")
        return node
