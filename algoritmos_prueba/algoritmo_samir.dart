// ═══════════════════════════════════════════════════════════════════════════
// ALGORITMO DE PRUEBA - SAMIR CAIZAPASTO - VERSIÓN PARA SUSTENTACIÓN
// ═══════════════════════════════════════════════════════════════════════════

void main() {
  print("=== INICIO DEL PROGRAMA ===");
  
  // CÓDIGO FUNCIONAL (sin errores)
  var nombre = "Samir";
  var edad = 22;
  final String universidad = "ESPOL";
  
  print("Estudiante: " + nombre);
  print("Universidad: " + universidad);
  
  // ESTRUCTURA DE DATOS: Lista
  var calificaciones = [85, 90, 78, 92, 88];
  print("Calificaciones registradas: ");
  
  // ESTRUCTURA DE CONTROL: For loop
  var suma = 0;
  for (var i = 0; i < 5; i = i + 1) {
    suma = suma + calificaciones[i];
    print("Nota: " + calificaciones[i]);
  }
  
  // FUNCIÓN CON RETORNO (Regla Semántica)
  var promedio = calcularPromedio(suma, 5);
  print("Promedio final: " + promedio);
  
  if (promedio >= 70) {
    print("APROBADO");
  } else {
    print("REPROBADO");
  }
  
  print("=== FIN DEL PROGRAMA ===");
}

// Función con retorno en todos los caminos (Regla de Samir)
int calcularPromedio(int suma, int cantidad) {
  if (cantidad > 0) {
    return suma / cantidad;
  } else {
    return 0;
  }
}

// Función con break correcto dentro de loop (Regla de Samir)
void buscarNota(var notas, int objetivo) {
  for (var i = 0; i < 5; i = i + 1) {
    if (notas[i] == objetivo) {
      print("Nota encontrada en posicion: " + i);
      break;
    }
  }
}

// ═════════════════════════════════════════════════════════════════════════════
// SECCIÓN DE ERRORES PARA DEMOSTRACIÓN (COMENTADA)
// ═════════════════════════════════════════════════════════════════════════════

/*
// ❌ ERROR SINTÁCTICO: 
// var numeroErroneo = (5 + 3;

// ❌ ERROR SEMÁNTICO 
void funcionErrorVariable() {
  print(total);  // 'total' no está declarada
}

// ❌ ERROR SEMÁNTICO 2: break fuera de bucle 
void funcionErrorBreak() {
  break;  // break debe estar dentro de un loop
}

// ❌ ERROR SEMÁNTICO 3: Función sin retorno en todos los caminos 
int funcionSinRetorno(bool condicion) {
  if (condicion) {
    return 10;
  }
  // Falta return en el else implícito
}
