#  Ejercicio 16. Hospital- Nivel de ocupaci´on
#  Queremos saber qu´e porcentaje de ocupaci´on de camas hay en el hospital. El hospital se representa por una matriz en donde
#  las filas son los pisos, y las columnas son las camas. Los valores de la matriz son Booleanos que indican si la cama est´a ocupada
#  o no. Si el valor es verdadero (True) indica que la cama est´a ocupada.
#  Se nos pide programar en Python una funci´on que devuelve una secuencia de reales, indicando la proporci´on de camas
#  ocupadas en cada piso.
#  problema nivel
#  de
#  ocupacion (in camas por piso:seq⟨seq⟨Bool⟩⟩) : seq⟨R⟩ {
# requiere: {Todos los pisos tienen la misma cantidad de camas.}
#  requiere: {Hay por lo menos 1 piso en el hospital.}
#  requiere: {Hay por lo menos una cama por piso.}
#  asegura: {|res| = |camas por piso|.}
#  asegura: {Para todo 0 ≤ i < |res| se cumple que res[i] es igual a la cantidad de camas ocupadas del piso i dividido el
#  total de camas del piso i).}
#  }