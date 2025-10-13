{-
 Especificar e implementar la funci´on sumaDigitos :: Integer->Integer que calcula la suma de d´ıgitos de
 un n´umero natural. Para esta funci´on pueden utilizar div y mod.
-}

sumaDigitos :: Int -> Int
sumaDigitos n | cantidadDeDigitos n == 1 = n
              | otherwise = digitoUnidades n + sumaDigitos (div n 10)

digitoUnidades :: Int -> Int
digitoUnidades n = mod n 10
cantidadDeDigitos :: Int -> Int
cantidadDeDigitos n | n < 10 = 1
                    | otherwise = cantidadDeDigitos(div n 10) + 1