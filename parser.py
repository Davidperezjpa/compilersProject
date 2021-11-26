import ply.yacc as yacc
from lexer import *

# Parsing rules
precedence = (
    ('left', '+', '-'),
    ('left', '*', '/'),
    ('right', 'UMINUS'),
)

# dictionary of names
names = {}
abstractTree = []

# Production of S->
def p_block(p):
    ''' block : code block
            | code '''
    p[0] = p[1]

def p_code(p):
    '''code : statement SEMICOLON 
            | flowctrl '''
    p[0] = p[1]

def p_statement_declare_int(p):
    '''statement : INTDEC NAME is_assing
    '''
    if type(p[3]) == 'float':
        print('No puedes asignar flotantes a enteros')
    else:
        names[p[2]] = { "type": "INT", "value": p[3]}

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
    ''' statement : expression''' 
    p[0] = p[1]

def p_is_assing(p):
    '''is_assing : "=" expression 
                | '''
    p[0] = 0
    if len(p) > 2:
        p[0] = p[2]

# ---------------------------------------------------
# ------------------- EXPRESSIONS -------------------
# ---------------------------------------------------

def p_bridge_expr_boolean(p):     # allows for a expression to be a expression_boolean
    '''expression : expression_boolean
                | '''
    print("p_bridge_expr_boolean")
    p[0] = p[1]

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | expression '^' expression'''
    print("p_expression_binop")
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
    '''expression_boolean : expression EQUAL expression
                  | expression NOTEQUAL expression
                  | expression GREATER expression
                  | expression LESSTHAN expression
                  | expression GREATEREQUAL expression
                  | expression LESSEQUAL expression'''
    print("p_expression_compare")
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


def p_expression_boolean_andor(p):
    '''expression_boolean : expression AND expression
                  | expression OR expression'''
    print("p_expression_boolean_andor")
    if p[2] == '&&':
        p[0] = p[1] and p[3]
    elif p[2] == '||':
        p[0] = p[1] or p[3]
    else:
        p[0] = None
    


def p_expression_uminus(p):
    "expression : '-' expression %prec UMINUS"
    print("p_expression_uminus")
    p[0] = -p[2]

def p_expression_group(p):
    "expression : '(' expression ')'"
    print("p_expression_group")
    p[0] = p[2]

def p_expression_inumber(p):
    "expression : INUMBER"
    print("p_expression_inumber")
    p[0] = p[1]

def p_expression_fnumber(p):
    "expression : FNUMBER"
    print("p_expression_fnumber")
    p[0] = p[1]

def p_expression_boolean(p):
    "expression_boolean :  BOOLEAN"
    print("p_expression_boolean_single")
    p[0] = p[1]

def p_expression_string(p):
    "expression :  STRING"
    print("p_expression_string")
    p[0] = p[1][1:len(p[1]) - 1]



def p_expression_name(p):       # obtiene el valor de una variable previamente guardada
    "expression : NAME"
    print("p_expression_name")
    # print(p[1])
    try:
        p[0] = names[p[1]]["value"]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0


def p_flowctrl_if(p):
    ''' flowctrl : IF '(' expression_boolean ')' '{' block '}' elif else '''
    print("p_flowctrl_if")
    # p[0] = p[6]

def p_elif(p):
    ''' elif : ELIF '(' expression_boolean ')' '{' block '}' elif
        |  '''
    print("p_elif")
    # p[0] = p[6]

def p_else(p):
    ''' else : ELSE '{' block '}' 
        |  '''
    print("p_else")
    # p[0] = p[3]

def p_error(p):
    # raise (Exception(p))
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
print(lines)
# for line in lines:
#     if line != '\n':
#         print(line)
#     yacc.parse(line)
parser.parse(lexer=lexer, input=open("textFile.txt").read())
print('Compiled successfully')