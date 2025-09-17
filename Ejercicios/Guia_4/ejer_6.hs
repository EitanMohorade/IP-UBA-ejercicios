{-
 Implementar la funci´on todosDigitosIguales :: Integer->Bool que determina si todos los d´ıgitos de un
 n´umero natural son iguales, es decir:
 problema todosDigitosIguales (n: Z) : B {
 requiere: { n > 0 }
 asegura: { resultado = true ↔ todos los d´ıgitos de n son iguales }
 }
-}
todosDigitosIguales :: Int -> Bool
todosDigitosIguales n | n < 10 = True
                      |otherwise = digitoUnidades n == digitoUnidades (div n 10) && todosDigitosIguales(div n 10)

digitoUnidades :: Int -> Int
digitoUnidades n = mod n 10


