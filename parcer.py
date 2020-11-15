import sys
from lexer import Lexer

VARIABLES = []
FUNCTIONS = []

class Variable:
    def __init__(self, name, var_type, initialized=False):
        self.name = name
        self.var_type = var_type
        self.initialized = initialized


class Variables:
    def __init__(self):
        self.variables = []
        self.level = 0
        self.count = 0

    def get_level(self, level):
        var = self.variables
        for i in range(level):
            var = var[-1]
        return var

    def add_variable(self, name, var_type, initialized=False):
        env = self.get_level(self.level)
        name = name + f'_{self.count}'
        self.count += 1
        env.append(Variable(name, var_type, initialized))
        VARIABLES.append(name)

    def new_level(self):
        env = self.get_level(self.level)
        self.level += 1
        env.append([])

    def prev_level(self):
        self.level -= 1

    def get_variable(self, name):
        for level in range(self.level, -1, -1):
            for item in self.get_level(level):
                if type(item) != list and item.name.split('_')[0] == name:
                    return item
        return None

    def is_define(self, name):
        return bool(self.get_variable(name))

    def is_define_locally(self, name):
        for item in self.get_level(self.level):
            if type(item) != list and item.name.split('_')[0] == name:
                return True

        return None

    def is_initialized(self, name):
        var = self.get_variable(name.split('_')[0])
        if var:
            return var.initialized
        else:
            return None

    def get_type(self, name):
        var = self.get_variable(name)
        return var.var_type

    def initialize(self, name):
        var = self.get_variable(name.split('_')[0])
        var.initialized = True


class Node:
    def __init__(self, kind, value=None, ex_type=None, cur_func=None, op1=None, op2=None, op3=None):
        self.kind = kind
        self.value = value
        self.ex_type = ex_type
        self.cur_func = cur_func
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
    FUNC = 'FUNC'
    FUNC_CALL = 'FUNC_CALL'
    PROG = 'PROG'

    NUM_TYPES = [Lexer.INT, Lexer.FLOAT]
    STR_TYPES = [Lexer.CHAR, Lexer.STRING]

    def __init__(self, lexer):
        self.lexer = lexer
        self.is_func = False
        self.vars = Variables()
        self.cur_func = None
        self.arguments = []

    def error(self, msg):
        self.lexer.error(msg, 'parser')

    def check_types(self, node):
        type_1 = node.op1.ex_type
        type_2 = node.op2.ex_type
        kind_1 = node.op1.kind
        kind_2 = node.op2.kind
        value_1 = node.op1.value
        value_2 = node.op2.value
        if kind_1 == Parser.VAR and not self.vars.is_initialized(value_1):
            self.error(f'(TypeError) variable \'{value_1.split("_")[0]}\' not initialized')
        if kind_2 == Parser.VAR and not self.vars.is_initialized(value_2):
            self.error(f'(TypeError) variable \'{value_2.split("_")[0]}\' not initialized')
        if (type_1 in self.STR_TYPES and type_2 in self.NUM_TYPES) \
                or (type_1 in self.NUM_TYPES and type_2 in self.STR_TYPES):
            self.error(f'(TypeError) must be {type_1}, not {type_2}')

    def term(self):
        if self.lexer.sym == Lexer.ID:
            if not self.vars.is_define(self.lexer.value):
                self.error(f'(NameError) name \'{self.lexer.value}\' is no defined')
            if self.lexer.value in FUNCTIONS:
                n = Node(kind=Parser.FUNC_CALL, value=self.vars.get_variable(self.lexer.value).name,
                         ex_type=self.vars.get_type(self.lexer.value), op1=self.func_arguments_set())
            else:
                n = Node(kind=Parser.VAR, value=self.vars.get_variable(self.lexer.value).name,
                         ex_type=self.vars.get_type(self.lexer.value))
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
            if type(self.lexer.value) is bool:
                val_type = Lexer.BOOL
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
                self.error(f'(SyntaxError) variable expected')
            elif self.vars.is_define_locally(self.lexer.value):
                self.error(f'(SyntaxError) \'{self.lexer.value}\' previously declared here')
            self.vars.add_variable(name=self.lexer.value, var_type=var_type)
            n = Node(kind=Parser.VAR, value=self.vars.get_variable(self.lexer.value).name, ex_type=var_type)
            self.lexer.next_tok()
            return n
        elif self.lexer.sym in Lexer.FIRST_OPERATORS:
            self.lexer.next_tok()
            if self.lexer.sym == Lexer.LPAR:
                op1 = self.paren_expr()
            else:
                op1 = self.term()
            n = Node(kind=Parser.U_MINUS, op1=op1, ex_type=op1.ex_type)
            return n
        elif self.lexer.sym == Lexer.LPAR:
            return self.paren_expr()
        else:
            self.error('(SyntaxError) unexpected expresion')

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
            else:
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
            n = Node(kind=kind, ex_type=self.lexer.BOOL, op1=n, op2=self.math())
            self.check_types(n)
        return n

    def expr(self):
        if self.lexer.sym != Lexer.ID and self.lexer.sym != Lexer.TYPE:
            return self.test()
        n = self.test()
        if n.kind == Parser.VAR and self.lexer.sym == Lexer.ASSIGN:
            self.lexer.next_tok()
            op2 = self.expr()
            if n.kind == Parser.VAR:
                self.vars.initialize(n.value)
            if op2.kind == Parser.VAR:
                self.vars.initialize(op2.value)
            n = Node(kind=Parser.SET, op1=n, op2=op2)
            self.check_types(n)
            n.ex_type = n.op1.ex_type
        elif n.kind == Parser.VAR and self.lexer.sym == Lexer.LPAR:
            cur_func = n.value.split('_')[0]
            FUNCTIONS.append(VARIABLES.pop().split('_')[0])
            op1 = self.func_arguments_create()
            self.arguments = op1
            op2 = self.statement()
            op3 = self.expr() if self.lexer.sym != Lexer.EOF else None
            n = Node(kind=Parser.FUNC, ex_type=n.ex_type, op1=op1, op2=op2, op3=op3, cur_func=cur_func)
        elif n.kind == Parser.VAR and self.lexer.sym in Lexer.ARITHMETIC_LONG:
            if self.lexer.sym in [Lexer.MUL_EQUAL, Lexer.DIV_EQUAL, Lexer.SUM_EQUAL, Lexer.MIN_EQUAL]:
                if self.lexer.sym == Lexer.MUL_EQUAL:
                    kind = Parser.MULT
                elif self.lexer.sym == Lexer.DIV_EQUAL:
                    kind = Parser.DIV
                elif self.lexer.sym == Lexer.SUM_EQUAL:
                    kind = Parser.ADD
                else:
                    kind = Parser.SUB
                self.lexer.next_tok()
                n = Node(kind=kind, op1=n, op2=self.expr())
                self.check_types(n)
                n.ex_type = n.op1.ex_type
            n = Node(kind=Parser.SET, op1=n.op1, op2=n)
            self.check_types(n)
            n.ex_type = n.op1.ex_type
            return n
        return n

    def func_arguments_create(self):
        if self.lexer.sym != Lexer.LPAR:
            self.error('(SyntaxError) \'(\' expected')
        self.lexer.next_tok()
        arguments = []
        var_type = None
        count = self.vars.count
        while self.lexer.sym != Lexer.RPAR:
            if self.lexer.sym == Lexer.TYPE:
                var_type = self.lexer.value
                self.lexer.next_tok()
            else:
                self.error('(SyntaxError) expected variable type')
            # self.vars.add_variable(name=self.lexer.value, var_type=var_type)
            arguments.append({'type': var_type, 'value': self.lexer.value + f'_{count}'})
            count += 1
            self.lexer.next_tok()
            if self.lexer.sym != Lexer.COMA:
                break
            else:
                self.lexer.next_tok()
        if self.lexer.sym != Lexer.RPAR:
            self.error('(SyntaxError) \')\' expected')
        self.lexer.next_tok()
        return arguments

    def func_arguments_set(self):
        self.lexer.next_tok()
        if self.lexer.sym != Lexer.LPAR:
            self.error('(SyntaxError) \'(\' expected')
        self.lexer.next_tok()
        arguments = []
        while self.lexer.sym != Lexer.RPAR:
            arguments.append(self.expr())
            if self.lexer.sym != Lexer.COMA:
                break
            else:
                self.lexer.next_tok()
        if self.lexer.sym != Lexer.RPAR:
            self.error('(SyntaxError) \')\' expected')
        self.lexer.next_tok()
        return arguments

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
        if self.lexer.sym == Lexer.QUESTION_MARK:
            self.lexer.next_tok()
            op2 = self.expr()
            if self.lexer.sym != Lexer.DOUBLE_DOT:
                self.error('(SyntaxError) : expected')
            self.lexer.next_tok()
            op3 = self.expr()
            if op2.kind == Parser.EMPTY or op3.kind == Parser.EMPTY:
                self.error('(SyntaxError) expresion expected')
            n = Node(kind=Parser.IF2, op1=n, op2=op2, op3=op3)
        return n

    def statement(self):
        if self.lexer.sym == Lexer.IF:
            self.lexer.next_tok()
            # self.is_func = True
            op1 = self.paren_expr()
            if op1.kind == self.EMPTY:
                self.error('(SyntaxError) must be condition in "if" statement')
            n = Node(kind=Parser.IF1, op1=op1, op2=self.statement())
            if self.lexer.sym == Lexer.ELSE:
                n.kind = Parser.IF2
                self.lexer.next_tok()
                n.op3 = self.statement()
            # self.is_func = False
        elif self.lexer.sym == Lexer.WHILE:
            self.lexer.next_tok()
            n = Node(kind=Parser.WHILE, op1=self.paren_expr(), op2=self.statement())
        elif self.lexer.sym == Lexer.DO:
            self.lexer.next_tok()
            n = Node(kind=Parser.DO, op1=self.statement())
            if self.lexer.sym != Lexer.WHILE:
                self.error('(SyntaxError) \'while\' expected')
            self.lexer.next_tok()
            n.op2 = self.paren_expr()
            if self.lexer.sym != Lexer.SEMICOLON:
                self.error('(SyntaxError) \';\' expected')
        elif self.lexer.sym == Lexer.RETURN:
            self.lexer.next_tok()
            n = Node(kind=Parser.RETURN, op1=self.statement(), cur_func=self.cur_func)
        elif self.lexer.sym == Lexer.SEMICOLON:
            n = Node(kind=Parser.EMPTY)
            self.lexer.next_tok()
        elif self.lexer.sym == Lexer.LBRA:
            n = Node(kind=Parser.EMPTY)
            self.lexer.next_tok()
            self.vars.new_level()
            for value in self.arguments:
                self.vars.add_variable(value['value'].split('_')[0], value['type'], True)
            while self.lexer.sym != Lexer.RBRA:
                n = Node(kind=Parser.SEQ, op1=n, op2=self.statement())
            self.vars.prev_level()
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
