# Analizador Léxico-Sintáctico-Semántico para Dart - TokenMasters

## 📦 Instalación y Dependencias

### Requisitos
- **Python 3.7+**

### Librerías necesarias
```bash
pip install ply
```

O usando el archivo de dependencias:
```bash
pip install -r requirements.txt
```

El archivo `requirements.txt` contiene:
```
ply==3.11
```

### Ejecutar el proyecto
```bash
python gui.py
```

---

## 👥 Equipo

| Integrante | GitHub |
|------------|--------|
| Samir Caizapasto | [@Sam-24-dev](https://github.com/Sam-24-dev) |
| Andrés Salinas | [@ivandresalin](https://github.com/ivandresalin) |
| Mateo Mayorga | [@bironmanusa](https://github.com/bironmanusa) |

---

## 📋 Descripción

Compilador completo para Dart con análisis léxico, sintáctico y semántico usando PLY (Python Lex-Yacc).

### Avance 1: Analizador Léxico ✅
- Reconocimiento de tokens (palabras reservadas, operadores, identificadores)
- Detección de errores léxicos

### Avance 2: Analizador Sintáctico ✅
- Validación de estructura gramatical
- Estructuras de control: if, while, for, do-while
- Detección de errores sintácticos con línea

### Avance 3: Analizador Semántico ✅
| Integrante | Reglas implementadas |
|------------|---------------------|
| **Samir** | Retorno de funciones, break/continue fuera de bucle |
| **Andrés** | Alcance de variables, inmutabilidad (final/const) |
| **Mateo** | Null-safety, compatibilidad de tipos, conversiones |

---

## 📁 Estructura del Proyecto

```
analizador-dart-tokenMasters/
├── lexer.py              # Analizador léxico
├── parser.py             # Analizador sintáctico y semántico
├── gui.py                # Interfaz gráfica
├── analyzer_service.py   # Servicio auxiliar
├── requirements.txt      # Dependencias
├── algoritmos_prueba/    # Algoritmos de prueba (.dart)
│   ├── algoritmo_samir.dart
│   ├── algoritmo_andres.dart
│   └── algoritmo_mateo.dart
└── logs/                 # Logs generados por análisis
    ├── lexico-*.txt
    ├── sintactico-*.txt
    └── semantico-*.txt
```

---

## 🚀 Uso

1. Ejecutar: `python gui.py`
2. Cargar un archivo `.dart` o escribir código
3. Ingresar nombre de usuario Git
4. Clic en "Analizar Código"
5. Ver resultados (tokens, errores) y logs generados

---

## 📝 Algoritmos de Prueba

- `algoritmo_samir.dart` - Funciones, print, errores de demo
- `algoritmo_andres.dart` - Estructuras de control (do-while, for, if-else)
- `algoritmo_mateo.dart` - Fibonacci recursivo

---

**Proyecto Final - Compiladores 2025**
