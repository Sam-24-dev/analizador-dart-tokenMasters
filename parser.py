"""
Analizador Sintáctico para Dart - Proyecto TokenMasters
Utiliza PLY (Python Lex-Yacc)
Integrantes:
- Andrés Salinas (ivandresalin)
- Mateo Mayorga (bironmanusa)
- Samir Caizapasto (Sam-24-dev)
"""

import ply.yacc as yacc
from lexer import tokens
from datetime import datetime
import os

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
)

# ============================================================================
# INICIO APORTE: Mateo Mayorga (bironmanusa)
# Responsable: Estructura base, variables, expresiones, estructuras de datos
# ============================================================================

# TODO Mateo: Implementar reglas de:
# - Programa principal (p_program)
# - Declaración de variables (var, final, const)
# - Expresiones aritméticas (+, -, *, /, %)
# - Expresiones booleanas (==, !=, <, >, &&, ||)
# - Listas: [1, 2, 3]
# - Mapas: {'key': value}
# - Clases básicas

# Regla temporal para que compile
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement
                      | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : function_declaration
                 | print_statement
                 | return_statement
                 | variable_declaration
                 | assignment
                 | expression SEMICOLON'''
    p[0] = p[1]

def p_variable_declaration(p):
    '''variable_declaration : VAR ID ASSIGN expression SEMICOLON
                            | tipo ID ASSIGN expression SEMICOLON
                            | tipo ID SEMICOLON'''
    if len(p) == 6:
        p[0] = ('var_decl', p[1], p[2], p[4])
    else:
        p[0] = ('var_decl', p[1], p[2], None)

def p_assignment(p):
    '''assignment : ID ASSIGN expression SEMICOLON'''
    p[0] = ('assign', p[1], p[3])

def p_expression(p):
    '''expression : ID
                  | NUMBER
                  | STRING
                  | TRUE
                  | FALSE
                  | NULL
                  | function_call
                  | input_expression
                  | binary_operation
                  | LPAREN expression RPAREN'''
    if len(p) == 4 and p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = p[1]

def p_binary_operation(p):
    '''binary_operation : expression PLUS expression
                        | expression MINUS expression
                        | expression TIMES expression
                        | expression DIVIDE expression
                        | expression MODULO expression'''
    p[0] = ('binop', p[2], p[1], p[3])

def p_function_call(p):
    '''function_call : ID LPAREN argument_list RPAREN
                     | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = ('call', p[1], p[3])
    else:
        p[0] = ('call', p[1], [])

def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_empty(p):
    '''empty :'''
    pass

# ============================================================================
# FIN APORTE: Mateo Mayorga (bironmanusa)
# ============================================================================


# ============================================================================
# INICIO APORTE: Andrés Salinas (ivandresalin)
# Responsable: Estructuras de control
# ============================================================================

# TODO Andrés: Implementar reglas de:
# - if-else statements
# - while loops
# - for loops
# - do-while loops

# ============================================================================
# FIN APORTE: Andrés Salinas (ivandresalin)
# ============================================================================


# ============================================================================
# INICIO APORTE: Samir Caizapasto (Sam-24-dev)
# Responsable: Funciones, Print, Input
# ============================================================================

# 1. DECLARACIÓN DE FUNCIONES

# Función con tipo de retorno y parámetros
def p_function_with_params(p):
    '''function_declaration : tipo ID LPAREN parameters RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function', p[1], p[2], p[4], p[7])

# Función con tipo de retorno sin parámetros
def p_function_no_params(p):
    '''function_declaration : tipo ID LPAREN RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function', p[1], p[2], [], p[6])

# Función void con parámetros
def p_function_void_params(p):
    '''function_declaration : VOID ID LPAREN parameters RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function_void', p[2], p[4], p[7])

# Función void sin parámetros
def p_function_void_no_params(p):
    '''function_declaration : VOID ID LPAREN RPAREN LBRACE statement_list RBRACE'''
    p[0] = ('function_void', p[2], [], p[6])

# Arrow function con parámetros
def p_arrow_function_params(p):
    '''function_declaration : tipo ID LPAREN parameters RPAREN ARROW expression SEMICOLON'''
    p[0] = ('arrow_function', p[1], p[2], p[4], p[7])

# Arrow function sin parámetros
def p_arrow_function_no_params(p):
    '''function_declaration : tipo ID LPAREN RPAREN ARROW expression SEMICOLON'''
    p[0] = ('arrow_function', p[1], p[2], [], p[6])

# Parámetros de función (lista)
def p_parameters_multiple(p):
    '''parameters : parameter
                  | parameters COMMA parameter'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# Parámetro individual
def p_parameter(p):
    '''parameter : tipo ID'''
    p[0] = ('param', p[1], p[2])

# Tipo de dato
def p_tipo(p):
    '''tipo : ID'''
    p[0] = p[1]

# Return statement con valor
def p_return_with_value(p):
    '''return_statement : RETURN expression SEMICOLON'''
    p[0] = ('return', p[2])

# Return statement sin valor (void)
def p_return_void(p):
    '''return_statement : RETURN SEMICOLON'''
    p[0] = ('return', None)


# 2. PRINT STATEMENT

# Print con expresión
def p_print_expression(p):
    '''print_statement : ID LPAREN expression RPAREN SEMICOLON'''
    # Se asume que ID es 'print'
    p[0] = ('print', p[3])


# 3. INPUT STATEMENT (stdin.readLineSync)

# Lectura de input: stdin.readLineSync()
def p_input_read(p):
    '''input_expression : ID DOT ID LPAREN RPAREN'''
    # stdin.readLineSync()
    p[0] = ('input', p[1], p[3])

# ============================================================================
# FIN APORTE: Samir Caizapasto (Sam-24-dev)
# ============================================================================


# Manejo de errores
syntax_errors = []

def p_error(p):
    global syntax_errors
    if p:
        error_msg = f"Error sintáctico en línea {p.lineno}: Token inesperado '{p.value}' (tipo: {p.type})"
        syntax_errors.append(error_msg)
        print(error_msg)
        parser.errok()
    else:
        error_msg = "Error sintáctico: Final de archivo inesperado"
        syntax_errors.append(error_msg)
        print(error_msg)

# Construcción del parser
parser = None

def build_parser():
    global parser
    parser = yacc.yacc(debug=False)
    return parser

def analyze_syntax(filename, git_user):
    global syntax_errors
    syntax_errors = []
    
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    
    from lexer import build_lexer
    lexer = build_lexer()
    parser_obj = build_parser()
    
    print(f"\n{'='*70}")
    print("  ANALIZADOR SINTÁCTICO - DART - TokenMasters")
    print(f"{'='*70}")
    print(f"Archivo: {filename}")
    print(f"Usuario: {git_user}")
    
    result = parser_obj.parse(data, lexer=lexer)
    
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y-%Hh%M")
    log_filename = f"logs/sintactico-{git_user}-{timestamp}.txt"
    
    os.makedirs('logs', exist_ok=True)
    
    with open(log_filename, 'w', encoding='utf-8') as log:
        log.write("=" * 80 + "\n")
        log.write("  ANÁLISIS SINTÁCTICO - DART\n")
        log.write("  Proyecto: TokenMasters\n")
        log.write("=" * 80 + "\n\n")
        log.write(f"Archivo: {filename}\n")
        log.write(f"Usuario: {git_user}\n")
        log.write(f"Fecha: {now.strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        
        if syntax_errors:
            log.write("=" * 80 + "\n")
            log.write(f"  ERRORES SINTÁCTICOS: {len(syntax_errors)}\n")
            log.write("=" * 80 + "\n\n")
            for i, error in enumerate(syntax_errors, 1):
                log.write(f"{i}. {error}\n")
        else:
            log.write("=" * 80 + "\n")
            log.write("  ✓ ANÁLISIS EXITOSO - SIN ERRORES\n")
            log.write("=" * 80 + "\n")
    
    print(f"\nErrores: {len(syntax_errors)}")
    print(f"Log: {log_filename}")
    print(f"{'='*70}\n")

def main():
    import sys
    if len(sys.argv) >= 3:
        analyze_syntax(sys.argv[1], sys.argv[2])
    else:
        print("Uso: python parser.py <archivo.dart> <usuario-git>")
        analyze_syntax("algoritmos_prueba/algoritmo_samir.dart", "Sam-24-dev")

if __name__ == "__main__":
    main()
