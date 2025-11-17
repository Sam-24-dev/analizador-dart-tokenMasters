# Analizador Léxico-Sintáctico-Semántico para Dart - TokenMasters

Proyecto de desarrollo de un compilador completo para el lenguaje de programación Dart utilizando Python y la biblioteca PLY (Python Lex-Yacc). Implementa análisis léxico, sintáctico y semántico.

## 👥 Equipo

- **Samir Caizapasto** - [@Sam-24-dev](https://github.com/Sam-24-dev)
- **Andrés Salinas** - [@ivandresalin](https://github.com/ivandresalin)
- **Mateo Mayorga** - [@bironmanusa](https://github.com/bironmanusa)

## 📋 Descripción del Proyecto

Este proyecto implementa un compilador completo para Dart en tres fases:

### Avance 1: Analizador Léxico ✅ COMPLETADO
- Identificar y clasificar tokens del lenguaje
- Reconocer palabras reservadas, operadores y delimitadores
- Procesar literales (números, cadenas, identificadores)
- Generar logs detallados del análisis léxico
- Detectar y reportar errores léxicos
- **Entregado: 12 de noviembre de 2025**

### Avance 2: Analizador Sintáctico ✅ COMPLETADO
- Validar la estructura gramatical del código Dart
- Reconocer declaraciones de funciones, variables y clases
- Procesar estructuras de control (if, while, for)
- Analizar expresiones aritméticas y lógicas
- Generar logs de análisis sintáctico
- Detectar y reportar errores sintácticos
- **Entregado: 15 de noviembre de 2025**

### Avance 3: Analizador Semántico 🔄 EN PROCESO
**Implementado (Samir):**
- ✅ **Regla 1:** Retorno de funciones
  - Funciones con tipo de retorno deben retornar en todos los caminos
  - Validación de existencia de `return`
  - Generación de errores con número de línea
- ✅ **Regla 2:** Estructuras de control (break/continue)
  - `break` y `continue` solo permitidos dentro de bucles
  - Validación post-parsing del árbol sintáctico
  - Reporte de errores con línea exacta

**Pendiente:**
- ⏳ **Andrés:** Reglas de Identificadores (Existencia y Alcance)
- ⏳ **Mateo:** Reglas de Operaciones Permitidas (Null Safety, Compatibilidad)
- ⏳ **Mateo:** Reglas de Conversión (Casting, Conversión Numérica)

**Entrega parcial (Samir):** 17 de noviembre de 2025

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
│   ├── algoritmo_andres.dart  # Algoritmo de Andrés (estructuras de control)
│   └── algoritmo_mateo.dart   # Algoritmo de Mateo (fibonacci recursivo)
├── logs/                      # Logs de análisis léxico, sintáctico y semántico
│   ├── lexico-*.txt          # 17 logs de análisis léxico
│   ├── sintactico-*.txt      # 13 logs de análisis sintáctico
│   └── semantico-*.txt       # 11 logs de análisis semántico
├── lexer.py                   # Analizador léxico (PLY) - Avance 1 ✅
├── parser.py                  # Analizador sintáctico y semántico (PLY) - Avances 2 y 3 ✅
├── parsetab.py                # Tabla de parsing generada por PLY
├── __pycache__/               # Archivos compilados de Python
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
- [x] Generación de 17 logs
- [x] Documentación completa
- [x] **Entregado: 12 de noviembre de 2025**

### Avance 2: Analizador Sintáctico ✅ COMPLETADO
- [x] Creación de parser.py con PLY yacc
- [x] Implementación de funciones (Samir) ✅
- [x] Implementación de print statements (Samir) ✅
- [x] Implementación de input (Samir) ✅
- [x] Estructuras de control - if, while, for (Andrés) ✅
- [x] Variables, expresiones, listas, mapas (Mateo) ✅
- [x] Clases y objetos (Mateo) ✅
- [x] Generación de 13 logs sintácticos ✅
- [x] **Entregado: 15 de noviembre de 2025**

### Avance 3: Analizador Semántico 🔄 EN PROCESO
**Implementado (Samir):**
- [x] Tablas semánticas (symbol_table, function_table, semantic_errors) ✅
- [x] **Regla 1:** Validación de retornos en funciones ✅
  - [x] Funciones con tipo de retorno deben tener `return`
  - [x] Validación en todos los caminos de ejecución
  - [x] Funciones helper: `has_return_in_all_paths()`, `validate_return_type()`
- [x] **Regla 2:** Validación de break/continue ✅
  - [x] `break` solo dentro de loops
  - [x] `continue` solo dentro de loops
  - [x] Validación post-parsing del árbol sintáctico
  - [x] Función helper: `validate_break_continue()`
- [x] Generación de 11 logs semánticos ✅
- [x] Reportar errores con número de línea ✅
- [x] Opción `--semantico` y `--ambos` ✅
- [x] Encoding UTF-8-sig para tildes ✅

**Pendiente (Otros integrantes):**
- [ ] **Andrés:** Reglas de Identificadores (Existencia y Alcance)
- [ ] **Mateo:** Reglas de Operaciones Permitidas (Null Safety, Compatibilidad)
- [ ] **Mateo:** Reglas de Conversión (Casting, Conversión Numérica)

**Entrega parcial (Samir):** 17 de noviembre de 2025
  - [x] `continue` solo dentro de loops
  - [x] Validación post-parsing del árbol sintáctico
- [x] Generación de 11 logs semánticos ✅
- [x] Reportar errores con número de línea ✅
- [x] Opción `--semantico` y `--ambos` ✅
- [x] **Entregado: 17 de noviembre de 2025**

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

---

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

---

### Analizador Semántico (Avance 3)

Para ejecutar el analizador semántico:

```bash
python parser.py algoritmos_prueba/[archivo.dart] [usuario-git] --semantico
```

**Ejemplos:**
```bash
python parser.py algoritmos_prueba/algoritmo_samir.dart Sam-24-dev --semantico
```

Genera logs con formato: `semantico-[usuario]-DDMMYYYY-HHhMM.txt`

---

### Análisis Completo (Sintáctico + Semántico)

Para ejecutar ambos análisis:

```bash
python parser.py algoritmos_prueba/[archivo.dart] [usuario-git] --ambos
```

**Ejemplo:**
```bash
python parser.py algoritmos_prueba/algoritmo_samir.dart Sam-24-dev --ambos
```

Genera 2 logs: uno sintáctico y uno semántico

---

### Opciones de Ejecución

| Comando | Descripción | Log Generado |
|---------|-------------|--------------|
| `python parser.py <archivo> <usuario>` | Análisis sintáctico (por defecto) | `sintactico-*.txt` |
| `python parser.py <archivo> <usuario> --semantico` | Solo análisis semántico | `semantico-*.txt` |
| `python parser.py <archivo> <usuario> --ambos` | Sintáctico + Semántico | Ambos logs |

## 📝 Formato de Logs

### Logs Léxicos
**Formato:** `lexico-usuario-DD-MM-YYYY-HHhMM.txt`

**Ejemplo:** `lexico-Sam-24-dev-12-11-2025-14h30.txt`

**Contenido:**
- Lista de todos los tokens reconocidos
- Tipo de token, número de línea y valor
- Total de tokens reconocidos
- Errores léxicos detectados

---

### Logs Sintácticos
**Formato:** `sintactico-usuario-DD-MM-YYYY-HHhMM.txt`

**Ejemplo:** `sintactico-Sam-24-dev-15-11-2025-01h30.txt`

**Contenido:**
- Resultado del análisis sintáctico
- Errores sintácticos con línea y tipo de token
- Estado: Éxito o errores encontrados

---

### Logs Semánticos
**Formato:** `semantico-usuario-DDMMYYYY-HHhMM.txt`

**Ejemplo:** `semantico-Sam-24-dev-17112025-15h03.txt`

**Contenido:**
- Errores semánticos detectados con número de línea
- Validaciones aplicadas:
  - Funciones sin `return` en todos los caminos
  - `break` o `continue` fuera de bucles
- Estado: Éxito o errores encontrados

**Salida en PowerShell:**
- Muestra cantidad de errores
- Lista detallada de cada error con su línea
- Ruta del log generado

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
- Break y continue statements
- Algoritmo de prueba con estructuras de control

**Mateo Mayorga (bironmanusa):** ✅ COMPLETADO
- Declaración de variables (var, final, const)
- Expresiones aritméticas y lógicas
- Estructuras de datos: listas y mapas
- Clases básicas
- Algoritmo de prueba con estructuras de datos

---

### Avance 3: Análisis Semántico 🔄 EN PROCESO

**Samir Caizapasto (Sam-24-dev):** ✅ IMPLEMENTADO (Parcial)
- **Regla 1: Retorno de funciones**
  - Validación de que funciones con tipo de retorno tengan `return`
  - Verificación de `return` en todos los caminos de ejecución
  - Funciones helper: `has_return_in_all_paths()`, `validate_return_type()`
- **Regla 2: Break/Continue en loops**
  - Validación de `break` solo dentro de bucles
  - Validación de `continue` solo dentro de bucles
  - Función helper: `validate_break_continue()` (post-parsing)
- Tablas semánticas: `symbol_table`, `function_table`, `semantic_errors`
- Sistema de logs semánticos con encoding UTF-8-sig
- Opción `--semantico` y `--ambos` en parser.py
- Reporte de errores con número de línea en PowerShell y logs

**Andrés Salinas (ivandresalin):** ⏳ PENDIENTE
- Reglas de Identificadores (Existencia y Alcance)
- TODOs dejados en código para implementación futura

**Mateo Mayorga (bironmanusa):** ⏳ PENDIENTE
- Reglas de Operaciones Permitidas (Null Safety, Compatibilidad Aritmética)
- Reglas de Conversión (Casting Explícito, Conversión Numérica)
- TODOs dejados en código para implementación futura

### Logs Generados

**Avance 1 - Análisis Léxico:**
- **Total:** 17 logs
- **Sam-24-dev:** 3 logs
- **bironmanusa:** 11 logs (múltiples pruebas)
- **ivandresalin:** 2 logs

**Avance 2 - Análisis Sintáctico:**
- **Total:** 13 logs
- **Sam-24-dev:** Logs generados exitosamente ✅
- **ivandresalin:** Logs generados exitosamente ✅
- **bironmanusa:** Logs generados exitosamente ✅

**Avance 3 - Análisis Semántico:**
- **Total:** 11 logs
- **Sam-24-dev:** Logs generados con validaciones exitosas ✅
- Pruebas con código correcto (0 errores)
- Pruebas con código incorrecto (4 errores detectados)

Los aportes están claramente marcados en el código con comentarios:
```python
# ============================================================
# INICIO APORTE: [Nombre] ([usuario-git])
# Responsable: [Descripción del componente]
# ============================================================
```

## 📊 Reglas Sintácticas y Semánticas Implementadas

### Funciones (Samir) ✅
**Sintáctico:**
- `tipo ID (parametros) { cuerpo }`
- `void ID (parametros) { cuerpo }`  
- `tipo ID (parametros) => expresion;` (arrow functions)
- `return expresion;`
- `return;`

**Semántico:**
- Funciones con tipo de retorno deben tener `return` en todos los caminos
- Validación de existencia de `return` statement
- Arrow functions válidas por definición (siempre retornan)

---

### Print e Input (Samir) ✅
**Sintáctico:**
- `print(expresion);`
- `stdin.readLineSync()`

---

### Variables y Expresiones (Mateo) ✅
**Sintáctico:**
- Declaraciones: `var`, `final`, `const`
- Expresiones aritméticas: `+`, `-`, `*`, `/`, `%`
- Listas y mapas

---

### Estructuras de Control (Andrés) ✅
**Sintáctico:**
- `if-else`, `while`, `for`, `do-while`
- `break`, `continue`

**Semántico (Samir):**
- `break` solo permitido dentro de bucles (while, for, do-while, for-in)
- `continue` solo permitido dentro de bucles
- Validación post-parsing del árbol sintáctico

---

### Análisis Semántico - Técnicas Implementadas

**Validación durante el parsing:**
- Regla 1 ejecutada en las reglas de funciones
- Tabla `function_table` actualizada durante reducción gramatical

**Validación post-parsing:**
- Regla 2 ejecutada después de construir el árbol completo
- Recorrido top-down del árbol sintáctico
- Tracking de contexto de loops con flag `in_loop`

## 📅 Entregas

| Avance | Descripción | Fecha Límite | Estado |
|--------|-------------|--------------|--------|
| **Avance 1** | Analizador Léxico | 12 de noviembre de 2025, 23:55 | ✅ ENTREGADO |
| **Avance 2** | Analizador Sintáctico | 15 de noviembre de 2025, 23:59 | ✅ ENTREGADO |
| **Avance 3** | Analizador Semántico | 17 de noviembre de 2025, 23:59 | 🔄 PARCIAL (Samir) |

**Nota Avance 3:** Solo la parte de Samir está implementada. Andrés y Mateo tienen pendientes sus reglas semánticas asignadas.

---

## 🎯 Reglas Semánticas Validadas

### Regla 1: Retorno de Funciones (Samir)
```dart
// ✅ CORRECTO
int sumar(int a, int b) {
  return a + b;  // Retorna en todos los caminos
}

// ❌ ERROR: Función 'funcionSinRetorno' debe retornar 'int' en todos los caminos
int funcionSinRetorno(int x) {
  int resultado = x + 10;
  print(resultado);
  // Falta return
}
```

### Regla 2: Break/Continue en Loops (Samir)
```dart
// ✅ CORRECTO
void funcionLoops() {
  for (int i = 0; i < 10; i++) {
    if (i == 5) break;  // OK: dentro de for
  }
  
  while (true) {
    continue;  // OK: dentro de while
  }
}

// ❌ ERROR: Línea X: 'break' fuera de bucle
void funcionIncorrecta() {
  if (x > 3) {
    break;  // ERROR: break no está en loop
  }
}
```

---

**Proyecto desarrollado para la materia de Lenguajes de Programación**
