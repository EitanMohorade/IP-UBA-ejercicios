{-
 a) Especificar e implementar una funci´on eAprox :: Integer->Float que aproxime el valor del n´umero e
 a partir de la siguiente sumatoria:
 n
 ˆ
 e(n) =
 i=0
 1
 i!
 b) Definir la constante e :: Float como la aproximaci´on de e a partir de los primeros 10 t´erminos de la serie anterior.
 ¡Atenci´on! A veces ciertas funciones esperan un Float y nosotros tenemos un Int. Para estos casos podemos utilizar la
 funci´on fromIntegral :: Int->Float definida en el Preludio de Haskell.
-}
{-a
problema esAprox (n: Z) : R {
 requiere: {n >= 0}
 asegura: {resultado es la sumatoria de i=0 hasta n de 1 sobre i factorial}
-}

eAprox :: Int -> Float
eAprox 0 = 1
eAprox n = (1 / (deIntAFloat(factorial n))) + eAprox (n-1)
--auxiliar
factorial :: Int -> Int
factorial n | n <= 1 =1
            | otherwise = n * factorial(n-1)
deIntAFloat :: Int -> Float
deIntAFloat n | n == 1 = 1.0
              | n == 0 = 0.0
              | otherwise = (deIntAFloat (n-1)) + 1.0
--

--b
e :: Float
e = eAprox 10