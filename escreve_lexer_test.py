# arith_lexer_test.py
from EscreveLexer import EscreveLexer

al = EscreveLexer()
al.build()
al.input('ESCREVE 2,"ola", 1, "mundo";') #"(3+5)*7")

while True:
    tk = al.token() 
    if not tk: 
        break
    print(tk,end=" ")

    