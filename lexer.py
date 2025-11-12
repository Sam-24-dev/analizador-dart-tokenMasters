"""
Analizador Léxico para Dart - Proyecto TokenMasters
Integrantes:
- Andrés Salinas (ivandresalin) - Palabras reservadas, operadores, delimitadores
- Mateo Mayorga (bironmanusa) - Tokens de tipos de datos, literales, identificadores
- Samir Caizapasto (Sam-24-dev) - Comentarios, espacios, errores léxicos, contador de líneas
"""

import ply.lex as lex
from datetime import datetime
import os
import sys

# ============================================================================
# SECCIÓN PARA ANDRÉS SALINAS (ivandresalin)
# TODO: Agregar aquí las palabras reservadas de Dart
# ============================================================================

# Palabras reservadas de Dart (PENDIENTE - ivandresalin)
# Ejemplo de estructura que debe seguir Andrés:
# reserved = {
#     'if': 'IF',
#     'else': 'ELSE',
#     'for': 'FOR',
#     'while': 'WHILE',
#     'var': 'VAR',
#     'const': 'CONST',
#     'final': 'FINAL',
#     'void': 'VOID',
#     'return': 'RETURN',
#     'class': 'CLASS',
#     'int': 'INT',
#     'double': 'DOUBLE',
#     'String': 'STRING_TYPE',
#     'bool': 'BOOL',
#     'true': 'TRUE',
#     'false': 'FALSE',
#     'null': 'NULL',
#     'print': 'PRINT',
#     'import': 'IMPORT',
#     'as': 'AS',
#     'break': 'BREAK',
#     'continue': 'CONTINUE',
#     # ... agregar todas las palabras reservadas de Dart
# }

reserved = {}  # Andrés llenará esto

# ============================================================================
# SECCIÓN PARA ANDRÉS SALINAS (ivandresalin)
# TODO: Agregar aquí los tokens de operadores y delimitadores
# ============================================================================

# Lista de tokens (PENDIENTE - ivandresalin y bironmanusa completarán)
# Andrés debe agregar: operadores aritméticos (+, -, *, /, %), 
#                      operadores de comparación (==, !=, <, >, <=, >=),
#                      operadores lógicos (&&, ||, !),
#                      delimitadores (, ), {, }, [, ], ;, ,, ., :, =>
# Mateo debe agregar: NUMBER, STRING, ID (identificadores)

tokens = [
    # Tokens de Andrés (ivandresalin) - PENDIENTE
    # 'PLUS',           # +
    # 'MINUS',          # -
    # 'TIMES',          # *
    # 'DIVIDE',         # /
    # 'MODULO',         # %
    # 'EQUALS',         # ==
    # 'NOTEQUAL',       # !=
    # 'LESSTHAN',       # <
    # 'GREATERTHAN',    # >
    # 'LESSEQUAL',      # <=
    # 'GREATEREQUAL',   # >=
    # 'AND',            # &&
    # 'OR',             # ||
    # 'NOT',            # !
    # 'ASSIGN',         # =
    # 'LPAREN',         # (
    # 'RPAREN',         # )
    # 'LBRACE',         # {
    # 'RBRACE',         # }
    # 'LBRACKET',       # [
    # 'RBRACKET',       # ]
    # 'SEMICOLON',      # ;
    # 'COMMA',          # ,
    # 'DOT',            # .
    # 'COLON',          # :
    # 'ARROW',          # =>
    
    # Tokens de Mateo (bironmanusa) - PENDIENTE
    # 'NUMBER',         # Números enteros y decimales
    # 'STRING',         # Cadenas de texto
    # 'ID',             # Identificadores
    
    # Token temporal para que el lexer funcione (Samir)
    # Tus compañeros reemplazarán esto con sus tokens reales
    'DUMMY',  # Token temporal - ELIMINAR cuando se agreguen los tokens reales
] + list(reserved.values())


# ============================================================================
# SECCIÓN PARA ANDRÉS SALINAS (ivandresalin)
# TODO: Agregar aquí las reglas de tokens para operadores y delimitadores
# ============================================================================

# Andrés debe agregar reglas simples como:
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_MODULO = r'%'
# t_EQUALS = r'=='
# t_NOTEQUAL = r'!='
# t_LESSTHAN = r'<'
# t_LESSEQUAL = r'<='
# t_GREATERTHAN = r'>'
# t_GREATEREQUAL = r'>='
# t_AND = r'&&'
# t_OR = r'\|\|'
# t_NOT = r'!'
# t_ASSIGN = r'='
# t_LPAREN = r'\('
# t_RPAREN = r'\)'
# t_LBRACE = r'\{'
# t_RBRACE = r'\}'
# t_LBRACKET = r'\['
# t_RBRACKET = r'\]'
# t_SEMICOLON = r';'
# t_COMMA = r','
# t_DOT = r'\.'
# t_COLON = r':'
# t_ARROW = r'=>'

# Regla temporal para que el lexer funcione (Samir)
# Tus compañeros eliminarán esto cuando agreguen sus tokens
t_DUMMY = r'[a-zA-Z0-9_{}();\[\]=+\-*/<>!,.:"]+'  # Reconoce cualquier cosa temporalmente


# ============================================================================
# SECCIÓN PARA MATEO MAYORGA (bironmanusa)
# TODO: Agregar aquí las reglas para números, strings e identificadores
# ============================================================================

# Mateo debe agregar funciones como:
# def t_NUMBER(t):
#     r'\d+(\.\d+)?'
#     t.value = float(t.value) if '.' in t.value else int(t.value)
#     return t
#
# def t_STRING(t):
#     r'\"([^\\\n]|(\\.))*?\"'
#     t.value = t.value[1:-1]  # Remover comillas
#     return t
#
# def t_ID(t):
#     r'[a-zA-Z_][a-zA-Z_0-9]*'
#     t.type = reserved.get(t.value, 'ID')  # Verificar si es palabra reservada
#     return t


# ============================================================================
# INICIO APORTE: Samir Caizapasto (Sam-24-dev)
# Responsable: Comentarios, Espacios, Errores Léxicos, Contador de Líneas
# ============================================================================

# Ignorar espacios y tabulaciones
t_ignore = ' \t'

# Comentarios de una sola línea //
def t_COMMENT(t):
    r'//.*'
    pass  # Los comentarios se ignoran, no se retornan como tokens

# Comentarios multilínea /* */
def t_MULTILINE_COMMENT(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')  # Contar saltos de línea dentro del comentario
    pass  # Los comentarios se ignoran, no se retornan como tokens

# Saltos de línea (para contar el número de línea)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  # Incrementar contador de líneas

# Manejo de errores léxicos (caracteres no reconocidos)
def t_error(t):
    print(f" ERROR LÉXICO: Carácter ilegal '{t.value[0]}' en la línea {t.lexer.lineno}, columna {find_column(t)}")
    t.lexer.skip(1)  # Saltar el carácter inválido y continuar

# Función auxiliar para encontrar la columna de un token
def find_column(token):
    """Calcula la columna de un token en el código fuente"""
    line_start = token.lexer.lexdata.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

# ============================================================================
# FIN APORTE: Samir Caizapasto (Sam-24-dev)
# ============================================================================


# ============================================================================
# CONSTRUCCIÓN DEL LEXER Y FUNCIONES PRINCIPALES
# ============================================================================

def build_lexer():
    """Construye y retorna el analizador léxico"""
    return lex.lex()

def analyze_file(filename, git_user):
    """
    Analiza un archivo Dart y genera un log detallado con los tokens encontrados
    
    Args:
        filename: Ruta del archivo .dart a analizar
        git_user: Usuario de GitHub para nombrar el log
    """
    # Verificar que el archivo existe
    if not os.path.exists(filename):
        print(f" Error: El archivo '{filename}' no existe")
        return
    
    # Leer el contenido del archivo
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
    except Exception as e:
        print(f" Error al leer el archivo: {e}")
        return
    
    # Construir el lexer
    lexer = build_lexer()
    
    # Obtener fecha y hora actual
    now = datetime.now()
    timestamp = now.strftime("%d-%m-%Y-%Hh%M")
    
    # Crear nombre del archivo log
    log_filename = f"logs/lexico-{git_user}-{timestamp}.txt"
    
    # Asegurar que la carpeta logs existe
    os.makedirs('logs', exist_ok=True)
    
    # Tokenizar el código
    lexer.input(data)
    
    # Listas para almacenar tokens y errores
    tokens_list = []
    errors_list = []
    
    # Capturar errores léxicos
    lexer.skip = lambda n: errors_list.append(f"Línea {lexer.lineno}")
    
    print(f"\n{'='*70}")
    print(f"  ANALIZADOR LÉXICO PARA DART - TokenMasters")
    print(f"{'='*70}")
    print(f" Archivo analizado: {filename}")
    print(f" Usuario: {git_user}")
    print(f" Fecha: {now.strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"{'='*70}\n")
    
    # Procesar todos los tokens
    token_count = 0
    for tok in lexer:
        token_count += 1
        tokens_list.append({
            'num': token_count,
            'type': tok.type,
            'value': tok.value,
            'line': tok.lineno
        })
        print(f"Token #{token_count:3d} | {tok.type:20s} | Línea {tok.lineno:3d} | Valor: {tok.value}")
    
    # Escribir el log en archivo
    with open(log_filename, 'w', encoding='utf-8') as log_file:
        log_file.write("=" * 80 + "\n")
        log_file.write("  ANÁLISIS LÉXICO - DART\n")
        log_file.write("  Proyecto: TokenMasters\n")
        log_file.write("=" * 80 + "\n\n")
        log_file.write(f" Archivo analizado: {filename}\n")
        log_file.write(f" Usuario Git: {git_user}\n")
        log_file.write(f" Fecha y hora: {now.strftime('%d/%m/%Y %H:%M:%S')}\n")
        log_file.write("\n" + "=" * 80 + "\n")
        log_file.write("  TOKENS RECONOCIDOS\n")
        log_file.write("=" * 80 + "\n\n")
        log_file.write(f"{'#':<6} | {'TIPO':<20} | {'LÍNEA':<6} | {'VALOR'}\n")
        log_file.write("-" * 80 + "\n")
        
        for token in tokens_list:
            log_file.write(f"{token['num']:<6} | {token['type']:<20} | {token['line']:<6} | {token['value']}\n")
        
        log_file.write("\n" + "=" * 80 + "\n")
        log_file.write("  ESTADÍSTICAS\n")
        log_file.write("=" * 80 + "\n\n")
        log_file.write(f" Total de tokens reconocidos: {token_count}\n")
        log_file.write(f" Total de errores léxicos: {len(errors_list)}\n")
        
        if errors_list:
            log_file.write("\n" + "=" * 80 + "\n")
            log_file.write("  ERRORES ENCONTRADOS\n")
            log_file.write("=" * 80 + "\n\n")
            for error in errors_list:
                log_file.write(f" {error}\n")
        
        log_file.write("\n" + "=" * 80 + "\n")
        log_file.write(f"  Análisis realizado por: {git_user}\n")
        log_file.write("  Analizador Léxico para Dart - TokenMasters\n")
        log_file.write("=" * 80 + "\n")
    
    print(f"\n{'='*70}")
    print(f" ANÁLISIS COMPLETADO")
    print(f"{'='*70}")
    print(f" Total de tokens reconocidos: {token_count}")
    print(f" Total de errores léxicos: {len(errors_list)}")
    print(f" Log guardado en: {log_filename}")
    print(f"{'='*70}\n")


def main():
    """Función principal del analizador léxico"""
    print("\n" + "="*70)
    print("  ANALIZADOR LÉXICO PARA DART - TokenMasters")
    print("  Desarrollado por: Sam-24-dev (Samir Caizapasto)")
    print("="*70 + "\n")
    
    # Si se ejecuta con argumentos desde terminal
    if len(sys.argv) >= 3:
        filename = sys.argv[1]
        git_user = sys.argv[2]
        analyze_file(filename, git_user)
    # Si se ejecuta directamente, usar valores por defecto
    else:
        print(" Modo de uso desde terminal:")
        print("   python lexer.py <archivo.dart> <usuario_git>")
        print("   Ejemplo: python lexer.py algoritmos_prueba/algoritmo_samir.dart Sam-24-dev\n")
        
        # Analizar el archivo de Samir por defecto
        default_file = "algoritmos_prueba/algoritmo_samir.dart"
        default_user = "Sam-24-dev"
        
        print(f" Ejecutando análisis con valores por defecto...")
        print(f"   Archivo: {default_file}")
        print(f"   Usuario: {default_user}\n")
        
        analyze_file(default_file, default_user)


if __name__ == "__main__":
    main()
