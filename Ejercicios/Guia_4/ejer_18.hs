{-
Implementar una funci´on mayorDigitoPar :: Integer->Integer seg´un la siguiente especificaci´on:
 problema mayorDigitoPar (n: N) : N {
 requiere: { True }
 asegura: { resultado es el mayor de los d´ıgitos pares de n. Si n no tiene ning´un d´ıgito par, entonces resultado es-1.
 }
 }
-}
mayorDigitoPar :: Int -> Int
mayorDigitoPar n | head (digitosPares n []) == (-1) = (-1) 
                 | head (digitosPares n []) >= head (tail (digitosPares n [])) = mayorDigitoPar (mod n (10^((cantidadDeDigitos n)-1)))
                 | head (digitosPares n []) < head (tail (digitosPares n [])) = head (tail (digitosPares n []))

digitosPares :: Int -> [Int] -> [Int]
digitosPares n lista | n < 10 && (mod n 2 == 0) = (n : lista)
                     | n < 10 && ((longitud lista) == 0) = ((-1) : lista) 
                     | n < 10 = lista
                     | (mod (div n (10^((cantidadDeDigitos n)-1))) 2) == 0 = digitosPares (mod n (10^((cantidadDeDigitos n)-1)) )  ((div n (10^((cantidadDeDigitos n)-1))) : lista)
                     | otherwise =  digitosPares (mod n (10^((cantidadDeDigitos n)-1)) ) lista

longitud :: [Int] -> Int
longitud [] = 0
longitud lista = 1 + longitud (tail(lista))

cantidadDeDigitos :: Int -> Int
cantidadDeDigitos n | n < 10 = 1
                    | otherwise = 1 + cantidadDeDigitos (div n 10)