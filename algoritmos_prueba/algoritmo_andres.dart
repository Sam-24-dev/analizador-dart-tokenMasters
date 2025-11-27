void main() {
  // ==========================================================
  // 1. DECLARACIÓN DE VARIABLES Y CONSTANTES (Aporte Lexer/Parser)
  // ==========================================================
  
  // 'const': Valor constante en tiempo de compilación (Regla Andrés)
  const int LIMITE_MAXIMO = 50;
  
  // 'final': Inmutable, se asigna una vez (Regla Andrés)
  final int topeSuma = 200;
  
  // 'var': Inferencia de tipo (int)
  var sumaTotal = 0;
  
  // Tipos explícitos
  int contadorPrimos = 0;
  int numeroActual = 0;

  // ==========================================================
  // 2. ESTRUCTURA DO-WHILE (Aporte Parser: p_do_while_statement)
  // ==========================================================
  do {
    numeroActual++;

    // ==========================================================
    // 3. ESTRUCTURA IF-ELSE CHAIN (Aporte Parser: p_if_statement)
    // ==========================================================
    
    // Regla de negocio: Ignorar el número 1 y saltar pares excepto el 2
    if (numeroActual == 1) {
      continue; // Salto de iteración (Aporte Parser: p_continue_statement)
    } else if (numeroActual > 2 && numeroActual % 2 == 0) {
      continue; 
    }

    // ==========================================================
    // 4. GESTIÓN DE ÁMBITO/SCOPE (Aporte Parser: push_scope/pop_scope)
    // ==========================================================
    // 'esPrimo' solo existe dentro de este bloque del do-while
    bool esPrimo = true; 
    
    // ==========================================================
    // 5. ESTRUCTURA FOR TRADICIONAL (Aporte Parser: p_for_statement)
    // ==========================================================
    // Variable 'i' local al bucle for (Scope anidado)
    for (int i = 3; i * i <= numeroActual; i += 2) {
      if (numeroActual % i == 0) {
        esPrimo = false;
        break; // Romper el for interno (Aporte Parser: p_break_statement)
      }
    }

    // ==========================================================
    // 6. LÓGICA DE ACTUALIZACIÓN Y CONTROL
    // ==========================================================
    if (esPrimo) {
      sumaTotal += numeroActual;
      contadorPrimos++;
      
      // Uso de print (Soportado sintácticamente)
      print(numeroActual);
    }

    // Verificación de invariante 'final' para detener el ciclo
    if (sumaTotal >= topeSuma) {
      print('Alerta: Límite de seguridad alcanzado.');
      break; // Romper el do-while externo
    }

  // ==========================================================
  // 7. OPERADORES RELACIONALES (Aporte Lexer)
  // ==========================================================
  } while (numeroActual < LIMITE_MAXIMO);

  // ==========================================================
  // 8. ESTRUCTURA WHILE (Aporte Parser: p_while_statement)
  // ==========================================================
  // Bucle simple de finalización
  while (contadorPrimos > 0) {
    contadorPrimos--; 
    // Solo para vaciar el contador demostrando el uso de while
  }
}