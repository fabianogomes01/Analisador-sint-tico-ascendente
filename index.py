import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN']

# Regras de expressão regular para tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

# Regra para token NUMBER (número)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Regra para ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Tratamento de erro
def t_error(t):
    print("Caractere ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

# Cria o analisador léxico
lexer = lex.lex()

# Regras de produção
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_paren(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

# Tratamento de erro
def p_error(p):
    print("Erro de sintaxe")

# Cria o analisador sintático
parser = yacc.yacc()

# Teste do analisador sintático
input_string = "2 + 3 * (4 - 1)"
result = parser.parse(input_string, lexer=lexer)
print("Resultado:", result)
