{-
 Especificar, implementar y dar el tipo de las siguientes funciones (s´ımil Ejercicio 4 Pr´actica 2 de ´ Algebra 1).
 n
 a) f1(n) =
 i=0
 b) f2(n,q) =
 2n
 2i, n ∈ N0.
 n
 i=1
 qi, n ∈ N y q ∈R
 c) f3(n,q) =
 d) f4(n,q) =
 i=1
 2n
 i=n
 qi, n ∈ N0 y q ∈R
 qi, n ∈ N0 y q ∈R
-}

{-a
problema f1 (n: Z) : Z {
 requiere: {n >= 0}
 asegura: {resultado es la sumatoria de i=0 hasta n de 2^i}
-}
f1 :: Int -> Int
f1 n = f1A (n+1) 
--auxiliar
f1A :: Int -> Int
f1A n | n == 0 = 0
      | otherwise = (2^(n-1)) + f1A (n-1) 
--

{-b
problema f2 (n: Z, q: R) : R {
 requiere: {n > 0}
 asegura: {resultado es la sumatoria de i=1 hasta n de q^i}
-}
f2 :: Int -> Float -> Float
f2 n q = qElevadoAlN (n+1) q

{-c
problema f2 (n: Z, q: R) : R {
 requiere: {n >= 0}
 asegura: {resultado es la sumatoria de i=1 hasta 2*n de q^i}
-}
f3 :: Int -> Float -> Float
f3 n q = (qElevadoAlN (2*n) q) + (q^(2*n))

{-d
problema f2 (n: Z, q: R) : R {
 requiere: {n >= 0}
 asegura: {resultado es la sumatoria de i=n hasta 2*n de q^i}
-}
f4 :: Int -> Float -> Float
f4 n q = (qElevadoAlN (2*n) q) + (q^(2*n)) - (qElevadoAlN n q) 


--
-- auxiliar
qElevadoAlN :: Int -> Float -> Float
qElevadoAlN n q |  n == 1 = 0
       | otherwise = (q^(n-1)) + qElevadoAlN (n-1) q
--