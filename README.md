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

### Avance 3: Analizador Semántico ✅ COMPLETADO
**Implementado (Samir):**
- ✅ **Regla 1:** Retorno de funciones (COMPLETO)
  - Validación de tipo de retorno compatible con expresión retornada
  - Funciones con tipo de retorno deben retornar en todos los caminos
  - Validación de if-else: ambas ramas deben retornar
  - Validación de if-elif-else: todas las ramas deben retornar
  - Generación de errores con número de línea
- ✅ **Regla 2:** Estructuras de control (break/continue) (COMPLETO)
  - `break` y `continue` solo permitidos dentro de bucles
  - Validación post-parsing del árbol sintáctico
  - Reporte de errores con línea exacta

**Implementado (Andrés):**
- ✅ **Reglas de Identificadores:** Existencia y Alcance (COMPLETO)
  - Sistema de ámbitos (scopes) con pila de tablas de símbolos
  - Búsqueda de variables con alcance léxico
  - Validación de re-declaración en mismo ámbito
  - Validación de inmutabilidad (final/const)
  - Validación de inicialización obligatoria para inmutables

**Implementado (Mateo):**
- ✅ **Reglas de Operaciones Permitidas:** (COMPLETO)
  - Validación de null-safety en operaciones
  - Compatibilidad aritmética entre tipos
  - Validación de operadores lógicos con booleanos
  - Comparaciones entre tipos compatibles
- ✅ **Reglas de Conversión:** (COMPLETO)
  - Conversión implícita (int → double, int/double → num)
  - Detección de conversiones que requieren cast explícito
  - Inferencia completa de tipos desde expresiones
  - Validación de compatibilidad en asignaciones

**Entrega completa:** 17 de noviembre de 2025

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
│   ├── sintactico-*.txt      # 17 logs de análisis sintáctico
│   └── semantico-*.txt       # 31 logs de análisis semántico
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
- [x] Generación de 17 logs sintácticos ✅
- [x] **Entregado: 15 de noviembre de 2025**

### Avance 3: Analizador Semántico ✅ COMPLETADO
**Implementado (Samir):**
- [x] Tablas semánticas (scope_stack, function_table, semantic_errors) ✅
- [x] **Regla 1:** Validación de retornos en funciones ✅
  - [x] Funciones con tipo de retorno deben tener `return`
  - [x] Validación en todos los caminos de ejecución
  - [x] Funciones helper: `has_return_in_all_paths()`, `validate_return_type()`
- [x] **Regla 2:** Validación de break/continue ✅
  - [x] `break` solo dentro de loops
  - [x] `continue` solo dentro de loops
  - [x] Validación post-parsing del árbol sintáctico
  - [x] Función helper: `validate_break_continue()`

**Implementado (Andrés):**
- [x] Sistema de ámbitos (scopes) con pila de símbolos ✅
- [x] **Reglas de Identificadores:** Existencia y Alcance ✅
  - [x] Validación de existencia de variables
  - [x] Búsqueda con alcance léxico
  - [x] Validación de re-declaración
  - [x] Validación de inmutabilidad (final/const)
  - [x] Funciones helper: `push_scope()`, `pop_scope()`, `lookup_variable()`, `register_variable()`

**Implementado (Mateo):**
- [x] **Reglas de Operaciones Permitidas:** ✅
  - [x] Validación de null-safety
  - [x] Compatibilidad aritmética entre tipos
  - [x] Validación de operadores lógicos
  - [x] Función helper: `validate_binary_operations()`
- [x] **Reglas de Conversión:** ✅
  - [x] Conversión implícita (int → double)
  - [x] Detección de cast explícito requerido
  - [x] Inferencia de tipos
  - [x] Funciones helper: `infer_type()`, `can_implicitly_convert()`

- [x] Generación de 31 logs semánticos ✅
- [x] Reportar errores con número de línea ✅
- [x] Opción `--semantico` y `--ambos` ✅
- [x] Encoding UTF-8-sig para tildes ✅
- [x] **Entregado: 17 de noviembre de 2025**

## 💻 Uso de los Analizadores

### Interfaz Gráfica (GUI)

La forma más cómoda de probar el analizador completo es ejecutar la
interfaz Tkinter incluida en `gui.py`, la cual expone un editor de
texto, botones para cargar/analizar/limpiar, pestañas de resultados y
una barra de estado. Para iniciarla:

```powershell
python gui.py
```

1. Escribe o carga un archivo `.dart` (botón **Cargar archivo…**).
2. Indica el usuario Git (campo en la parte superior) o deja el valor
  por defecto.
3. Presiona **Analizar** para ejecutar en secuencia los análisis
  léxico, sintáctico y semántico.
4. Consulta la pestaña **Tokens** y la pestaña **Errores**; la GUI
  también muestra las rutas de los logs generados automáticamente.

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

### Avance 3: Análisis Semántico ✅ COMPLETADO

**Samir Caizapasto (Sam-24-dev):** ✅ COMPLETADO
- **Regla 1: Retorno de funciones (COMPLETO)**
  - Validación de tipo de retorno compatible con expresión retornada
  - Validación de que funciones con tipo de retorno tengan `return`
  - Verificación de `return` en todos los caminos de ejecución (if-else, if-elif-else)
  - Funciones helper: `has_return_in_all_paths()`, `has_return_in_block()`, `has_return_in_elif_chain()`, `validate_return_type()`
- **Regla 2: Break/Continue en loops (COMPLETO)**
  - Validación de `break` solo dentro de bucles
  - Validación de `continue` solo dentro de bucles
  - Función helper: `validate_break_continue()` (post-parsing con recorrido del árbol)
  - Reporte de errores con número de línea

**Andrés Salinas (ivandresalin):** ✅ COMPLETADO
- **Reglas de Identificadores: Existencia y Alcance (COMPLETO)**
  - Sistema de ámbitos (scopes) con pila de tablas de símbolos
  - Funciones de gestión: `push_scope()`, `pop_scope()`, `get_current_scope()`, `lookup_variable()`
  - Búsqueda de variables con alcance léxico (de local a global)
  - Validación de re-declaración en mismo ámbito
  - Validación de inmutabilidad (final/const) con `validate_assignment()`
  - Validación de inicialización obligatoria para variables inmutables
  - Función helper: `register_variable()`

**Mateo Mayorga (bironmanusa):** ✅ COMPLETADO
- **Reglas de Operaciones Permitidas (COMPLETO)**
  - Validación de null-safety en operaciones binarias
  - Compatibilidad aritmética entre tipos numéricos
  - Validación de operadores lógicos requieren booleanos
  - Comparaciones solo entre tipos compatibles
  - Función helper: `validate_binary_operations()`
- **Reglas de Conversión (COMPLETO)**
  - Conversión implícita permitida (int → double, int/double → num)
  - Detección de conversiones que requieren cast explícito (double → int)
  - Inferencia completa de tipos desde expresiones
  - Validación de compatibilidad en asignaciones y declaraciones
  - Funciones helper: `infer_type()`, `can_implicitly_convert()`, `is_numeric_type()`, `get_base_type()`

**Sistema Completo:**
- Tablas semánticas: `scope_stack`, `function_table`, `semantic_errors`
- Sistema de logs semánticos con encoding UTF-8-sig (Windows compatible)
- Opción `--semantico` y `--ambos` en parser.py
- Reporte de errores con número de línea en PowerShell y logs
- Limpieza automática de tablas entre análisis múltiples

### Logs Generados

**Avance 1 - Análisis Léxico:**
- **Total:** 17 logs
- **Sam-24-dev:** 3 logs
- **bironmanusa:** 11 logs (múltiples pruebas)
- **ivandresalin:** 2 logs

**Avance 2 - Análisis Sintáctico:**
- **Total:** 17 logs
- **Sam-24-dev:** Logs generados exitosamente ✅
- **ivandresalin:** Logs generados exitosamente ✅
- **bironmanusa:** Logs generados exitosamente ✅

**Avance 3 - Análisis Semántico:**
- **Total:** 31 logs
- **Sam-24-dev:** Logs generados con validaciones exitosas ✅
- **ivandresalin:** Implementación completa de alcance y existencia ✅
- **bironmanusa:** Implementación completa de operaciones y conversiones ✅
- Pruebas con código correcto (0 errores)
- Pruebas con código incorrecto (errores detectados correctamente)

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
| **Avance 3** | Analizador Semántico | 17 de noviembre de 2025, 23:59 | ✅ COMPLETADO |

**Nota Importante:** Todos los avances están completos. La GUI (Interfaz Gráfica) será implementada en una fase posterior del proyecto.

---

## 🎯 Reglas Semánticas Validadas

### Regla 1: Retorno de Funciones (Samir) ✅
```dart
// ✅ CORRECTO
int sumar(int a, int b) {
  return a + b;  // Retorna en todos los caminos
}

// ✅ CORRECTO: if-else ambas ramas retornan
int absoluto(int x) {
  if (x >= 0) {
    return x;
  } else {
    return -x;
  }
}

// ❌ ERROR: Función 'funcionSinRetorno' debe retornar 'int' en todos los caminos
int funcionSinRetorno(int x) {
  int resultado = x + 10;
  print(resultado);
  // Falta return
}

// ❌ ERROR: No todos los caminos retornan
int funcionRetornoParcial(int x) {
  if (x > 0) {
    return x;
  }
  // ERROR: Falta return cuando x <= 0
}
```

### Regla 2: Break/Continue en Loops (Samir) ✅
```dart
// ✅ CORRECTO
void funcionLoops() {
  for (int i = 0; i < 10; i = i + 1) {
    if (i == 5) break;  // OK: dentro de for
  }
  
  while (true) {
    continue;  // OK: dentro de while
  }
}

// ❌ ERROR: 'break' fuera de bucle
void funcionIncorrecta() {
  if (x > 3) {
    break;  // ERROR: break no está en loop
  }
}

// ❌ ERROR: 'continue' fuera de bucle
void otraFuncionIncorrecta() {
  continue;  // ERROR: continue no está en loop
}
```

### Regla 3: Alcance y Existencia de Variables (Andrés) ✅
```dart
// ✅ CORRECTO: Variables en diferentes ámbitos
void funcionConAmbitos() {
  int x = 10;  // Ámbito de función
  
  if (x > 5) {
    int y = 20;  // Ámbito de bloque if
    print(x);    // OK: x visible desde ámbito padre
    print(y);    // OK: y en ámbito actual
  }
  
  print(x);  // OK: x en ámbito actual
  // print(y);  // ERROR: y no existe en este ámbito
}

// ❌ ERROR: Variable ya declarada en este ámbito
void redeclaracion() {
  int x = 10;
  int x = 20;  // ERROR: 'x' ya declarada
}

// ❌ ERROR: Variable inmutable no puede ser reasignada
void inmutabilidad() {
  final int x = 10;
  x = 20;  // ERROR: No se puede asignar a variable inmutable 'x'
}

// ❌ ERROR: const/final debe ser inicializada
void inicializacionObligatoria() {
  final int x;  // ERROR: 'x' declarada como final debe ser inicializada
}
```

### Regla 4: Operaciones y Null Safety (Mateo) ✅
```dart
// ✅ CORRECTO: Operaciones entre tipos compatibles
void operacionesCorrectas() {
  int a = 10;
  int b = 5;
  int suma = a + b;        // OK: int + int = int
  double division = a / 2;  // OK: int / int = double
  
  String s1 = "Hola";
  String s2 = " Mundo";
  String concatenacion = s1 + s2;  // OK: String + String
}

// ❌ ERROR: Operador aritmético requiere operandos numéricos
void operacionIncorrecta() {
  String texto = "10";
  int numero = 5;
  int resultado = texto + numero;  // ERROR: String + int no permitido
}

// ❌ ERROR: Operador lógico requiere operandos booleanos
void operadorLogicoIncorrecto() {
  int x = 10;
  int y = 5;
  bool resultado = x && y;  // ERROR: && requiere bool, no int
}

// ❌ ERROR: Operación con valor null sin comprobación
void nullSafety() {
  int? x = null;
  int y = 10;
  int resultado = x + y;  // ERROR: Operación '+' con valor null
}
```

### Regla 5: Conversiones y Compatibilidad de Tipos (Mateo) ✅
```dart
// ✅ CORRECTO: Conversión implícita permitida
void conversionImplicita() {
  int entero = 10;
  double decimal = entero;  // OK: int → double implícito
}

// ✅ CORRECTO: Inferencia de tipos
void inferenciaTipos() {
  var x = 10;        // Inferido como int
  var y = 10.5;      // Inferido como double
  var z = "texto";   // Inferido como String
}

// ❌ ERROR: Conversión requiere cast explícito
void castExplicito() {
  double decimal = 10.5;
  int entero = decimal;  // ERROR: double → int requiere cast
}

// ❌ ERROR: Tipo incompatible en asignación
void incompatibilidadTipos() {
  int numero = 10;
  String texto = numero;  // ERROR: No se puede asignar int a String
}

// ❌ ERROR: Asignación incompatible
void asignacionIncompatible() {
  int x = 10;
  bool y = x;  // ERROR: No se puede asignar int a bool
}
```

---

**Proyecto desarrollado para la materia de Lenguajes de Programación**
