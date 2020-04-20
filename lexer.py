from ply import lex


class Lexer:
    tokens = [
        'IF', 'WHILE', 'PRINT',
        'LRB', 'RRB', 'LCB', 'RCB',
        'INTEGER', 'SUM', 'SUB', 'MUL', 'DIV',
        'LT', 'GT', 'SEMICOLON'
    ]

    # COLONS
    t_SEMICOLON = r';'
    # BRACKETS
    t_LRB = r'\('
    t_RRB = r'\)'
    t_LCB = r'\{'
    t_RCB = r'\}'
    # OPERATOR
    t_SUM = r'\+'
    t_SUB = r'\-'
    t_MUL = r'\*'
    t_DIV = r'\/'
    t_LT = r'\<'
    t_GT = r'\>'
    # KW
    t_IF = r'if'
    t_WHILE = r'while'
    t_PRINT = r'print'

    def t_INTEGER(self, t):
        r'(\d+)'
        return t

    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    t_ignore = '\n \t'

    def t_error(self, t):
        raise Exception('Error at', t.value)

    def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)
        return self.lexer
