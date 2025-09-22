{-
Recordemos que un entero p > 1 es primo si y s´olo si no existe un entero k tal que 1 < k < p y k divida a p.
a) Implementar menorDivisor :: Int->Int que calcule el menor divisor (mayor que 1) de un natural n pasado
como par´ametro.
-}
menorDivisor :: Int->Int
menorDivisor n = divisoresDesde n 2

--auxiliar
divisoresDesde :: Int-> Int-> Int --funcion que devuelve el primer divisor de n desde i
divisoresDesde n i | mod n i == 0 = i
                   | otherwise = divisoresDesde n (i+1)
--
{-
b) Implementar la funci´on esPrimo :: Int->Bool que indica si un n´umero natural pasado como par´ametro es primo.
-}
esPrimo :: Int->Bool
esPrimo n = (menorDivisor n) == n

{-
c) Implementar la funci´on sonCoprimos :: Int->Int->Bool que dados dos n´umeros naturales indica si no
tienen alg´un divisor en com´un mayor estricto que 1.
-}
sonCoprimos :: Int->Int->Bool
sonCoprimos n m | mod (head (agregarDivisores n 2 [])) m == 0 = True --verifica si el primer elem de la lista de divisores de n divide a m
                | otherwise = sonCoprimos (head (tail (agregarDivisores n 1 []))) m --elimina el elemento que el paso anterior no lo dividio y pasa por el siguiente

--auxiliar
agregarDivisores :: Int -> Int -> [Int] -> [Int]
agregarDivisores n i lista |(mod n i == 0) = agregarDivisores n (i+1) (i : lista) --agrega a i si la division entre n y i da resto 0
                           | i > n = lista --devuelve lista si i ya es mayor a n
                           | otherwise = agregarDivisores n (i+1)  lista --si llega aca es pq i no da resto 0, por lo q prueba i+1
--
{-
d) Implementar la funci´on nEsimoPrimo :: Int->Int que devuelve el n-´esimo primo (n ≥ 1). Recordar que el
primer primo es el 2, el segundo es el 3, el tercero es el 5, etc
-}
nEsimoPrimo :: Int->Int
nEsimoPrimo n = generarNprimos n 2 []

generarNprimos ::  Int ->Int-> [Int]-> Int
generarNprimos n i lista | longitud(lista) == n = head(lista) --verifica si la longitud de la lista es igual al numero de primos que se pidieron (n)
                         | (esPrimo i) = generarNprimos n (i+1) (i : lista) --agrega el i primo si no se cumple lo de arriba
                         | otherwise = (generarNprimos n (i+1) lista)  --prueba con el siguiente numero si no era primo el i
{-
generarPrimosHasta :: Int ->Int-> [Int]-> [Int]
generarPrimosHasta n i lista| (esPrimo i) = generarPrimosHasta n (i+1) (i : lista)
                            | n <= i = lista
                            | otherwise = generarPrimosHasta n (i+1) lista
-}
--auxiliar longitud
longitud :: [Int] -> Int
longitud [] = 0
longitud lista = 1 + longitud (tail(lista)) 