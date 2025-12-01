// Algoritmo de Prueba - Mateo Mayorga
// Propósito: Validar el analizador léxico para números, strings e identificadores

// Funcion recursiva de Fibonacci
int fibonacci(int n) {
    if (n <= 0){
        return 0; // Caso base: fibonacci(0) = 0
    }

    if (n == 1){
        return 1; // Caso base: fibonacci(1) = 1
    }
    
    return fibonacci(n-1) + fibonacci(n-2); //Caso recursivo fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
}

void main() {
    int n = [0,1,2,3,4,5,6,7,8,9]; 
    for (int i = 0; i < n.length; i++){
        print(fibonacci(i));
    }
}