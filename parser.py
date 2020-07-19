from ply import yacc
from lexer import Lexer
from nonTerminal import NonTerminal
from codeGenerator import CodeGenerator


class Parser:

    tokens = Lexer().tokens

    def __init__(self):
        self.tempCount = 0
        self.codeGenerator = CodeGenerator()

    def p_program(self, p):
        "program : exp"
        pass

    def p_exp_sum(self, p):
        "exp : exp SUM exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_sub(self, p):
        "exp : exp SUB exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_mul(self, p):
        "exp : exp MUL exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_div(self, p):
        "exp : exp DIV exp"
        self.codeGenerator.generate_arithmetic_code(p, self.new_temp())

    def p_exp_integer(self, p):
        "exp : INTEGER"
        p[0] = NonTerminal()
        p[0].value = p[1]

    def new_temp(self):
        temp = "T" + str(self.tempCount)
        self.tempCount += 1
        return temp

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
