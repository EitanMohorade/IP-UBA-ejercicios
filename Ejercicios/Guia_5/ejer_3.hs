{-
 Definir las siguientes funciones sobre listas de enteros:
 1. sumatoria :: [Integer]-> Integer seg´un la siguiente especificaci´on:
 problema sumatoria (s: seq⟨Z⟩) : Z {
 requiere: { True }
 asegura: { resultado = |s|−1
 i=0 s[i] }
 }
-}

{-
 2. productoria :: [Integer]-> Integer seg´un la siguiente especificaci´on:
 problema productoria (s: seq⟨Z⟩) : Z {
 requiere: { True }
 asegura: { resultado = |s|−1
 i=0 s[i] }
 }
-}

{-
 3. maximo :: [Integer]-> Integer seg´un la siguiente especificaci´on:
 problema maximo (s: seq⟨Z⟩) : Z {
 requiere: { |s| > 0 }
 asegura: { resultado ∈ s ∧ todo elemento de s es menor o igual a resultado }
 }
-}

{-
 4. sumarN :: Integer-> [Integer]-> [Integer] seg´un la siguiente especificaci´on:
 problema sumarN (n: Z, s: seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: { True }
 asegura: {|resultado| = |s| ∧ cada posici´on de resultado contiene el valor que hay en esa posici´on en s sumado
 n }
 }
-}

{-
5. sumarElPrimero :: [Integer]-> [Integer] seg´un la siguiente especificaci´on:
 problema sumarElPrimero (s: seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: { |s| > 0 }
 asegura: {resultado = sumarN(s[0],s) }
 }
 Por ejemplo sumarElPrimero [1,2,3] da [2,3,4]
-}

{-
 6. sumarElUltimo :: [Integer]-> [Integer] seg´un la siguiente especificaci´on:
 problema sumarElUltimo (s: seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: { |s| > 0 }
 asegura: {resultado = sumarN(s[|s| − 1],s) }
 }
 Por ejemplo sumarElUltimo [1,2,3] da [4,5,6]
-}

{-
 7. pares :: [Integer]-> [Integer] seg´un la siguiente especificaci´on:
 problema pares (s: seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: { True }
 asegura: {resultado s´olo tiene los elementos pares de s en el orden dado, respetando las repeticiones}
 }
 Por ejemplo pares [1,2,3,5,8,2] da [2,8,2]
}
-}

{-
 8. multiplosDeN :: Integer-> [Integer]-> [Integer] que dado un n´umero n y una lista xs, devuelve una lista
 con los elementos de xs m´ultiplos de n.
 9. ordenar :: [Integer]-> [Integer] que ordena los elementos de la lista en forma creciente. Sugerencia: Pensar
 c´omo pueden usar la funci´on m´aximo para que ayude a generar la lista ordenada necesaria.
-}