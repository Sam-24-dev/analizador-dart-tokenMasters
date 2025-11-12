# INSTRUCCIONES PARA LOS COMPAÑEROS - TokenMasters

## 📌 Estado Actual del Proyecto

### ✅ YA IMPLEMENTADO (Samir Caizapasto - Sam-24-dev)

- ✅ Estructura base del proyecto
- ✅ Manejo de comentarios de una línea `//`
- ✅ Manejo de comentarios multilínea `/* */`
- ✅ Ignorar espacios y tabs
- ✅ Contador de líneas
- ✅ Detección de errores léxicos
- ✅ Generación de logs automática
- ✅ Función principal `main()` y `analyze_file()`

---

## 🔴 PENDIENTE - Andrés Salinas (ivandresalin)

### Tu responsabilidad: Palabras Reservadas, Operadores y Delimitadores

#### 📍 UBICACIÓN EN `lexer.py`: Líneas 14-121

### 1️⃣ Agregar Palabras Reservadas (línea ~14)

Reemplaza esto:
```python
reserved = {}  # Andrés llenará esto
```

Por esto:
```python
reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'for': 'FOR',
    'while': 'WHILE',
    'do': 'DO',
    'var': 'VAR',
    'const': 'CONST',
    'final': 'FINAL',
    'void': 'VOID',
    'return': 'RETURN',
    'class': 'CLASS',
    'int': 'INT',
    'double': 'DOUBLE',
    'String': 'STRING_TYPE',
    'bool': 'BOOL',
    'true': 'TRUE',
    'false': 'FALSE',
    'null': 'NULL',
    'print': 'PRINT',
    'import': 'IMPORT',
    'as': 'AS',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'extends': 'EXTENDS',
    'implements': 'IMPLEMENTS',
    'new': 'NEW',
    'this': 'THIS',
    'super': 'SUPER',
    'static': 'STATIC',
    'async': 'ASYNC',
    'await': 'AWAIT',
}
```

### 2️⃣ Agregar Tokens (línea ~41)

Descomenta y completa esta sección:
```python
tokens = [
    # Tus tokens Andrés:
    'PLUS',           # +
    'MINUS',          # -
    'TIMES',          # *
    'DIVIDE',         # /
    'MODULO',         # %
    'EQUALS',         # ==
    'NOTEQUAL',       # !=
    'LESSTHAN',       # <
    'GREATERTHAN',    # >
    'LESSEQUAL',      # <=
    'GREATEREQUAL',   # >=
    'AND',            # &&
    'OR',             # ||
    'NOT',            # !
    'ASSIGN',         # =
    'LPAREN',         # (
    'RPAREN',         # )
    'LBRACE',         # {
    'RBRACE',         # }
    'LBRACKET',       # [
    'RBRACKET',       # ]
    'SEMICOLON',      # ;
    'COMMA',          # ,
    'DOT',            # .
    'COLON',          # :
    'ARROW',          # =>
    'PLUSPLUS',       # ++
    'MINUSMINUS',     # --
    
    # Tokens de Mateo (bironmanusa) - PENDIENTE
    # 'NUMBER',
    # 'STRING',
    # 'ID',
    
    # ELIMINAR ESTE TOKEN DUMMY cuando agregues los tuyos:
    # 'DUMMY',
] + list(reserved.values())
```

### 3️⃣ Agregar Reglas de Tokens (línea ~106)

Descomenta y completa:
```python
# ============================================================================
# INICIO APORTE: Andrés Salinas (ivandresalin)
# Responsable: Operadores y Delimitadores
# ============================================================================

# Operadores aritméticos
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_MODULO = r'%'

# Operadores de comparación (orden importante: == antes que =)
t_EQUALS = r'=='
t_NOTEQUAL = r'!='
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_LESSTHAN = r'<'
t_GREATERTHAN = r'>'

# Operadores lógicos
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

# Operadores de asignación e incremento
t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'--'
t_ASSIGN = r'='

# Delimitadores
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_SEMICOLON = r';'
t_COMMA = r','
t_DOT = r'\.'
t_COLON = r':'
t_ARROW = r'=>'

# ============================================================================
# FIN APORTE: Andrés Salinas (ivandresalin)
# ============================================================================
```

### 4️⃣ ELIMINAR el token DUMMY

En la línea ~130, elimina:
```python
t_DUMMY = r'[a-zA-Z0-9_{}();\[\]=+\-*/<>!,.:"]+'  # ELIMINAR ESTO
```

---

## 🔴 PENDIENTE - Mateo Mayorga (bironmanusa)

### Tu responsabilidad: Números, Strings e Identificadores

#### 📍 UBICACIÓN EN `lexer.py`: Líneas 135-160

### 1️⃣ Agregar tus tokens a la lista (línea ~70)

Descomenta en la sección de tokens:
```python
# Tokens de Mateo:
'NUMBER',         # Números enteros y decimales
'STRING',         # Cadenas de texto
'ID',             # Identificadores
```

### 2️⃣ Agregar Reglas de Tokens (línea ~135)

Agrega esto:
```python
# ============================================================================
# INICIO APORTE: Mateo Mayorga (bironmanusa)
# Responsable: Literales (números, strings, identificadores)
# ============================================================================

def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    t.value = t.value[1:-1]  # Remover comillas
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # Verificar si es palabra reservada
    return t

# ============================================================================
# FIN APORTE: Mateo Mayorga (bironmanusa)
# ============================================================================
```

---

## 🧪 CÓMO PROBAR TU PARTE

### 1. Ejecuta el analizador:
```bash
python lexer.py algoritmos_prueba/algoritmo_[tu_nombre].dart [tu_usuario_git]
```

Ejemplos:
```bash
python lexer.py algoritmos_prueba/algoritmo_andres.dart ivandresalin
python lexer.py algoritmos_prueba/algoritmo_mateo.dart bironmanusa
```

### 2. Verifica que se genere el log en `logs/`

### 3. Haz commit de tus cambios:
```bash
git add lexer.py
git commit -m "feat: Agregar tokens de [tu parte] - [tu nombre]"
git push origin main
```

---

## 📋 CHECKLIST FINAL

Cada uno debe verificar que su log contenga:
- ✅ Su usuario Git en el nombre del archivo
- ✅ Fecha y hora correctas
- ✅ Tokens reconocidos correctamente
- ✅ Sin errores léxicos en código válido
- ✅ El commit aparece en GitHub con su usuario

---

## ⚠️ IMPORTANTE

- **NO borren el código de los demás**
- **Respeten las secciones marcadas con comentarios**
- **Cada uno trabaja en SU sección**
- **Prueben antes de hacer commit**

---

**Cualquier duda, consulten en el grupo** 💬
