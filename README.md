# Analizador Léxico para Dart - TokenMasters

Proyecto de desarrollo de un analizador léxico para el lenguaje de programación Dart utilizando Python y la biblioteca PLY (Python Lex-Yacc).

## 👥 Equipo

- **Samir Caizapasto** - [@Sam-24-dev](https://github.com/Sam-24-dev)
- **Andrés Salinas** - [@ivandresalin](https://github.com/ivandresalin)
- **Mateo Mayorga** - [@bironmanusa](https://github.com/bironmanusa)

## 📋 Descripción del Proyecto

Este proyecto implementa un analizador léxico (lexer) para el lenguaje Dart, capaz de:
- Identificar y clasificar tokens del lenguaje
- Reconocer palabras reservadas, operadores y delimitadores
- Procesar literales (números, cadenas, identificadores)
- Generar logs detallados del análisis léxico
- Detectar y reportar errores léxicos

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
│   ├── algoritmo_samir.dart   # Algoritmo de Samir (comentarios, variables)
│   ├── algoritmo_andres.dart  # Algoritmo de Andrés (operadores, clases)
│   └── algoritmo_mateo.dart   # Algoritmo de Mateo (fibonacci recursivo)
├── logs/                      # Logs de análisis léxico generados (16 logs)
├── lexer.py                   # Analizador léxico principal (PLY)
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

- [x] Configuración inicial del repositorio
- [x] Estructura de carpetas
- [x] Algoritmos de prueba por integrante
- [x] Implementación del analizador léxico (lexer.py)
- [x] Pruebas con algoritmos
- [x] Generación de logs
- [x] Documentación completa

## 💻 Uso del Analizador

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

Esto generará automáticamente un archivo log en la carpeta `logs/` con el formato: `lexico-[usuario]-DD-MM-YYYY-HHhMM.txt`

## 📝 Formato de Logs

Los logs generados seguirán el formato:
```
lexico-usuario-DD-MM-YYYY-HHhMM.txt
```

Ejemplo:
```
lexico-Sam-24-dev-12-11-2025-14h30.txt
```

## 🤝 Contribuciones

### Distribución de Tareas - Análisis Léxico

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

### Logs Generados

Se generaron **16 logs** de prueba con el formato correcto:
- **Sam-24-dev:** 3 logs
- **bironmanusa:** 11 logs (múltiples pruebas)
- **ivandresalin:** 2 log

Los aportes están claramente marcados en el código con comentarios:
```python
# ============================================================
# INICIO APORTE: [usuario-git]
# Descripción del componente
# ============================================================
```

## 📅 Entrega

**Fecha límite**: 12 de noviembre de 2025, 23:55

---

**Proyecto desarrollado para la materia de Lenguajes de Programación**
