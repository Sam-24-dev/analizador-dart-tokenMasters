void main() {
  // === PRUEBAS VÁLIDAS ===
  var x = 10;

  // 1. if simple
  if (x > 5) {
    print("Mayor a 5");
  }

  // 2. if-else
  var flag = true;
  if (flag == false) {
    print("Falso");
  } else {
    print("Verdadero");
  }

  // 3. if-else if-else
  var temp = 25;
  if (temp < 0) {
    print("Congelado");
  } else if (temp < 30) {
    print("Normal");
  } else {
    print("Caliente");
  }

  // 4. if con sentencia simple (sin llaves)
  var a = 1;
  if (a == 1) print("a es 1");
  else print("a no es 1");


  // 6. while simple
  var i = 0;
  while (i < 5) {
    i = i + 1;
  }

  // 7. do-while
  var j = 10;
  do {
    j = j - 1;
  } while (j > 5);

  // 8. for tradicional (con todas las partes)
  for (var k = 0; k < 10; k = k + 1) {
    print(k);
  }

  // 10. for-in (for each)
  var numbers = [1, 2, 3];
  for (var num in numbers) {
    print(num);
  }

  // 11. break y continue
  for (var l = 0; l < 10; l = l + 1) {
    if (l == 5) break;
    if (l % 2 == 0) continue;
  }
}