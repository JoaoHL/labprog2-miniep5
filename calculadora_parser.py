from calculadora_lexer import tokens
import ply.yacc as yacc

# As proximas quatro definicoes sao usadas
# para expressoes mais complexas, com mais
# de dois termos

def p_expressao_soma(p):
    'expressao : expressao termo MAIS'
    p[0] = p[1] + p[2]

def p_expressao_subtracao(p):
    'expressao : expressao termo MENOS'
    p[0] = p[1] - p[2]

def p_expressao_multiplicacao(p):
    'expressao : expressao termo MULTI'
    p[0] = p[1] * p[2]

def p_expressao_divisao(p):
    'expressao : expressao termo DIV'
    if p[2] != 0:
        p[0] = p[1] / p[2]
    else:
        print("Divisao por zero nao suportada.\n")

# Definicao basica de uma expressao: um termo

def p_expressao_num(p):
    'expressao : termo'
    p[0] = p[1]

# O "atomo" de cada expressao: os numeros, que
# sao nomeados como "termo" no parser

def p_termo_num(p):
    'termo : NUM'
    p[0] = p[1]

def p_error(p):
    print("Erro de sintaxe! Tente novamente.")

parser = yacc.yacc()

print("----------------- CALCULADORA POSFIXA ----------------")
print("-> Digite suas expressoes EM NOTACAO POSFIXA: ")
while True:
    try:
        exp = input('>>> ')
    except EOFError:
        break
    if not exp: 
        continue
    resultado = parser.parse(exp)
    print("Resultado : ", resultado)
