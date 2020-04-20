from ply import yacc
from lexer import Lexer

class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        pass

    def p_program(self, p):
        "program : exp"
        print('program : exp')

    def p_exp_sum(self, p):
        "exp : exp SUM exp"
        print('exp : exp SUM exp')

    def p_exp_sub(self, p):
        "exp : exp SUB exp"
        print('exp : exp SUB exp')

    def p_exp_mul(self, p):
        "exp : exp MUL exp"
        print('exp : exp MUL exp')

    def p_exp_div(self, p):
        "exp : exp DIV exp"
        print('exp : exp DIV exp')

    def p_exp_integer(self, p):
        "exp : INTEGER"
        print('exp : INTEGER', p[1])


    precedence = (
        ('left', 'SUM', 'SUB'),
        ('left', 'MUL', 'DIV')
    )

    def p_error(self, p):
        print(p.value)
        raise Exception('ParsingError: invalid grammar at ', p)

    def build(self, **kwargs):
        """build the parser"""
        self.parser = yacc.yacc(module=self, **kwargs)
        return self.parser
