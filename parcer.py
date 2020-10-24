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

    EMPTY = 'EMPTY'
    RETURN = 'RETURN'

    SEQ = 'SEQ'
    EXPR = 'EXPR'
    FUNC = 'FUNC'
    PROG = 'PROG'

    NUM_TYPES = [Lexer.INT, Lexer.FLOAT]
    STR_TYPES = [Lexer.CHAR, Lexer.STRING]

    def __init__(self, lexer):
        self.lexer = lexer

    def error(self, msg):
        self.lexer.error(msg, 'parser')

    def check_types(self, node):
        type_1 = node.op1.ex_type
        type_2 = node.op2.ex_type
        if (type_1 in self.STR_TYPES and type_2 in self.NUM_TYPES) \
                or (type_1 in self.NUM_TYPES and type_2 in self.STR_TYPES):
            self.lexer.error(f'(TypeError) must be {type_1}, not {type_2}')

    def term(self):
        if self.lexer.sym == Lexer.ID:
            if self.lexer.value not in VARIABLES:
                self.lexer.error(f'(NameError) name \'{self.lexer.var_name}\' is no defined')
            n = Node(kind=Parser.VAR, value=self.lexer.value, ex_type=VARIABLES[self.lexer.value])
            self.lexer.next_tok()
            return n
        elif self.lexer.sym == Lexer.VALUE:
            val_type = None
            val_value = self.lexer.value
            if type(self.lexer.value) is int:
                val_type = Lexer.INT
            if type(self.lexer.value) is float:
                val_type = Lexer.FLOAT
                val_value = int(self.lexer.value)
            if type(self.lexer.value) is str:
                if len(self.lexer.value) == 1:
                    val_type = Lexer.CHAR
                    val_value = ord(self.lexer.value)
                else:
                    val_type = Lexer.STRING
            n = Node(kind=Parser.CONST, value=val_value, ex_type=val_type)
            self.lexer.next_tok()
            return n
        elif self.lexer.sym == Lexer.TYPE:
            var_type = self.lexer.value
            self.lexer.next_tok()
            if self.lexer.sym != Lexer.ID:
                self.lexer.error(f'(SyntaxError) variable expected')
            elif self.lexer.value in VARIABLES:
                self.lexer.error(f'(SyntaxError) \'{self.lexer.var_name}\' previously declared here')
            n = Node(kind=Parser.VAR, value=self.lexer.value, ex_type=var_type)
            self.lexer.add_var(var_name=self.lexer.value, var_type=var_type)
            self.lexer.next_tok()
            return n
        elif self.lexer.sym == Lexer.LPAR:
            return self.paren_expr()
        else:
            self.lexer.error('(SyntaxError) unexpected expresion')

    def expr(self):
        if self.lexer.sym != Lexer.ID and self.lexer.sym != Lexer.TYPE:
            return self.term()
        n = self.term()
        if n.kind == Parser.VAR and self.lexer.sym == Lexer.LPAR:
            n = Node(kind=Parser.FUNC, ex_type=n.ex_type, op1=self.paren_expr(), op2=self.statement())
        return n

    def paren_expr(self):
        if self.lexer.sym != Lexer.LPAR:
            self.error('(SyntaxError) \'(\' expected')
        self.lexer.next_tok()
        if self.lexer.sym == Lexer.RPAR:
            self.lexer.next_tok()
            return Node(kind=Parser.EMPTY)

        n = self.expr()
        if self.lexer.sym != Lexer.RPAR:
            self.error('(SyntaxError) \')\' expected')
        self.lexer.next_tok()
        return n

    def statement(self):
        if self.lexer.sym == Lexer.RETURN:
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
                self.error('(SyntaxError) \';\' expected')
            self.lexer.next_tok()
        return n

    def parse(self):
        self.lexer.next_tok()
        node = Node(kind=Parser.PROG, op1=self.expr())
        if self.lexer.sym != Lexer.EOF:
            self.error("(SyntaxError) invalid statement syntax")
        return node
