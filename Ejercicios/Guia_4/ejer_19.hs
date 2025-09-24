{-
 Implementar la funci´on esSumaInicialDePrimos :: Integer->Bool seg´un la siguiente especificaci´on:
 problema esSumaInicialDePrimos (n: Z) : B {
 requiere: { n ≥ 0 }
 asegura: { resultado = true ↔ n es igual a la suma de los m primeros n´umeros primos, para alg´un m.}
 }
-}
esSumaInicialDePrimos :: Int -> Bool
esSumaInicialDePrimos n = auxiliar n 1

auxiliar :: Int -> Int -> Bool
auxiliar n i | (sumarNprimos i 1) > n = False
             | (sumarNprimos i 1) == n = True
             | otherwise = auxiliar n (i+1)

sumarNprimos :: Int -> Int -> Int 
sumarNprimos n i | (esPrimo i) == False = sumarNprimos n (i+1)
                 | n < 1 = 0
                 | n == i = i
                 | i > n = 0
                 |otherwise = 1 + sumarNprimos n (i+1)

menorDivisor :: Int -> Int
menorDivisor 1 = 1
menorDivisor n = divisoresDesde n 2

divisoresDesde :: Int -> Int -> Int
divisoresDesde n i | mod n i == 0 = i
                   |  otherwise = divisoresDesde n (i+1)

esPrimo :: Int->Bool
esPrimo 1 = False
esPrimo n = (menorDivisor n) == n