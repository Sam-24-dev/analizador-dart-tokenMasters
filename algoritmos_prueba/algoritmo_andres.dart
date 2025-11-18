void main() {
// === CASOS VÁLIDOS ===

// 1. Declaración mutable y asignación compatible
var contador = 10;
contador = 20; // Válido

// 2. Declaración inmutable (final) con inicialización correcta
final PI = 3.14159; // Válido

// 3. Conversión implícita válida (int a double)
double precio = 5; // Válido (5 se convierte implícitamente a 5.0)

// === CASOS INVÁLIDOS (DEBEN GENERAR ERRORES SEMÁNTICOS) ===

// 💥 ERROR 1: Asignación a variable final (Inmutabilidad)
final limite = 100;
limite = 150; 

// 💥 ERROR 2: Declaración final sin inicialización (Inicialización obligatoria)
final nombre;

// 💥 ERROR 3: Asignación incompatible de tipos (double a int sin cast)
int entero = 50;
entero = 10.5; // double a int requiere cast explícito

// 💥 ERROR 4: Uso de variable de ámbito local (existencia)
if (contador > 0) {
    var temporal = true;
}
var resultado = temporal; // 'temporal' fuera de alcance


}