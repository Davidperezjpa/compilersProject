import ply.lex as lex

#TODO Operaciones
#DONE Aritméticas
#DONE Comparación
#DONE Booleanas
#DONE Operaciones de bloques

#DONE Tipos de datos
#DONE Int
#DONE Float
#DONE String
#DONE Bolean

#DONE Operaciones permitidas entre sistema de tipos
#TODO Flujo de control
#DONE If/Else/Elif
#DONE While
# For
#DONE terminacion de ;
#TODO Arbol sintáctico
#TODO salida de codigo de 3 direcciones



literals = ['=', '+', '-', '*', '/', '^', '(', ')', '{', '}']
reserved = { 
    'int' : 'INTDEC',
    'float' : 'FLOATDEC',
    'string' : 'STRINGDEC',
    'boolean' : 'BOOLEANDEC',
    'print' : 'PRINT',
    'if' : 'IF',
    'else' : 'ELSE',
    'elif' : 'ELIF',
    'while' : 'WHILE'

 }

tokens = [
    'INUMBER', 'FNUMBER', 'STRING', 'BOOLEAN', 'NAME', 'SEMICOLON', 'EQUAL', 'NOTEQUAL', 'GREATER', 'LESSTHAN', 'GREATEREQUAL', 'LESSEQUAL', 'AND', 'OR'
] + list(reserved.values())


t_EQUAL            = r'=='
t_NOTEQUAL         = r'!='
t_GREATER          = r'>'
t_LESSTHAN         = r'<'
t_GREATEREQUAL     = r'>='
t_LESSEQUAL        = r'<='
t_AND        = r'&&'
t_OR        = r'\|\|'


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