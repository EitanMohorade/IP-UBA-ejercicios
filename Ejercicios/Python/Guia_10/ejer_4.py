#  Ejercicio 4. Veterinaria- Tabla turnos
#  Las personas responsables de los turnos est´an anotadas en una matriz donde las columnas representan los d´ıas, en orden de
#  lunes a domingo, y cada fila un rango de una hora. Hay cuatro filas para los turnos de la ma˜nana (9, 10, 11 y 12 hs) y otras
#  cuatro para la tarde (14, 15, 16 y 17).
#  1
# Para hacer m´as eficiente el trabajo del personal de una veterinaria, se necesita analizar si quienes quedan de responsables,
#  est´an asignadas de manera continuada en los turnos de cada d´ıa.
#  Para ello se pide desarrollar una funci´on en Python que, dada la matriz de turnos, devuelva una lista de tuplas de bool, una
#  por cada d´ıa. Cada tupla debe contener dos elementos. El primer elemento debe ser True si y solo si todos los valores de los
#  turnos de la ma˜nana para ese d´ıa son iguales entre s´ı. El segundo elemento debe ser True si y solo si todos los valores de los
#  turnos de la tarde para ese d´ıa son iguales entre s´ı.
#  Siempre hay una persona responsable en cualquier horario de la veterinaria.
#  problema un
#  responsable
#  por
#  turno (in grilla
#  horaria : seq⟨seq⟨str⟩⟩) : seq⟨Bool × Bool⟩ {
#  requiere: {|grilla horaria| = 8.}
#  requiere: {Todos los elementos de grilla horaria tienen el mismo tama˜no (mayor a 0 y menor 8).}
#  requiere: {No hay cadenas vac´ıas en las listas de grilla horaria.}
#  asegura: {|res| = |grilla horaria[0]|.}
#  asegura: {El primer valor de la tupla en res [i], con i:Z, 0 res| es igual a True los primeros 4 valores de la columna i de
#  grilla horaria son iguales entre s´ı.}
#  asegura: {El segundo valor de la tupla en res [i], con i:Z, 0 res| es igual a True los ´ultimos 4 valores de la columna i de
#  grilla horaria son iguales entre s´ı.}
#  } Ejercicio 4. Veterinaria- Tabla turnos
#  Las personas responsables de los turnos est´an anotadas en una matriz donde las columnas representan los d´ıas, en orden de
#  lunes a domingo, y cada fila un rango de una hora. Hay cuatro filas para los turnos de la ma˜nana (9, 10, 11 y 12 hs) y otras
#  cuatro para la tarde (14, 15, 16 y 17).
#  1
# Para hacer m´as eficiente el trabajo del personal de una veterinaria, se necesita analizar si quienes quedan de responsables,
#  est´an asignadas de manera continuada en los turnos de cada d´ıa.
#  Para ello se pide desarrollar una funci´on en Python que, dada la matriz de turnos, devuelva una lista de tuplas de bool, una
#  por cada d´ıa. Cada tupla debe contener dos elementos. El primer elemento debe ser True si y solo si todos los valores de los
#  turnos de la ma˜nana para ese d´ıa son iguales entre s´ı. El segundo elemento debe ser True si y solo si todos los valores de los
#  turnos de la tarde para ese d´ıa son iguales entre s´ı.
#  Siempre hay una persona responsable en cualquier horario de la veterinaria.
#  problema un
#  responsable
#  por
#  turno (in grilla
#  horaria : seq⟨seq⟨str⟩⟩) : seq⟨Bool × Bool⟩ {
#  requiere: {|grilla horaria| = 8.}
#  requiere: {Todos los elementos de grilla horaria tienen el mismo tama˜no (mayor a 0 y menor 8).}
#  requiere: {No hay cadenas vac´ıas en las listas de grilla horaria.}
#  asegura: {|res| = |grilla horaria[0]|.}
#  asegura: {El primer valor de la tupla en res [i], con i:Z, 0 res| es igual a True los primeros 4 valores de la columna i de
#  grilla horaria son iguales entre s´ı.}
#  asegura: {El segundo valor de la tupla en res [i], con i:Z, 0 res| es igual a True los ´ultimos 4 valores de la columna i de
#  grilla horaria son iguales entre s´ı.}
#  }