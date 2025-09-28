
{-
 a) Definir las siguientes funciones sobre listas de caracteres, interpretando una palabra como una secuencia de
 caracteres sin blancos:
 a) sacarBlancosRepetidos :: [Char]-> [Char], que reemplaza cada subsecuencia de blancos contiguos de la pri
mera lista por un solo blanco en la lista resultado.

 b) contarPalabras :: [Char]-> Integer, que dada una lista de caracteres devuelve la cantidad de palabras que
 tiene.

 c) palabras :: [Char]-> [[Char]], que dada una lista arma una nueva lista con las palabras de la lista original.

 d) palabraMasLarga :: [Char]-> [Char], que dada una lista de caracteres devuelve su palabra m´as larga.

 e) aplanar :: [[Char]]-> [Char], que a partir de una lista de palabras arma una lista de caracteres concaten´ando
las.

 f ) aplanarConBlancos :: [[Char]]-> [Char], que a partir de una lista de palabras, arma una lista de caracteres
 concaten´andolas e insertando un blanco entre cada palabra.

 g) aplanarConNBlancos :: [[Char]]-> Integer-> [Char], que a partir de una lista de palabras y un entero n,
 arma una lista de caracteres concaten´andolas e insertando n blancos entre cada palabra (n debe ser no negativo).

 b) ¿C´omo cambian los ejercicios si agregamos el renombre de tipos: type Texto = [Char]?
 -}
type Texto = [Char]

contarPalabras :: Texto -> Int
contarPalabras [] = 0
contarPalabras [' '] = 0
contarPalabras [x] = 1
contarPalabras (x:y:xs) | x /= ' ' && y == ' ' = 1 + contarPalabras xs
                        | otherwise = contarPalabras (y:xs)
palabra :: Texto -> [Texto]
palabra [] = []
palabra [' '] = []
palabra [x] = [[x]]
palabra (x:xs) | x /= ' ' = primeraPalabra (x:xs) : (palabra (quitarPalabra (x:xs)))

--auxuliar
primeraPalabra :: Texto -> Texto
primeraPalabra (x:xs) |   x /= ' ' = x : primeraPalabra xs
                      | otherwise = []
quitarPalabra :: Texto -> Texto
quitarPalabra (x:xs) | x /= ' ' = quitarPalabra xs
                     | otherwise = xs
--