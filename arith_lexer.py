# Arith_lexer.py
import ply.lex as plex


class ArithLexer:
    tokens= ("num", "varid", "assign")
    literals = ['*', '+', '(', ')', '-', ';']
    t_ignore = " "

    def __init__(self):
        self.lexer = None

    def t_num(self, t):
        r"[0-9]+"
        t.value = int (t.value)
        return t
    
    def t_varid(self, t):
        r"[A-Z]+" 
        # t.value = t.value
        return t
    
    def t_assign(self, t):
        r":=" 
        return t
    
    def build(self, **kwargs):
        self.lexer = plex.lex(module=self, **kwargs)

    def input(self, string):
        self.lexer.input(string)
    
    def token(self):
        token = self.lexer.token()
        return token if token is None else token.type 
     
    def t_error(self, t):
        print(f"Unexpected token: [{t.value[:10]}]")
        exit(1)


