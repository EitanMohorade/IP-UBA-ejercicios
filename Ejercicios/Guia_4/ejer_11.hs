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