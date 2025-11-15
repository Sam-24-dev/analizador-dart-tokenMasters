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