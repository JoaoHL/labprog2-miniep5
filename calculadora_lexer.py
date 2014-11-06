import ply.lex as lex

# Definicao dos tokens
tokens = (
        'NUM',
        'MAIS',
        'MENOS',
        'MULTI',
        'DIV',
)

t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTI = r'\*'
t_DIV = r'/'

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

#O analisador vai ignorar quebras de linha, espacos em branco e tabs
t_ignore = ' \t\n'

def t_error(t):
    print("Caractere nao reconhecido: '", t.value[0], "'.")
    t.lexer.skip(1)

lexer = lex.lex()
