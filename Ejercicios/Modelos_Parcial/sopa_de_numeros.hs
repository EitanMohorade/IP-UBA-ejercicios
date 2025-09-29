{-
Una sopa de n´umeros es un juego que consiste en descubrir propiedades de un tablero de dimensiones n × m con n y
 m>0, en los que en cada posici´on hay un n´umero entero positivo. Cada posici´on se identifica con una dupla (i,j) en el cual
 la primera componente corresponde a una fila y la segunda a una columna. A modo de ejemplo, la siguiente figura muestra
 un tablero de 5 × 4 en el que el n´umero 13 aparece en la posici´on (1,1) y el n´umero 5 aparece en la posici´on (4,3). Notar
 que tanto la numeraci´on de las filas como la de las columnas comienzan en 1.
-}
{-
 Un camino en un tablero est´a dado por una secuencia de posiciones adyacentes en la que solo es posible desplazarse
 desde una posici´on dada hacia la posici´on de su derecha o hacia la que se encuentra debajo. En otras palabras, un camino
 de longitud l en un tablero se define como una secuencia con l posiciones, ordenadas de manera tal que el elemento i-´esimo
 es la posici´on resultante de haberse movido hacia la derecha o hacia abajo desde la posici´on (i-1)-´esima. Siguiendo con el
 ejemplo, a continuaci´on puede observarse un camino de longitud 5 que representa la sucesi´on Fibonacci y que empieza en la
 posici´on (2,1) y termina en (4,3) del tablero.
-}

{-
 Para manipular las sopas de n´umeros en Haskell vamos a representar el tablero como una lista de filas de igual longitud.
 A su vez, cada fila vamos a representarla como una lista de enteros positivos. Las posiciones vamos a representarlas con
 tuplas de dos n´umeros enteros positivos y un camino va a estar dado por una lista de posiciones.
 Para implementar esta sopa de n´umeros nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desa
rrollo enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducci´on
 a la Programaci´on / Algoritmos y Estructuras de Datos I (FCEyN-UBA). Asumimos los siguientes renombres de tipos de
 datos en las especificaciones de los ejercicios:
 Fila = seq⟨Z⟩
 Tablero = seq⟨Fila⟩
 Posicion = Z×Z– Observaci´on: las posiciones son: (fila, columna)
 Camino = seq⟨Posicion⟩
-}

{-Ejercicio 1 Implementar la funci´on maximo :: Tablero->Int
 problema maximo (t: Tablero) : Z {
 requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
 menos un elemento}
 requiere: {Existe al menos una columna en el tablero t }
 requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
 asegura: {res es igual al n´umero m´as grande del tablero t}
 }
-}

{-Ejercicio 2
 Implementar la funci´on masRepetido :: Tablero->Int
 problema masRepetido (t: Tablero) : Z {
 requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
 menos un elemento}
 requiere: {Existe al menos una columna en el tablero t }
 requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayor estricto a 0}
 asegura: {res es igual al n´umero que m´as veces aparece en un tablero t. Si hay empate devuelve cualquiera de ellos}
 }
-}

{-Ejercicio 3
 Implementar la funci´on valoresDeCamino :: Tablero->Camino->[Int]
 problema valoresDeCamino (t: Tablero, c: Camino) : seq⟨Z⟩ {
 requiere: {El tablero t es un tablero bien formado, es decir, la longitud de todas las filas es la misma, y tienen al
 menos un elemento}
 requiere: {Existe al menos una columna en el tablero t }
 requiere: {El tablero t no es vac´ıo, todos los n´umeros del tablero son positivos, mayores estrictos a 0}
 requiere: {El camino c es un camino v´alido, es decir, secuencia de posiciones adyacentes en la que solo es posible
 desplazarse hacia la posici´on de la derecha o hacia abajo y todas las posiciones est´an dentro de los limites del tablero
 t}
 asegura: {res es igual a la secuencia de n´umeros que est´an en el camino c, ordenados de la misma forma que aparecen
 las posiciones correspondientes en el camino.}
 }
-}

{-Ejercicio 4
 Implementar la funci´on esCaminoFibo :: [Int]->Int->Bool
 problema esCaminoFibo (s:seq⟨Z⟩, i : Z) : Bool {
 requiere: {La secuencia de n´umeros s es no vac´ıa y est´a compuesta por n´umeros positivos (mayores estrictos a 0)
 que representan los n´umeros ubicados en las posiciones que forman un camino en un tablero}
 requiere: {i ≥ 0}
 asegura: {res = true ⇔ los valores de s son la sucesi´on de Fibonacci inicializada con el n´umero pasado como
 par´ametro i}
 }
 Notas: En este ejercicio se pasa una secuencia de valores en lugar de un tablero y un camino para no generar dependencia
 con el ejercicio anterior. Recordemos que la sucesi´on de Fibonacci est´a definida con la siguiente funci´on recursiva:
 f(0) = 0
 f(1) = 1
 f(n) = f(n-1) + f(n-2) con n>1
 En el ejemplo del tablero y del camino (verde claro) que figuran m´as arriba tenemos que esCaminoFibo [1,1,2,3,5] 1
 reduce a True.
 esCaminoFibo (valoresDeCamino tablero [(3,2), (4, 2), (4,3)]) 3, siendo tablero el del ejemplo, tambi´en reduce a
 True.
-}