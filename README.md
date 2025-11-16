# Analizador Léxico-Sintáctico para Dart - TokenMasters

Proyecto de desarrollo de un analizador léxico y sintáctico para el lenguaje de programación Dart utilizando Python y la biblioteca PLY (Python Lex-Yacc).

## 👥 Equipo

- **Samir Caizapasto** - [@Sam-24-dev](https://github.com/Sam-24-dev)
- **Andrés Salinas** - [@ivandresalin](https://github.com/ivandresalin)
- **Mateo Mayorga** - [@bironmanusa](https://github.com/bironmanusa)

## 📋 Descripción del Proyecto

Este proyecto implementa un compilador completo para Dart en dos fases:

### Avance 1: Analizador Léxico ✅ COMPLETADO
- Identificar y clasificar tokens del lenguaje
- Reconocer palabras reservadas, operadores y delimitadores
- Procesar literales (números, cadenas, identificadores)
- Generar logs detallados del análisis léxico
- Detectar y reportar errores léxicos

### Avance 2: Analizador Sintáctico ✅ COMPLETADO
- Validar la estructura gramatical del código Dart
- Reconocer declaraciones de funciones, variables y clases
- Procesar estructuras de control (if, while, for)
- Analizar expresiones aritméticas y lógicas
- Generar logs de análisis sintáctico
- Detectar y reportar errores sintácticos

## �️ Tecnologías

- **Lenguaje**: Python 3.7+
- **Biblioteca**: PLY (Python Lex-Yacc)

## 📦 Instalación

1. Clonar el repositorio:
```bash
git clone https://github.com/Sam-24-dev/analizador-dart-tokenMasters.git
cd analizador-dart-tokenMasters
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## 📁 Estructura del Proyecto

```
analizador-dart-tokenMasters/
├── algoritmos_prueba/         # Algoritmos de prueba en Dart de cada integrante
│   ├── algoritmo_samir.dart   # Algoritmo de Samir (funciones, print, input)
│   ├── algoritmo_andres.dart  # Algoritmo de Andrés (Estructuras de control)
│   └── algoritmo_mateo.dart   # Algoritmo de Mateo (fibonacci recursivo)
├── logs/                      # Logs de análisis léxico y sintáctico
│   ├── lexico-*.txt          # 16 logs de análisis léxico
│   └── sintactico-*.txt      # 10 logs de análisis sintáctico
├── lexer.py                   # Analizador léxico (PLY) - Avance 1 ✅
├── parser.py                  # Analizador sintáctico (PLY) - Avance 2 ✅
├── .gitignore                 # Archivos ignorados por Git
├── requirements.txt           # Dependencias (PLY 3.11)
└── README.md                  # Documentación del proyecto
```

## 🔧 Componentes del Analizador

### Tokens Implementados

**Palabras Reservadas (60+):** 
- Control de flujo: `if`, `else`, `for`, `while`, `do`, `switch`, `case`, `break`, `continue`, `return`
- Declaraciones: `var`, `final`, `const`, `void`, `class`, `enum`, `typedef`
- Tipos: `dynamic`, `int`, `double`, `String`, `bool`
- Asíncronos: `async`, `await`, `sync`, `yield`
- Otros: `import`, `export`, `library`, `abstract`, `static`, `extends`, `implements`, etc.

**Operadores:**
- Aritméticos: `+`, `-`, `*`, `/`, `%`, `~/`
- Comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Lógicos: `&&`, `||`, `!`
- Asignación: `=`, `+=`, `-=`, `*=`, `/=`, `%=`
- Incremento/Decremento: `++`, `--`
- Bitwise: `&`, `|`, `^`, `~`, `<<`, `>>`, `>>>`
- Especiales: `??`, `?.`, `..`, `?..`, `...`, `...?`, `=>`

**Delimitadores:** `(`, `)`, `{`, `}`, `[`, `]`, `;`, `,`, `.`, `:`

**Literales:**
- Números: enteros y decimales
- Strings: comillas simples y dobles
- Identificadores: variables, funciones, clases

**Otros:**
- Comentarios: `//` y `/* */`
- Espacios y saltos de línea
- Detección de errores léxicos

## 🚀 Estado del Proyecto

### Avance 1: Analizador Léxico ✅ COMPLETADO
- [x] Configuración inicial del repositorio
- [x] Estructura de carpetas
- [x] Algoritmos de prueba por integrante
- [x] Implementación del analizador léxico (lexer.py)
- [x] Pruebas con algoritmos
- [x] Generación de 16 logs
- [x] Documentación completa
- [x] **Entregado: 12 de noviembre de 2025**

### Avance 2: Analizador Sintáctico ✅ COMPLETADO
- [x] Creación de parser.py con PLY yacc
- [x] Implementación de funciones (Samir) ✅
- [x] Implementación de print statements (Samir) ✅
- [x] Implementación de input (Samir) ✅
- [x] Estructuras de control - if, while, for (Andrés)✅
- [x] Variables, expresiones, listas, mapas (Mateo)✅
- [x] Clases y objetos (Mateo)✅
- [x] Generación de logs sintácticos✅
- [x] **Entrega: 15 de noviembre de 2025, 23:59**✅

## 💻 Uso de los Analizadores

### Analizador Léxico (Avance 1)

Para ejecutar el analizador léxico:

```bash
python lexer.py algoritmos_prueba/[archivo.dart] [usuario-git]
```

**Ejemplos:**
```bash
python lexer.py algoritmos_prueba/algoritmo_samir.dart Sam-24-dev
python lexer.py algoritmos_prueba/algoritmo_andres.dart ivandresalin
python lexer.py algoritmos_prueba/algoritmo_mateo.dart bironmanusa
```

Genera logs con formato: `lexico-[usuario]-DD-MM-YYYY-HHhMM.txt`

### Analizador Sintáctico (Avance 2)

Para ejecutar el analizador sintáctico:

```bash
python parser.py algoritmos_prueba/[archivo.dart] [usuario-git]
```

**Ejemplos:**
```bash
python parser.py algoritmos_prueba/algoritmo_samir.dart Sam-24-dev
python parser.py algoritmos_prueba/algoritmo_andres.dart ivandresalin
python parser.py algoritmos_prueba/algoritmo_mateo.dart bironmanusa
```

Genera logs con formato: `sintactico-[usuario]-DD-MM-YYYY-HHhMM.txt`

## 📝 Formato de Logs

### Logs Léxicos
Formato: `lexico-usuario-DD-MM-YYYY-HHhMM.txt`

Ejemplo: `lexico-Sam-24-dev-12-11-2025-14h30.txt`

### Logs Sintácticos
Formato: `sintactico-usuario-DD-MM-YYYY-HHhMM.txt`

Ejemplo: `sintactico-Sam-24-dev-15-11-2025-01h30.txt`

## 🤝 Contribuciones

### Avance 1: Análisis Léxico ✅

**Samir Caizapasto (Sam-24-dev):**
- Manejo de comentarios de línea (`//`) y multilínea (`/* */`)
- Ignorar espacios en blanco y tabulaciones
- Contador de líneas para reportar errores
- Detección de errores léxicos con ubicación (línea y columna)
- Funciones principales: `analyze_file()`, `main()`, `build_lexer()`

**Andrés Salinas (ivandresalin):**
- 60+ palabras reservadas de Dart
- Todos los operadores (aritméticos, lógicos, comparación, bitwise, especiales)
- Todos los delimitadores
- Algoritmo de prueba complejo con clases, operadores avanzados

**Mateo Mayorga (bironmanusa):**
- Reconocimiento de números (enteros y decimales)
- Reconocimiento de strings (comillas simples y dobles)
- Reconocimiento de identificadores con validación de palabras reservadas
- Algoritmo de prueba con recursividad (Fibonacci)

### Avance 2: Análisis Sintáctico ✅

**Samir Caizapasto (Sam-24-dev):** ✅ COMPLETADO
- Declaración de funciones con tipo de retorno y parámetros
- Funciones void con/sin parámetros
- Arrow functions (`=>`)
- Return statements (con/sin valor)
- Print statements
- Input statements (`stdin.readLineSync()`)
- Algoritmo de prueba con múltiples tipos de funciones

**Andrés Salinas (ivandresalin):** ✅ COMPLETADO
- Estructuras de control: if-else, while, for, do-while
- Algoritmo de prueba con estructuras de control

**Mateo Mayorga (bironmanusa):** ✅ COMPLETADO
- Declaración de variables (var, final, const)
- Expresiones aritméticas y lógicas
- Estructuras de datos: listas y mapas
- Clases básicas
- Algoritmo de prueba con estructuras de datos

### Logs Generados

**Avance 1 - Análisis Léxico:**
- **Total:** 16 logs
- **Sam-24-dev:** 3 logs
- **bironmanusa:** 11 logs (múltiples pruebas)
- **ivandresalin:** 2 logs

**Avance 2 - Análisis Sintáctico:**
- **Sam-24-dev:** Logs generados exitosamente ✅
- **ivandresalin:** Logs generados exitosamente ✅
- **bironmanusa:** Logs generados exitosamente ✅

Los aportes están claramente marcados en el código con comentarios:
```python
# ============================================================
# INICIO APORTE: [usuario-git]
# Descripción del componente
# ============================================================
```

## 📊 Reglas Sintácticas Implementadas

### Funciones (Samir) ✅
- `tipo ID (parametros) { cuerpo }`
- `void ID (parametros) { cuerpo }`  
- `tipo ID (parametros) => expresion;` (arrow functions)
- `return expresion;`
- `return;`

### Print e Input (Samir) ✅
- `print(expresion);`
- `stdin.readLineSync()`

### Variables y Expresiones (Mateo) ✅
- Declaraciones: `var`, `final`, `const`
- Expresiones aritméticas: `+`, `-`, `*`, `/`, `%`
- Listas y mapas

### Estructuras de Control (Andrés) ✅
- `if-else`
- `while`
- `for`

## 📅 Entregas

**Avance 1 - Analizador Léxico:**
- Fecha límite: 12 de noviembre de 2025, 23:55
- Estado: ✅ ENTREGADO

**Avance 2 - Analizador Sintáctico:**
- Fecha límite: 15 de noviembre de 2025, 23:59
- Estado: ✅ ENTREGADO

---

**Proyecto desarrollado para la materia de Lenguajes de Programación**
