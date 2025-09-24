{-
En este ejercicio vamos a trabajar con matrices.
 Vamos a representar una matriz como una secuencia de secuencias. Si m es nuestra secuencia de secuencias que representa
 una matriz: La secuencia i-´esima de m representa la i-´esima fila de la matriz, y el elemento j-´esimo dentro de la secuencia
 i-´esima representa el elemento en la fila i, columna j de la matriz.
 Por ejemplo, a la matriz identidad de R3 la podemos definir como la lista de listas: [[1,0,0],[0,1,0],[0,0,1]] en Haskell.
 Usando esta representaci´on, definir las siguientes funciones sobre matrices:
 1. sumaTotal :: [[Integer]]-> Integer seg´un la siguiente especificaci´on:
 problema sumaTotal (m: seq⟨seq⟨Z⟩⟩) : Z {
 requiere: { |m| > 0 }
 requiere: { |m[0]| > 0 }
 requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
 asegura: { resultado = |m|−1
 i=0
 }
 |m[i]|−1
 j=0
 m[i][j] }
-}

{-
 2. cantidadDeApariciones :: Integer-> [[Integer]]-> Integer seg´un la siguiente especificaci´on:
 problema cantidadDeApariciones (e: Z, m: seq⟨seq⟨Z⟩⟩) : Z {
 requiere: { |m| > 0 }
 requiere: { |m[0]| > 0 }
 requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
 asegura: { resultado = |m|−1
 i=0
 }
 |m[i]|−1
 j=0
 1 si m[i][j] es igual a e, 0 si no }
 
-}

{- 
 3. contarPalabras :: String->[[String]]->Int seg´un la siguiente especificaci´on:
 problema contarPalabras (p: String, m: seq⟨seq⟨String⟩⟩) : Z {
 requiere: { |m| > 0 }
 requiere: { |m[0]| > 0 }
 requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
 asegura: { El resultado es la cantidad de veces que p aparece exactamente igual en los elementos de m }
 }

-}

{-
 4. cantidadDeApariciones2 :: (Eq a) => a-> [[a]]-> Integer tal que pueda usarlo para resolver los dos ejerci
cios anteriores.
-}

{-
 5. multiplicarPorEscalar :: Integer-> [[Integer]]-> [[Integer]] seg´un la siguiente especificaci´on:
 problema multiplicarPorEscalar (lambda: Z, m: seq⟨seq⟨Z⟩⟩) : seq⟨seq⟨Z⟩⟩ {
 requiere: { |m| > 0 }
 requiere: { |m[0]| > 0 }
 requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
 asegura: { |resultado| = m }
 asegura: { Para todo 0 ≤ i < |m|, |resultado[i]| = |m[i]| }
 asegura: { Para toda posici´on v´alida i,j de m, resultado[i][j] = lambda × m[i][j]}}
 -}

{-
6. concatenarFilas :: [[String]]->[String] seg´un la siguiente especificaci´on:
 problema concatenarFilas (m: seq⟨seq⟨String⟩⟩) : seq⟨String⟩ {
 requiere: { |m| > 0 }
 requiere: { |m[0]| > 0 }
 requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
 asegura: { |resultado| = |m| }
 asegura: { Para todo 0 ≤ i < |m|, resultado[i] = concatenaci´on de todos los strings en m[i] }
 }
 -}

{-
 7. i´esimaFila :: Integer-> [[a]]-> [a] seg´un la siguiente especificaci´on:
 problema i´esimaFila (i: Z, m: seq⟨seq⟨T⟩⟩) : seq⟨T⟩ {
 requiere: { |m| > 0 }
 requiere: { |m[0]| > 0 }
 requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
 requiere: { 0 ≤ i < |m| }
 asegura: { |resultado| = |m[i]| }
 asegura: { Para todo 0 <= j < |m[i]|, resultado[j] = m[i][j] }
 }
-}

{-
 8. i´esimaColumna :: Integer-> [[a]]-> [a] seg´un la siguiente especificaci´on:
 problema i´esimaColumna (i: Z, m: seq⟨seq⟨T⟩⟩) : seq⟨T⟩ {
 requiere: { |m| > 0 }
 requiere: { |m[0]| > 0 }
 requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
 requiere: { 0 ≤ i < |m[0]| }
 asegura: { |resultado| = |m| }
 asegura: { Para todo 0 <= f < |m|, resultado[f] = m[f][i] }
 }

-}

{-
 9. matrizIdentidad :: Integer-> [[Integer]] seg´un la siguiente especificaci´on:
 problema matrizIdentidad (n: Z) : seq⟨seq⟨Z⟩⟩ {
 requiere: { n > 0 }
 asegura: { |resultado| = n }
 asegura: { Para todo 0 <= i < n, |resultado[i]| = n}
 asegura: { Para todo 0 <= i < n, resultado[i][i] = 1 }
 asegura: { Para todo 0 ≤ i,j < n, si i es distinto de j entonces resultado[i][j] = 0 }
 }
 
 Sugerencia: Pensar en una funci´on auxiliar que genere la i-´esima fila de la matriz identidad de tama˜no n.
 
-} 


{-
 10. cantidadParesColumna :: Integer-> [[Integer]]-> Integer seg´un la siguiente especificaci´on:
 problema cantidadParesColumna (i: Z, m: seq⟨seq⟨Z⟩⟩) : Z {
 requiere: { |m| > 0 }
 requiere: { |m[0]| > 0 }
 requiere: { Todos los elementos de la secuencia m tienen la misma longitud }
 requiere: { 0 ≤ i < |m[0]| }
 asegura: { resultado = |m|−1
 j=0 1 si m[j][i] es par, 0 si no}
 }
-}