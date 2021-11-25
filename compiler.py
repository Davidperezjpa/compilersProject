import ply.yacc as yacc
import ply.lex as lex

#TODO Operaciones
#DONE Aritméticas
#DONE Comparación
# Booleanas
# Operaciones de bloques

#TODO Tipos de datos
#DONE Int
#DONE Float
#DONE String
#DONE Bolean

#TODO Operaciones permitidas entre sistema de tipos
#TODO Flujo de control
# If/Else/Elif
# While
# For
#DONE terminacion de ;
#TODO Arbol sintáctico
#TODO salida de codigo de 3 direcciones



literals = ['=', '+', '-', '*', '/', '^', '(', ')']
reserved = { 
    'int' : 'INTDEC',
    'float' : 'FLOATDEC',
    'string' : 'STRINGDEC',
    'boolean' : 'BOOLEANDEC',
    'print' : 'PRINT'
 }

tokens = [
    'INUMBER', 'FNUMBER', 'STRING', 'BOOLEAN', 'NAME', 'SEMICOLON', 'EQUAL', 'NOTEQUAL', 'GREATER', 'LESSTHAN', 'GREATEREQUAL', 'LESSEQUAL'
] + list(reserved.values())


t_EQUAL            = r'=='
t_NOTEQUAL         = r'!='
t_GREATER          = r'>'
t_LESSTHAN         = r'<'
t_GREATEREQUAL     = r'>='
t_LESSEQUAL        = r'<='


# Tokens

def t_BOOLEAN(t):
    r'true|false'
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'NAME')    # Check for reserved words
    return t

def t_FNUMBER(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'".*"'
    return t


t_SEMICOLON = r';'

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Parsing rules
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}
abstractTree = []

def p_code(p):
    'code : statement SEMICOLON'

def p_statement_declare_int(p):
    '''statement : INTDEC NAME is_assing
    '''
    if type(p[3]) == 'float':
        print('No puedes asignar flotantes a enteros')
    else:
        names[p[2]] = { "type": "INT", "value": p[3]}

def p_is_assing(p):
    '''is_assing : "=" expression 
                | '''
    p[0] = 0
    if len(p) > 2:
        p[0] = p[2]

def p_statement_declare_float(p):
    'statement : FLOATDEC NAME is_assing'
    names[p[2]] = { "type": "FLOAT", "value":p[3]}

def p_statement_declare_boolean(p):
    'statement : BOOLEANDEC NAME is_assing'
    names[p[2]] = { "type": "BOOLEAN", "value":p[3]}

def p_statement_declare_string(p):
    'statement : STRINGDEC NAME is_assing'
    names[p[2]] = { "type": "STRING", "value":p[3]}

def p_statement_print(p):
    '''statement : PRINT '(' expression ')' '''
    print(p[3])

def p_statement_assign(p):
    'statement : NAME "=" expression'
    if p[1] not in names:
        print ( "You must declare a variable before using it")
    names[p[1]]["value"] = p[3]

def p_statement_expr(p):
    'statement : expression'
    # print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '^' expression'''
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
    elif p[2] == '^':
        p[0] = p[1] ** p[3]

def p_expression_compare(p):
    '''expression : expression EQUAL expression
                  | expression NOTEQUAL expression
                  | expression GREATER expression
                  | expression LESSTHAN expression
                  | expression GREATEREQUAL expression
                  | expression LESSEQUAL expression'''
    if p[2] == '==':
        p[0] = p[1] == p[3]
    elif p[2] == '!=':
        p[0] = p[1] != p[3]
    elif p[2] == '>':
        p[0] = p[1] > p[3]
    elif  p[2] == '<':
        p[0] = p[1] < p[3]
    elif p[2] == '>=':
        p[0] = p[1] >= p[3]
    elif p[2] == '<=':
        p[0] = p[1] <= p[3]
    else:
        p[0] = None
    


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    p[0] = p[2]

def p_expression_inumber(p):
    "expression : INUMBER"
    p[0] = p[1]

def p_expression_fnumber(p):
    "expression : FNUMBER"
    p[0] = p[1]

def p_expression_boolean(p):
    "expression :  BOOLEAN"
    p[0] = p[1]

def p_expression_string(p):
    "expression :  STRING"
    p[0] = p[1][1:len(p[1]) - 1]



def p_expression_name(p):       # obtiene el valor de una variable previamente guardada
    "expression : NAME"
    # print(p[1])
    try:
        p[0] = names[p[1]]["value"]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print(p)
        print("Syntax error at line '%s' character '%s'" % (p.lineno, p.lexpos) )
    else:
        print("Syntax error at EOF")

parser = yacc.yacc(debug=True)


# Console program
''' while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s:
        continue
    yacc.parse(s) '''

# File input
lines = []
with open('textFile.txt') as file:
    lines = file.readlines()

for line in lines:
    if line != '\n':
        yacc.parse(line)
print('Compiled successfully')