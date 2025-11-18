"""
Analizador Sintáctico y Semántico para Dart - Proyecto TokenMasters
Utiliza PLY (Python Lex-Yacc)
Integrantes:
- Andrés Salinas (ivandresalin)
- Mateo Mayorga (bironmanusa)
- Samir Caizapasto (Sam-24-dev)

AVANCE 2: Análisis Sintáctico ✅ COMPLETADO
AVANCE 3: Análisis Semántico ✅ COMPLETADO
  ✅ Samir: Reglas de Retorno de Funciones y break/continue
  ✅ Andrés: Reglas de Identificadores (Alcance, Existencia, Inmutabilidad)
  ✅ Mateo: Reglas de Operaciones (Null Safety, Compatibilidad, Conversiones)
"""

import ply.yacc as yacc
from lexer import tokens
from datetime import datetime
import os

# ============================================================================
# TABLAS SEMÁNTICAS - Avance 3 (Samir/Andrés/Mateo)
# ============================================================================
# Pila de tablas de símbolos para manejar el alcance (scopes). scope_stack[0] es el ámbito global.
scope_stack = [{}] # Ámbito global inicial
function_table = {}    # Tabla de funciones: firmas y tipos de retorno
loop_stack = []        # Stack de loops: validar break/continue
semantic_errors = []   # Lista de errores semánticos

# Precedencia de operadores
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MODULO'),
)

# ============================================================================
# GESTIÓN DE ÁMBITOS (SCOPES) - [Andrés Salinas]
# ============================================================================

def push_scope():
    """Abre un nuevo ámbito (nuevo diccionario) y lo añade a la pila."""
    scope_stack.append({})
    
def pop_scope():
    """Cierra el ámbito actual (elimina el último diccionario de la pila)."""
    if len(scope_stack) > 1:
        scope_stack.pop()
        
def get_current_scope():
    """Retorna la tabla de símbolos del ámbito actual."""
    return scope_stack[-1]

def lookup_variable(name, local_only=False):
    """
    Busca una variable por nombre, desde el ámbito actual hacia el global.
    Retorna el diccionario de información de la variable (tipo, inmutabilidad) o None.
    Implementa el alcance léxico (lexical scoping).
    """
    # Recorrer la pila de ámbitos de arriba a abajo (local a global)
    for scope in reversed(scope_stack):
        if name in scope:
            return scope[name] # Retorna el dict: {'type': 'int', 'is_final': True, ...}
        # Si solo buscamos localmente, paramos tras el ámbito actual
        if local_only:
            break
    return None # No encontrado

# ============================================================================
# INICIO APORTE: Mateo Mayorga (bironmanusa)
# Responsable: Estructura base, variables, expresiones, estructuras de datos
# ============================================================================

# ---------------- REGLA DE PROGRAMA PRINCIPAL ----------------
def p_program(p):
    '''program : statement_list'''
    p[0] = ('program', p[1])

# ---------------- LISTA DE SENTENCIAS ----------------
def p_statement_list(p):
    '''statement_list : statement
                      | statement_list statement
                      | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = p[1] + [p[2]]

# ---------------- SENTENCIA ----------------
def p_statement(p):
    '''statement : if_statement
                 | while_statement
                 | do_while_statement
                 | for_statement
                 | for_in_statement
                 | break_statement
                 | continue_statement
                 | function_declaration
                 | print_statement
                 | return_statement
                 | variable_declaration
                 | assignment
                 | class_declaration
                 | expression SEMICOLON
                 '''
    p[0] = p[1]

# ---------------- DECLARACIÓN DE VARIABLES ----------------
def p_variable_declaration(p):
    '''variable_declaration : VAR ID ASSIGN expression SEMICOLON
                            | CONST ID ASSIGN expression SEMICOLON
                            | FINAL ID ASSIGN expression SEMICOLON
                            | tipo ID ASSIGN expression SEMICOLON
                            | tipo ID SEMICOLON'''
    # En este punto, no podemos obligar la inicialización de CONST/FINAL 
    # sin reescribir la gramática para evitar la regla 'tipo ID SEMICOLON' para ellos.
    # Se maneja en register_variable.

    if len(p) == 6:
        p[0] = ('var_decl', p[1], p[2], p[4])
        try:
            # Uso de register_variable (Mateo/Andrés/Samir)
            register_variable(p[2], p[1], p[4], p.lineno(2))
        except Exception:
            register_variable(p[2], p[1], p[4])
    else: # Regla: tipo ID SEMICOLON (p[1] es tipo o palabra clave, p[2] es ID, p[3] es SEMICOLON)
        p[0] = ('var_decl', p[1], p[2], None)
        try:
            # Uso de register_variable (Mateo/Andrés/Samir)
            register_variable(p[2], p[1], None, p.lineno(2))
        except Exception:
            register_variable(p[2], p[1], None)

# ---------------- ASIGNACIÓN ----------------
def p_assignment(p):
    '''assignment : ID ASSIGN expression SEMICOLON'''
    p[0] = ('assign', p[1], p[3])
    try:
        # Uso de validate_assignment (Mateo/Andrés/Samir)
        validate_assignment(p[1], p[3], p.lineno(1))
    except Exception:
        validate_assignment(p[1], p[3])

# ---------------- EXPRESIONES ----------------
def p_expression(p):
    '''expression : ID
                  | NUMBER
                  | STRING
                  | TRUE
                  | FALSE
                  | NULL
                  | list_literal
                  | map_literal
                  | function_call
                  | input_expression
                  | binary_operation
                  | LPAREN expression RPAREN'''
    if len(p) == 2 and isinstance(p[1], str) and p.slice[1].type == 'ID':
        # NO validar existencia aquí (PLY bottom-up causa falsos positivos)
        # La validación se hace post-parsing en validate_semantic_rules()
        p[0] = p[1]
    elif len(p) == 4 and p[1] == '(':
        p[0] = p[2]
    else:
        p[0] = p[1]

# ---------------- OPERACIONES ARITMÉTICAS Y BOOLEANAS ----------------
def p_binary_operation(p):
    '''binary_operation : expression PLUS expression
                        | expression MINUS expression
                        | expression TIMES expression
                        | expression DIVIDE expression
                        | expression MODULO expression
                        | expression EQUALS expression
                        | expression NOTEQUAL expression
                        | expression LESSTHAN expression
                        | expression GREATERTHAN expression
                        | expression LESSEQUAL expression
                        | expression GREATEREQUAL expression
                        | expression AND expression
                        | expression OR expression'''
    # Guardamos también la línea del operador para reportes más precisos
    try:
        lineno = p.lineno(2)
    except Exception:
        lineno = None
    p[0] = ('binop', p[2], p[1], p[3], lineno)

# ---------------- LISTAS ----------------
def p_list_literal(p):
    '''list_literal : LBRACKET list_elements RBRACKET
                    | LBRACKET RBRACKET'''
    if len(p) == 3:
        p[0] = ('list', [])
    else:
        p[0] = ('list', p[2])

def p_list_elements(p):
    '''list_elements : expression
                     | list_elements COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# ---------------- MAPAS ----------------
def p_map_literal(p):
    '''map_literal : LBRACE map_entries RBRACE 
                   | LBRACE RBRACE'''
    if len(p) == 3:
        p[0] = (map, {})
    else:
        p[0] = ('map', dict(p[2]))

def p_map_entries(p):
    '''map_entries : map_entry
                   | map_entries COMMA map_entry'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

def p_map_entry(p):
    '''map_entry : STRING COLON expression'''
    p[0] = (p[1], p[3])

# ---------------- CLASES BÁSICAS ----------------
def p_class_declaration(p):
    '''class_declaration : CLASS ID LBRACE class_members RBRACE'''
    
    # 1. Gestión de Ámbito de la Clase (propiedades y métodos)
    push_scope() # Empieza el ámbito de la clase
    
    # 2. class_members [p[4]] se procesan dentro del nuevo ámbito
    p[0] = ('class', p[2], p[4])
    
    pop_scope() # Cierra el ámbito de la clase

def p_class_members(p):
    '''class_members : class_member
                     | class_members class_member
                     | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] else []
    else:
        p[0] = p[1] + [p[2]]

def p_class_member(p):
    '''class_member : variable_declaration
                    | function_declaration'''
    p[0] = p[1]

# ---------------- LLAMADAS A FUNCIÓN ----------------
def p_function_call(p):
    '''function_call : ID LPAREN argument_list RPAREN
                     | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = ('call', p[1], p[3])
    else:
        p[0] = ('call', p[1], [])

# ---------------- ARGUMENTOS DE FUNCIÓN ----------------
def p_argument_list(p):
    '''argument_list : expression
                     | argument_list COMMA expression'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]

# ---------------- VACÍO ----------------
def p_empty(p):
    '''empty :'''
    pass

# ============================================================================
# HELPERS SEMÁNTICOS [Mateo Mayorga / Andrés Salinas]
# ============================================================================

def is_numeric_type(t):
    return t in ('int', 'double', 'num')

def get_base_type(var_info):
    """Extrae el tipo base (string) de la información de la variable."""
    return var_info['type'] if isinstance(var_info, dict) else var_info

def can_implicitly_convert(from_t, to_t):
    """Reglas de conversión implícita:
    - int -> double es implícito (ej: 3 a 3.0)
    - int/double -> num implícito
    - mismo tipo: ok
    """
    if from_t == to_t:
        return True
    if from_t == 'int' and to_t == 'double':
        return True
    if (from_t in ('int', 'double') and to_t == 'num'):
        return True
    return False

def infer_type(node):
    """Inferir tipo desde un nodo del AST o valor literal.
    Retorna cadenas como 'int','double','String','bool','Null','List','Map','unknown'.
    """
    # Literales python
    if node is None:
        return 'Null'
    if isinstance(node, bool):
        return 'bool'
    if isinstance(node, int):
        return 'int'
    if isinstance(node, float):
        return 'double'
    # Literales string ahora se representan como tupla ('str', valor)
    if isinstance(node, tuple) and len(node) == 2 and node[0] == 'str':
        return 'String'
    if isinstance(node, list):
        return 'List'
    if isinstance(node, dict):
        return 'Map'

    # Nodos AST (tuplas)
    if isinstance(node, tuple) and len(node) > 0:
        tag = node[0]
        # binop: ('binop', op, left, right)
        if tag == 'binop':
            op = node[1]
            left_t = infer_type(node[2])
            right_t = infer_type(node[3])
            # Operadores aritméticos -> num
            if op in ('+', '-', '*', '/', '%', '~/'):
                if is_numeric_type(left_t) and is_numeric_type(right_t):
                    if 'double' in (left_t, right_t):
                        return 'double'
                    return 'int'
                # String concatenation
                if op == '+' and left_t == 'String' and right_t == 'String':
                    return 'String'
                return 'unknown'
            # comparaciones y lógicos
            if op in ('==', '!=', '<', '>', '<=', '>='):
                return 'bool'
            if op in ('&&', '||'):
                return 'bool'
            if op == '??':
                # null-aware coalescing: tipo es del operando no-null
                if left_t != 'Null':
                    return left_t
                return right_t
        # llamada a función: ('call', name, args)
        if tag == 'call':
            fname = node[1]
            f = function_table.get(fname)
            if f:
                return f.get('type', 'unknown')
            return 'unknown'
        # return, var_decl, assign, etc -> no inf
        return 'unknown'

    # identificadores: nombre de variable (cadenas simples)
    if isinstance(node, str):
        var_info = lookup_variable(node)
        # Si encuentra la variable, devuelve el tipo base. Si no, devuelve 'unknown'.
        if var_info:
            return get_base_type(var_info)
        
        # Validación de EXISTENCIA/DECLARACIÓN:
        if node not in function_table: # No es función
             # La línea del error es difícil de obtener aquí, pero la regla p_expression ya lo maneja
             pass 

        return 'unknown'

    return 'unknown'


def register_variable(name, declared_token, init_expr, lineno=None):
    """
    Registrar variable en el ámbito actual y validar compatibilidad inicial e inmutabilidad.
    """
    current_scope= get_current_scope()

    # Determinar si es inmutable (Andrés)
    # El lexer devuelve el VALUE en minúsculas, no el TYPE
    is_final = declared_token == 'final'
    is_const = declared_token == 'const'
    is_keyword = declared_token in ('var', 'const', 'final')
    
    # Validar RE-DECLARACIÓN LOCAL (Alcance)
    if name in current_scope:
        semantic_errors.append(f"Línea {lineno}: Error semántico: Variable '{name}' ya declarada en este ámbito.")
        return # No registrar si ya existe en el ámbito local

    # 1. Validación de Inicialización para inmutables (Regla de Dart - Andrés)
    if (is_final or is_const) and init_expr is None:
        semantic_errors.append(f"Línea {lineno}: Error semántico: La variable '{name}' declarada como {declared_token} debe ser inicializada.")
    
    # 2. Determinar el tipo inferido o declarado
    if is_keyword:
        # Si es palabra clave (var, final, const), inferimos
        if init_expr is not None:
            t = infer_type(init_expr)
        else:
            t = 'dynamic'
    else:
        # Declarado con tipo explícito (ej: 'int')
        t = declared_token

    # Estructura de registro unificada: tipo + propiedades de inmutabilidad
    var_info = {
        'type': t,
        'is_final': is_final,
        'is_const': is_const
    }
    current_scope[name] = var_info

    # 3. Validación de compatibilidad inicial (Solo si NO fue palabra clave)
    # Si usamos var, final, o const, la compatibilidad es implícita (inferida).
    if init_expr is not None and not is_keyword:
        declared_type = t
        expr_t = infer_type(init_expr)
        
        if expr_t == 'unknown':
            pass  # No reportar error si no se pudo inferir (puede ser función no declarada aún)
        elif not can_implicitly_convert(expr_t, declared_type):
            if is_numeric_type(expr_t) and is_numeric_type(declared_type):
                semantic_errors.append(f"Línea {lineno}: Asignación de '{expr_t}' a '{declared_type}' en '{name}' puede requerir conversión explícita/cast")
            else:
                semantic_errors.append(f"Línea {lineno}: Tipo incompatible al inicializar '{name}': '{expr_t}' no es '{declared_type}'")


def validate_assignment(target_name, expr_node, lineno=None):
    """
    Validar asignación a variable (Compatibilidad e Inmutabilidad).
    """
    
    # 1. Existencia y Obtención del objeto de información de la variable
    var_info = lookup_variable(target_name)
    
    if var_info is None:
        # Error: Variable no declarada (existencia)
        semantic_errors.append(f"Línea {lineno}: Error semántico: Intento de asignar a identificador no declarado: '{target_name}'")
        return # Sale si no existe

    # 2. Validación de INMUTABILIDAD (Regla de Dart - Andrés)
    if var_info.get('is_final') or var_info.get('is_const'):
        semantic_errors.append(f"Línea {lineno}: Error semántico: No se puede asignar a la variable inmutable '{target_name}'.")
        return # Sale si es inmutable

    # 3. Evaluación del Tipo de la Expresión y Tipo Declarado
    declared_type = get_base_type(var_info)
    expr_t = infer_type(expr_node)
    
    if declared_type == 'dynamic' or expr_t == 'unknown' or declared_type == 'unknown':
        return
        
    # Validaciones de Compatibilidad de Tipo
    
    # Si ambos numéricos, revisar convertibilidad
    if is_numeric_type(expr_t) and is_numeric_type(declared_type):
        # int -> double OK; double -> int requiere cast (Compatibilidad)
        if expr_t == 'double' and declared_type == 'int': 
            semantic_errors.append(f"Línea {lineno}: Asignación de 'double' a 'int' en '{target_name}' requiere cast explícito")
        return
        
    # compatibles iguales
    if expr_t == declared_type: 
        return
        
    # comparar String/bool
    if declared_type == 'String' and expr_t != 'String': 
        semantic_errors.append(f"Línea {lineno}: No se puede asignar '{expr_t}' a 'String' en '{target_name}'")
        return
        
    if declared_type == 'bool' and expr_t != 'bool': 
        semantic_errors.append(f"Línea {lineno}: No se puede asignar '{expr_t}' a 'bool' en '{target_name}'")
        return
        
    # casos generales
    if not can_implicitly_convert(expr_t, declared_type): # Usar declared_type
        semantic_errors.append(f"Línea {lineno}: Asignación incompatible: '{expr_t}' no se convierte implícitamente a '{declared_type}' en '{target_name}'")

def validate_binary_operations(tree):
    """Recorre el AST y valida operaciones binarias respecto a tipos y null-safety."""
    if tree is None:
        return
    if isinstance(tree, list):
        for item in tree:
            validate_binary_operations(item)
        return
    if not isinstance(tree, tuple) or len(tree) == 0:
        return
    node_type = tree[0]
    if node_type == 'binop':
        op = tree[1]
        left = tree[2]
        right = tree[3]
        lt = infer_type(left)
        rt = infer_type(right)
        lineno = None
        if len(tree) > 4:
            lineno = tree[4]
        
        # Si no se pudo inferir algún tipo, no validar (evitar falsos positivos)
        if lt == 'unknown' or rt == 'unknown':
            # Recursión y salir
            for child in tree[1:]:
                validate_binary_operations(child)
            return
        
        # Null safety: si alguno es Null y op no es '??' o comparación, alertar
        if ('Null' in (lt, rt)) and op not in ('??', '==', '!='):
            if lineno:
                semantic_errors.append(f"Línea {lineno}: Operación '{op}' con valor null sin comprobación")
            else:
                semantic_errors.append(f"Operación '{op}' con valor null sin comprobación")
        # Operadores aritméticos
        if op in ('+', '-', '*', '/', '%', '~/'):
            if not (is_numeric_type(lt) and is_numeric_type(rt)):
                # permitir concatenación String + String
                if not (op == '+' and lt == 'String' and rt == 'String'):
                    if lineno:
                        semantic_errors.append(f"Línea {lineno}: Operador aritmético '{op}' requiere operandos numéricos (encontrado '{lt}', '{rt}')")
                    else:
                        semantic_errors.append(f"Operador aritmético '{op}' requiere operandos numéricos (encontrado '{lt}', '{rt}')")
        # Operadores lógicos
        if op in ('&&', '||'):
            if lt != 'bool' or rt != 'bool':
                if lineno:
                    semantic_errors.append(f"Línea {lineno}: Operador lógico '{op}' requiere operandos booleanos (encontrado '{lt}', '{rt}')")
                else:
                    semantic_errors.append(f"Operador lógico '{op}' requiere operandos booleanos (encontrado '{lt}', '{rt}')")
        # Comparaciones: permitir entre tipos comparables
        if op in ('==', '!=', '<', '>', '<=', '>='):
            if lt != rt and not (is_numeric_type(lt) and is_numeric_type(rt)):
                if lineno:
                    semantic_errors.append(f"Línea {lineno}: Comparación '{op}' entre tipos incompatibles ('{lt}', '{rt}')")
                else:
                    semantic_errors.append(f"Comparación '{op}' entre tipos incompatibles ('{lt}', '{rt}')")

    # Recursión en hijos
    for child in tree[1:]:
        validate_binary_operations(child)


def validate_semantic_rules(tree):
    """
    Recorrido Post-Parse: Solo para validaciones que requieren el AST completo 
    (como break/continue y operaciones binarias), NO para registro de símbolos.
    """
    # 1) Validar break/continue (ya existente)
    validate_break_continue(tree, in_loop=False)
    
    # 2) Validar operaciones binarias y null-safety
    validate_binary_operations(tree)
    
    # IMPORTANTE: Se elimina la función walk_and_validate
    # que causaba la doble registración de variables.

# ============================================================================
# FIN APORTE: Mateo Mayorga (bironmanusa)
# ============================================================================


# ============================================================================
# INICIO APORTE: Andrés Salinas (ivandresalin)
# Responsable: Estructuras de control (Añadido manejo de ámbito de bloque)
# ============================================================================

# Sentencia compuesta o simple (ayuda a aceptar bloques con o sin llaves).
def p_block_or_statement(p):
    '''block_or_statement : LBRACE statement_list RBRACE
                          | statement'''
    # Esta regla solo normaliza el AST; el manejo de ámbito se hace en las estructuras de control.
    if len(p) == 4:
        p[0] = ('block', p[2])   # bloque: lista de sentencias
    else:
        p[0] = ('block', [p[1]]) # normalizamos a bloque con una sola sentencia

# ---------------- IF / ELSEIF / ELSE ----------------
def p_if_statement(p):
    '''if_statement : IF LPAREN expression RPAREN statement_block
                    | IF LPAREN expression RPAREN statement_block ELSE statement_block
                    | IF LPAREN expression RPAREN statement_block else_if_list'''
    
    # El statement_block (p[5]) ya maneja el push/pop scope internamente.
    
    # Caso simple: if (cond) stmt
    if len(p) == 6:
        p[0] = ('if', p[3], p[5], None)
    # if ... else ...
    elif len(p) == 8 and p[6] == 'ELSE':
        p[0] = ('if', p[3], p[5], p[7])
    # if ... else-if list (else_if_list devuelve un árbol que puede terminar en else o None)
    else:
        # estructura: IF LPAREN expr RPAREN statement_block else_if_list
        p[0] = ('if_chain', p[3], p[5], p[6])

# lista de else-if (puede finalizar con un else opcional)
def p_else_if_list(p):
    '''else_if_list : ELSE IF LPAREN expression RPAREN statement_block
                    | ELSE IF LPAREN expression RPAREN statement_block else_if_list
                    | ELSE statement_block'''
    # else if simple
    if len(p) == 7 and p[1] == 'ELSE' and p[2] == 'IF':
        # devuelve una lista encadenada como ('elif', cond, block, next) donde next puede ser otra elif o None
        p[0] = ('elif', p[4], p[6], None)
    # else if seguido de más else-if
    elif len(p) == 8:
        p[0] = ('elif', p[4], p[6], p[7])
    # else final
    else:
        p[0] = ('else', p[2])

# Regla de bloque con gestión de ámbito
def p_statement_block(p):
    '''statement_block : LBRACE statement_list RBRACE
                       | statement'''
    
    if len(p) == 4:
        # Si tiene llaves, se crea un ámbito explícito para el bloque.
        push_scope()
        result = ('block', p[2])
        pop_scope()
        p[0] = result
    else:
        # Si es una sola sentencia, el ámbito es el del padre (no se necesita push/pop).
        p[0] = p[1]


# ---------------- WHILE ----------------
def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN statement_block'''
    # El statement_block (p[5]) ya maneja el push/pop scope internamente.
    p[0] = ('while', p[3], p[5])

# ---------------- DO-WHILE ----------------
def p_do_while_statement(p):
    '''do_while_statement : DO statement_block WHILE LPAREN expression RPAREN SEMICOLON'''
    # El statement_block (p[2]) ya maneja el push/pop scope internamente.
    p[0] = ('do_while', p[2], p[5])

# ---------------- FOR (tradicional) ----------------
# Para la parte de inicialización permitimos variable_declaration, assignment o empty.
def p_for_statement(p):
    '''for_statement : FOR LPAREN for_init SEMICOLON for_condition SEMICOLON for_update RPAREN statement_block'''
    # El statement_block (p[9]) ya maneja el push/pop scope internamente.
    p[0] = ('for', p[3], p[5], p[7], p[9])

def p_for_init(p):
    '''for_init : variable_declaration_no_semicolon
                | assignment_no_semicolon
                | empty'''
    p[0] = p[1]

def p_for_condition(p):
    '''for_condition : expression
                     | empty'''
    p[0] = p[1]

def p_for_update(p):
    '''for_update : expression
                  | assignment_no_semicolon
                  | empty'''
    p[0] = p[1]

# versiones de reglas sin punto y coma para usar en la cabecera del for
def p_variable_declaration_no_semicolon(p):
    '''variable_declaration_no_semicolon : VAR ID ASSIGN expression
                                         | CONST ID ASSIGN expression
                                         | FINAL ID ASSIGN expression
                                         | tipo ID ASSIGN expression
                                         | tipo ID'''
    if len(p) == 5:
        p[0] = ('var_decl', p[1], p[2], p[4])
        # Nota: Estas variables se registran en el ámbito actual de la función/bloque.
    else:
        p[0] = ('var_decl', p[1], p[2], None)

def p_assignment_no_semicolon(p):
    '''assignment_no_semicolon : ID ASSIGN expression'''
    p[0] = ('assign', p[1], p[3])

# ---------------- FOR-IN (for each) ----------------
def p_for_in_statement(p):
    '''for_in_statement : FOR LPAREN for_in_iterator IN expression RPAREN statement_block'''
    # El statement_block (p[7]) ya maneja el push/pop scope internamente.
    p[0] = ('for_in', p[3], p[5], p[7])

#iterador del for-in (iterator)
def p_for_in_iterator(p):
    '''for_in_iterator : VAR ID
                       | ID''' # ID aquí asume que ID puede ser un tipo de dato
    if len(p) == 3:
        p[0] = ('iterator_decl', p[1], p[2])
    else:
        p[0] = ('iterator_id', p[1])

# ---------------- BREAK / CONTINUE ----------------
def p_break_statement(p):
    '''break_statement : BREAK SEMICOLON'''
    # Guardamos línea para validación semántica post-parsing (Samir - Regla 2.2)
    p[0] = ('break', p.lineno(1))

def p_continue_statement(p):
    '''continue_statement : CONTINUE SEMICOLON'''
    # Guardamos línea para validación semántica post-parsing (Samir - Regla 2.2)
    p[0] = ('continue', p.lineno(1))


# ============================================================================
# FIN APORTE: Andrés Salinas (ivandresalin)
# ============================================================================


# ============================================================================
# INICIO APORTE: Samir Caizapasto (Sam-24-dev)
# Responsable: Funciones, Print, Input
# ============================================================================

# ========== FUNCIONES HELPER SEMÁNTICAS (Samir - Avance 3) ==========

def validate_return_type(declared_type, return_expression):
    """Valida si el tipo de retorno coincide con el declarado (Samir - Regla 1.1)"""
    if return_expression is None:
        # Return vacío (void)
        return declared_type == 'void'
    
    # Inferir tipo de la expresión de retorno
    expr_type = infer_type(return_expression)
    
    # Si no se pudo inferir, aceptar (evitar falsos positivos)
    if expr_type == 'unknown':
        return True
    
    # Validar compatibilidad de tipos
    if declared_type == 'void' and expr_type != 'Null':
        return False  # void no debe retornar valor
    
    if declared_type == expr_type:
        return True  # Tipos iguales
    
    # Conversión implícita permitida
    if can_implicitly_convert(expr_type, declared_type):
        return True
    
    return False

def has_return_in_all_paths(statement_list):
    """Verifica si todos los caminos de ejecución tienen return (Samir - Regla 1.2)"""
    if not statement_list:
        return False
    
    for stmt in statement_list:
        if isinstance(stmt, tuple) and len(stmt) > 0:
            stmt_type = stmt[0]
            
            # Return directo encontrado
            if stmt_type == 'return':
                return True
            
            # Validar if-else: AMBAS ramas deben retornar
            if stmt_type == 'if' and len(stmt) >= 4:
                # stmt = ('if', condition, then_block, else_block)
                then_block = stmt[2]
                else_block = stmt[3]
                
                if else_block is not None:
                    # Si hay else, verificar que AMBAS ramas retornen
                    then_has_return = has_return_in_block(then_block)
                    else_has_return = has_return_in_block(else_block)
                    
                    if then_has_return and else_has_return:
                        return True
            
            # Validar if-chain (else-if): todas las ramas deben retornar
            if stmt_type == 'if_chain' and len(stmt) >= 4:
                # stmt = ('if_chain', condition, then_block, elif_chain)
                then_block = stmt[2]
                elif_chain = stmt[3]
                
                if has_return_in_block(then_block) and has_return_in_elif_chain(elif_chain):
                    return True
    
    return False

def has_return_in_block(block):
    """Verifica si un bloque tiene return (Samir - Helper para Regla 1.2)"""
    if block is None:
        return False
    
    # Si es un bloque con lista de statements
    if isinstance(block, tuple) and len(block) > 0:
        if block[0] == 'block' and len(block) >= 2:
            return has_return_in_all_paths(block[1])
        elif block[0] == 'return':
            return True
    
    # Si es una lista de statements directamente
    if isinstance(block, list):
        return has_return_in_all_paths(block)
    
    return False

def has_return_in_elif_chain(elif_chain):
    """Verifica si cadena de elif/else tiene return en todas las ramas (Samir - Helper para Regla 1.2)"""
    if elif_chain is None:
        return False
    
    if not isinstance(elif_chain, tuple) or len(elif_chain) == 0:
        return False
    
    chain_type = elif_chain[0]
    
    # Si termina en 'else', verificar que tenga return
    if chain_type == 'else' and len(elif_chain) >= 2:
        return has_return_in_block(elif_chain[1])
    
    # Si es 'elif', verificar que esta rama Y la siguiente retornen
    if chain_type == 'elif' and len(elif_chain) >= 4:
        # elif_chain = ('elif', condition, block, next_chain)
        current_block = elif_chain[2]
        next_chain = elif_chain[3]
        
        # AMBAS deben retornar: el elif actual Y la cadena siguiente
        return has_return_in_block(current_block) and has_return_in_elif_chain(next_chain)
    
    return False

def validate_break_continue(tree, in_loop=False):
    """
    Valida que break/continue solo aparezcan dentro de bucles (Samir - Regla 2.2)
    
    Se ejecuta DESPUÉS del parsing porque:
    - PLY usa parsing bottom-up (reduce primero las hojas, luego los padres)
    - Intentar usar loop_stack durante el parsing causa falsos positivos
    - Esta función recorre el árbol de arriba hacia abajo
    
    Parámetros:
    - tree: Árbol sintáctico (tupla o lista) generado por el parser
    - in_loop: Flag que indica si estamos dentro de un bucle
    """
    # Si es None o vacío, terminar
    if tree is None:
        return
    
    # Si es una lista (statement_list), recorrer cada elemento
    if isinstance(tree, list):
        for item in tree:
            validate_break_continue(item, in_loop)
        return
    
    # Si no es tupla, no hay nada que validar
    if not isinstance(tree, tuple) or len(tree) == 0:
        return
    
    node_type = tree[0]
    
    # Si encontramos un bucle, activamos el flag para sus hijos
    if node_type in ('while', 'for', 'do-while', 'for-in'):
        # while: ('while', condition, body)
        # for: ('for', init, condition, update, body)
        # do-while: ('do-while', body, condition)
        # for-in: ('for-in', variable, iterable, body)
        
        # Recorrer TODOS los hijos CON in_loop=True
        for child in tree[1:]:
            validate_break_continue(child, in_loop=True)
    
    # Si encontramos break/continue, verificamos si estamos en bucle
    elif node_type == 'break':
        if not in_loop:
            semantic_errors.append("Error semántico: 'break' fuera de bucle")
    
    elif node_type == 'continue':
        if not in_loop:
            semantic_errors.append("Error semántico: 'continue' fuera de bucle")
    
    # Para cualquier otro nodo, seguir recorriendo CON el mismo flag
    else:
        for child in tree[1:]:
            validate_break_continue(child, in_loop)

# ========== 1. DECLARACIÓN DE FUNCIONES (Gestión de Alcance) ==========

# Función con tipo de retorno y parámetros
def p_function_with_params(p):
    '''function_declaration : tipo ID LPAREN parameters RPAREN LBRACE statement_list RBRACE'''
    # SINTÁCTICO: Reconocer estructura
    func_type = p[1]
    func_name = p[2]
    params = p[4]
    
    # ========== SEMÁNTICA: Guardar función en tabla ANTES de procesar el cuerpo ==========
    function_params_list = []
    for tag, param_type, param_name in params: 
        function_params_list.append((param_type, param_name))
    function_table[func_name] = {'type': func_type, 'params': function_params_list}
    # ========== FIN REGISTRO PREVIO ==========
    
    # 1. Entrar a nuevo ámbito para la función (Alcance)
    push_scope()
    
    # 2. Registrar los parámetros en el nuevo ámbito (Scope)
    for tag, param_type, param_name in params: 
        # Los parámetros de Dart son implícitamente final
        get_current_scope()[param_name] = {'type': param_type, 'is_final': True, 'is_const': False}
    
    # 3. Procesar el cuerpo (statement_list se procesa DENTRO del scope con parámetros)
    body = p[7]
    
    # ========== SEMÁNTICA: Validar retornos (Samir - Regla 1) ==========
    # Validar que la función tenga return
    if func_type != 'VOID' and not has_return_in_all_paths(body):
        semantic_errors.append(f"Línea {p.lineno(2)}: Función '{func_name}' debe retornar '{func_type}' en todos los caminos")
    # ========== FIN SEMÁNTICA ==========
    
    pop_scope() # Cierra el ámbito de la función
    p[0] = ('function', func_type, func_name, params, body)

# Función con tipo de retorno sin parámetros
def p_function_no_params(p):
    '''function_declaration : tipo ID LPAREN RPAREN LBRACE statement_list RBRACE'''
    # SINTÁCTICO: Reconocer estructura
    func_type = p[1]
    func_name = p[2]

    # ========== SEMÁNTICA: Guardar función en tabla ANTES de procesar el cuerpo ==========
    function_table[func_name] = {'type': func_type, 'params': []}
    # ========== FIN REGISTRO PREVIO ==========

    push_scope() # Abre el ámbito de la función

    body = p[6]
    
    # ========== SEMÁNTICA: Validar retornos (Samir - Regla 1) ==========
    if not has_return_in_all_paths(body):
        semantic_errors.append(
            f"Línea {p.lineno(2)}: Función '{func_name}' debe retornar '{func_type}' en todos los caminos"
        )
    # ========== FIN SEMÁNTICA ==========
    
    pop_scope() # Cierra el ámbito de la función
    p[0] = ('function', func_type, func_name, [], body)

# Función void con parámetros
def p_function_void_params(p):
    '''function_declaration : VOID ID LPAREN parameters RPAREN LBRACE statement_list RBRACE'''
    # SINTÁCTICO: Reconocer estructura
    func_name = p[2]
    params = p[4]
    
    # ========== SEMÁNTICA: Guardar función en tabla ANTES de procesar el cuerpo ==========
    function_params_list = []
    for tag, param_type, param_name in params: 
        function_params_list.append((param_type, param_name))
    function_table[func_name] = {'type': 'void', 'params': function_params_list}
    # ========== FIN REGISTRO PREVIO ==========
    
    push_scope() # Abre el ámbito de la función

    # Registrar los parámetros en el nuevo ámbito (Scope)
    for tag, param_type, param_name in params: 
        # Los parámetros de Dart son implícitamente final
        get_current_scope()[param_name] = {'type': param_type, 'is_final': True, 'is_const': False}
        
    body = p[7]
    # Void no requiere return, está OK
    
    pop_scope() # Cierra el ámbito de la función
    p[0] = ('function_void', func_name, params, p[7])

# Función void sin parámetros
def p_function_void_no_params(p):
    '''function_declaration : VOID ID LPAREN RPAREN LBRACE statement_list RBRACE'''
    # SINTÁCTICO: Reconocer estructura
    func_name = p[2]
    
    # ========== SEMÁNTICA: Guardar función en tabla ANTES de procesar el cuerpo ==========
    function_table[func_name] = {'type': 'void', 'params': []}
    # ========== FIN REGISTRO PREVIO ==========
    
    push_scope() # Abre el ámbito de la función
    
    # Procesar cuerpo
    body = p[6]
    # Void no requiere return, está OK
    
    pop_scope() # Cierra el ámbito de la función
    p[0] = ('function_void', func_name, [], body)

# Arrow function con parámetros
def p_arrow_function_params(p):
    '''function_declaration : tipo ID LPAREN parameters RPAREN ARROW expression SEMICOLON'''
    # SINTÁCTICO: Arrow functions siempre retornan (OK semánticamente)
    func_name = p[2]
    params = p[4]
    
    # Preparar lista limpia para Function Table
    function_params_list = []
    for tag, param_type, param_name in params: 
        # No se necesita push/pop scope aquí porque las arrow functions no crean un bloque de alcance local para variables internas
        function_params_list.append((param_type, param_name))
        
    function_table[func_name] = {'type': p[1], 'params': function_params_list}
    p[0] = ('arrow_function', p[1], func_name, p[4], p[7])

# Arrow function sin parámetros
def p_arrow_function_no_params(p):
    '''function_declaration : tipo ID LPAREN RPAREN ARROW expression SEMICOLON'''
    # SINTÁCTICO: Arrow functions siempre retornan (OK semánticamente)
    func_name = p[2]
    function_table[func_name] = {'type': p[1], 'params': []}
    p[0] = ('arrow_function', p[1], func_name, [], p[6])

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
    # El valor reducido aquí es la tupla de 3 elementos: ('param', tipo, ID)
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


# ========== 2. PRINT STATEMENT ==========

# Print con expresión
def p_print_expression(p):
    '''print_statement : ID LPAREN expression RPAREN SEMICOLON'''
    # SINTÁCTICO: Se asume que ID es 'print'
    # SEMÁNTICO: Validar que realmente se esté llamando a 'print'
    if p[1] != 'print':
        # Reportar como error semántico (no detener parsing)
        semantic_errors.append(f"Línea {p.lineno(1)}: Identificador '{p[1]}' no es la función 'print'")
    p[0] = ('print', p[3])


# ========== 3. INPUT STATEMENT (stdin.readLineSync) ==========

# Lectura de input: stdin.readLineSync()
def p_input_read(p):
    '''input_expression : ID DOT ID LPAREN RPAREN'''
    # SINTÁCTICO: stdin.readLineSync()
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
    global syntax_errors, semantic_errors, scope_stack, function_table
    syntax_errors = []
    semantic_errors = []
    scope_stack = [{}]  # Reiniciar scope global
    function_table = {}  # Limpiar tabla de funciones
    
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


def analyze_semantic(filename, git_user):
    global syntax_errors, semantic_errors, scope_stack, function_table
    syntax_errors = []
    semantic_errors = []
    scope_stack = [{}]  # Reiniciar scope global
    function_table = {}  # Limpiar tabla de funciones
    
    with open(filename, 'r', encoding='utf-8') as f:
        data = f.read()
    
    from lexer import build_lexer
    lexer = build_lexer()
    parser_obj = build_parser()
    
    print(f"\n{'='*70}")
    print("  ANALIZADOR SEMÁNTICO - DART - TokenMasters")
    print(f"{'='*70}")
    print(f"Archivo: {filename}")
    print(f"Usuario: {git_user}")
    
    result = parser_obj.parse(data, lexer=lexer)
    
    # ========== SEMÁNTICA: Validaciones post-parse (null-safety, operaciones, conversiones) ==========
    # Ejecutar validaciones semánticas completas que recorren el árbol
    if result is not None:
        validate_semantic_rules(result)
    
    now = datetime.now()
    timestamp = now.strftime("%d%m%Y-%Hh%M")
    log_filename = f"logs/semantico-{git_user}-{timestamp}.txt"
    
    os.makedirs('logs', exist_ok=True)
    
    with open(log_filename, 'w', encoding='utf-8-sig') as log:
        log.write("=" * 80 + "\n")
        log.write("  ANÁLISIS SEMÁNTICO - DART\n")
        log.write("  Proyecto: TokenMasters\n")
        log.write("=" * 80 + "\n\n")
        log.write(f"Archivo: {filename}\n")
        log.write(f"Usuario: {git_user}\n")
        log.write(f"Fecha: {now.strftime('%d/%m/%Y %H:%M:%S')}\n\n")
        
        if semantic_errors:
            log.write("=" * 80 + "\n")
            log.write(f"  ERRORES SEMÁNTICOS: {len(semantic_errors)}\n")
            log.write("=" * 80 + "\n\n")
            for i, error in enumerate(semantic_errors, 1):
                log.write(f"{i}. {error}\n")
        else:
            log.write("=" * 80 + "\n")
            log.write("  ✓ ANÁLISIS EXITOSO - SIN ERRORES\n")
            log.write("=" * 80 + "\n")
    
    print(f"\nErrores semánticos: {len(semantic_errors)}")
    print(f"Log: {log_filename}")
    print(f"{'='*70}\n")

def main():
    import sys
    if len(sys.argv) >= 3:
        # Verificar qué tipo de análisis se solicita
        if len(sys.argv) >= 4:
            if sys.argv[3] == '--ambos':
                # Ejecutar ambos análisis (genera 2 logs)
                analyze_syntax(sys.argv[1], sys.argv[2])
                analyze_semantic(sys.argv[1], sys.argv[2])
            elif sys.argv[3] == '--semantico':
                # Solo semántico
                analyze_semantic(sys.argv[1], sys.argv[2])
            else:
                # Por defecto: sintáctico
                analyze_syntax(sys.argv[1], sys.argv[2])
        else:
            # Sin flag: por defecto sintáctico
            analyze_syntax(sys.argv[1], sys.argv[2])
    else:
        print("Uso:")
        print("  Sintáctico: python parser.py <archivo.dart> <usuario-git>")
        print("  Semántico:  python parser.py <archivo.dart> <usuario-git> --semantico")
        print("  Ambos:      python parser.py <archivo.dart> <usuario-git> --ambos")
        print("\nEjecutando análisis sintáctico por defecto...")
        analyze_syntax("algoritmos_prueba/algoritmo_samir.dart", "Sam-24-dev")

if __name__ == "__main__":
    main()