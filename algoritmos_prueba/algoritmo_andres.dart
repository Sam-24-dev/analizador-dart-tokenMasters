// Archivo de prueba para Andrés Salinas (ivandresalin): Palabras Reservadas, Operadores, Delimitadores

import 'dart:async' show hide; // IMPORT, SHOW, HIDE

abstract class TestClass with Mixin { // ABSTRACT, CLASS, WITH, MIXIN
    final int baseValue = 100; // FINAL, BASE
    int? count = 1; // QUESTION, ASSIGN, NUMBER

    void testOperators(var a, var b) { // VOID, VAR, LPAREN, RPAREN
        if (a is! dynamic && b == baseValue) { // IF, IS_NOT, DYNAMIC_TYPE, AND, EQUALS, ID
            count++; // INCREMENT
            
            // Operadores de asignación y lógicos
            a += 5; // PLUSEQUAL
            if (b != null || a < 10) { // NOTEQUAL, OR, LESSTHAN
                b = a >> 1; // SHIFT_RIGHT
            }
        } else { // ELSE
            a = ~b; // ASSIGN, BITWISE_NOT
        }
    }
    
    // Operadores especiales y delimitadores
    var result = (a > 0) ? a : null; // GREATERTHAN, QUESTION, COLON, NULL
    var list = [1, 2, ...?count]; // LBRACKET, RBRACKET, COMMA, SPREAD, NULL_AWARE_SPREAD
    
    // Cascade (Cascada)
    var obj = TestClass()..count = 5 // CASCADE, DOT
                          ..baseValue *= 2; // TIMESEQUAL
                          
    // Arrow function
    String getName() => "Andres"; // ARROW, STRING

    int get area => count ?? 0; // GET, DOUBLE_QUESTION
}

// Sentencias de control
void main() {
    try {
        throw 'Error'; // THROW
    } on Exception catch (e) { // ON, CATCH
        return; // RETURN
    } finally { // FINALLY
        assert(true); // ASSERT
    }
}