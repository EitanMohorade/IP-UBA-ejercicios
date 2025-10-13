
-- Ejercicio 1
cantidadNumerosAbundantes :: Integer -> Integer -> Integer
--cantidadNumerosAbundantes _ _ = 0
cantidadNumerosAbundantes d h | d > h = 0 
                              | numeroAbundante h = 1 + cantidadNumerosAbundantes d (h-1)
                              | otherwise = cantidadNumerosAbundantes d (h-1)

--auxiliar
numeroAbundante :: Integer -> Bool
numeroAbundante n | sumarNumerosEnLista (divisoresDesde n 1)  > n = True
                  | otherwise = False

divisoresDesde :: Integer -> Integer -> [Integer]
divisoresDesde n i | n == i = []
                   | mod n i == 0 = i : divisoresDesde n (i+1)
                   | otherwise = divisoresDesde n (i+1)

sumarNumerosEnLista :: [Integer] -> Integer
sumarNumerosEnLista [] = 0
sumarNumerosEnLista (x:xs) = x + sumarNumerosEnLista xs
--

-- Ejercicio 2
type Cursadas = [(Nombre, Anio, Cuatrimestre)]
type Nombre = String
type Anio = Integer
type Cuatrimestre = Integer --0 es curso de verano 

cursadasVencidas :: [(String, Integer, Integer)] -> [String]
--cursadasVencidas _ = []
cursadasVencidas [] = []
cursadasVencidas ((nombre, anio, cuatri):cs) | anio < 2021 = nombre : eliminarRepetidos(cursadasVencidas cs)
                                             | anio == 2021 && cuatri < 2 = nombre : eliminarRepetidos(cursadasVencidas cs)
                                             | otherwise = eliminarRepetidos (cursadasVencidas cs)
--auxiliar
eliminarRepetidos :: [String] -> [String]
eliminarRepetidos [x] = [x]
eliminarRepetidos [] = []
eliminarRepetidos (x:xs) = x : eliminarRepetidos (eliminarUnoRepetido xs x)


eliminarUnoRepetido :: [String] -> String -> [String]
eliminarUnoRepetido [] _ = []
eliminarUnoRepetido (x:xs) y | x == y = eliminarUnoRepetido xs y
                             | otherwise = x : eliminarUnoRepetido xs y
--

-- Ejercicio 3
saturarEnUmbralHastaNegativo :: [Integer] -> Integer -> [Integer]
--saturarEnUmbralHastaNegativo _ _ = []
saturarEnUmbralHastaNegativo [] y = [] 
saturarEnUmbralHastaNegativo (x:xs) y | x < 0 = []
                                      | x <= y   = x : saturarEnUmbralHastaNegativo xs y
                                      | otherwise = y : saturarEnUmbralHastaNegativo xs y

-- Ejercicio 4
cantidadParesColumna :: [[Integer]] -> Integer -> Integer
--cantidadParesColumna _ _ = 0
cantidadParesColumna [] _ = 0
cantidadParesColumna (x:xs) n = (parEnColumna x n) + cantidadParesColumna xs n 

--auxiliar
parEnColumna :: [Integer] -> Integer -> Integer
parEnColumna [] _ = 0
parEnColumna (x:xs) y | (y == 1) && (mod x 2 == 0) = 1
                      | otherwise = parEnColumna xs (y-1)

longitud :: [Integer] -> Integer
longitud [] = 0
longitud (x:xs) = 1 + longitud xs
--