// Algoritmo de Prueba - Samir Caizapasto
// Propósito: Validar funciones, print e input

void main() {
  // Print básico
  print("Iniciando programa...");
  
  // Declaración de variables
  var nombre = "Samir";
  int edad = 20;
  
  print("Nombre: Samir");
  
  // Llamada a función
  int resultado = sumar(10, 5);
  print(resultado);
  
  // Función que retorna
  double promedio = calcularPromedio(8, 9);
  print(promedio);
  
  // Solicitar entrada (comentado para no causar error)
  // var input = stdin.readLineSync();
}

// ============================================================================
// FUNCIONES CORRECTAS (para validar sintáctico)
// ============================================================================

// Función con retorno y parámetros
int sumar(int a, int b) {
  return a + b;
}

// Función con retorno
double calcularPromedio(int a, int b) {
  return (a + b) / 2;
}

// Función void
void mostrarMensaje() {
  print("Este es un mensaje");
}

// Arrow function
int duplicar(int x) => x * 2;

// ============================================================================
// FUNCIONES CON ERRORES SEMÁNTICOS (para validar semántico)
// Descomentar para probar análisis semántico
// ============================================================================

// ERROR SEMÁNTICO 1: Función sin return
/*
int funcionSinRetorno(int x) {
  int resultado = x + 10;
  print(resultado);
  // ERROR: Falta return
}
*/

// ERROR SEMÁNTICO 2: No todos los caminos retornan
/*
int funcionRetornoParcial(int x) {
  if (x > 0) {
    return x;
  }
  // ERROR: Falta return cuando x <= 0
}
*/

// ERROR SEMÁNTICO 3: break fuera de loop
/*
void funcionBreakIncorrecto() {
  int x = 5;
  if (x > 3) {
    break;  // ERROR: break fuera de loop
  }
}
*/

// ERROR SEMÁNTICO 4: continue fuera de loop
/*
void funcionContinueIncorrecto() {
  int y = 10;
  continue;  // ERROR: continue fuera de loop
}
*/

// FUNCIÓN CORRECTA: Loops con break/continue (correcto)
void funcionLoopsCorrectos() {
  for (int i = 0; i < 10; i = i + 1) {
    if (i == 5) {
      break;  // OK: dentro de for
    }
  }
  
  int contador = 0;
  while (contador < 5) {
    contador = contador + 1;
    if (contador == 3) {
      continue;  // OK: dentro de while
    }
  }
}
