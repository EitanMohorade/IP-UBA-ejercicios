{-
 Especificar e implementar una funci´on esCapicua :: Integer->Bool que dado n ∈ N≥0 determina si n es
 un n´umero capic´ua.
-}
esCapicua :: Int -> Bool
esCapicua n | concatenarNumero (revertir ((devuelveOtraMitad n))) (revertir((devuelveMitad n))) == n = True
            | otherwise = False

--auxiliares 

--para devolver extremos del numero
devuelveMitad :: Int -> Int --los ultimos digitos (y en impar si el numero es impar)
devuelveMitad n | mod (cantidadDeDigitos n ) 2 == 0 = div n (10^div (cantidadDeDigitos n) 2)
                | otherwise = div n (10^div (cantidadDeDigitos n) 2)

devuelveOtraMitad :: Int -> Int --los primeros digitos (y en par si el numero es impar)
devuelveOtraMitad n | mod (cantidadDeDigitos n ) 2 == 0  = mod n (10^div (cantidadDeDigitos n) 2)
                    | otherwise = mod n (10^(div (cantidadDeDigitos n) 2))
--
--poner izquierda a derecha los numeros
revertir :: Int -> Int
revertir n | cantidadDeDigitos n == 1 = digitoUnidades n
           | otherwise =  concatenarNumero (digitoUnidades n) (revertir (div n 10))
--
cantidadDeDigitos :: Int -> Int
cantidadDeDigitos n | n < 10 = 1
                    | otherwise = 1 + cantidadDeDigitos (div n 10)

concatenarNumero :: Int -> Int -> Int --FALLA SI B TIENE DIGITOS EN 0 ADELANTE, EJEMPLO: 12 02 /= 1202 SINO QUE ES 122
concatenarNumero a b = a * 10 ^ cantidadDeDigitos b + b
  --                   | otherwise = a * 10 ^ (cantidadDeDigitos a - (cantidadDeDigitos b)+1) + b

digitoUnidades :: Int -> Int
digitoUnidades n = mod n 10
--
