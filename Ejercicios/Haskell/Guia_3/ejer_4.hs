{-
Especificar e implementar las siguientes funciones utilizando tuplas para representar pares y ternas de
 n´umeros.
a) productoInterno: calcula el producto interno entre dos tuplas de R × R.
-}

{-
Especificacion: 
 problema productoInterno (a: (R), b: (R)) : R  {
    requiere: {'a' y 'b' tienen la misma longitud}
    requiere: {'a' y 'b' sean pares o ternas de numeros}
    asegura: {resultado es el producto de 'a' por 'b' entre todos sus elementos}
 }
-}
--con duplas
productoInternoV1 :: (Integer, Integer) -> (Integer, Integer) -> Integer
productoInternoV1 (a, b) (c, d) = a * b * c * d
--con ternas
productoInternoV2 :: (Integer, Integer, Integer) -> (Integer,Integer , Integer) -> Integer
productoInternoV2 (a, b, c) (d, f, g) = a * b * c * d * f * g 

{-
c) distancia: calcula la distancia eucl´ıdea entre dos puntos de R2.
-}

{-
Especificacion: 
 problema distancia (a: (R, R), b: (R, R)) : R  {
    requiere: {true}
    asegura: {resultado es la distancia entre los puntos a y b de un plano cartesiano}
 }
-}
distancia :: (Double, Double) -> (Double, Double) -> Double
distancia (a, b) (c, d) = sqrt (((c-a)^2) + ((d-b)^2))

{-
d) sumaTerna: dada una terna de enteros, calcula la suma de sus tres elementos.
-}

{-
Especificacion: 
 problema sumaTerna (a: (Z, Z, Z)) : Z  {
    requiere: {true}
    asegura: {resultado es la suma de los elementos de 'a'}
 }
-}
sumaTerna :: (Integer, Integer, Integer) -> Integer
sumaTerna (a, b, c) = a+b+c

{-
g) crearPar :: a-> b-> (a, b): a partir de dos componentes, crea un par con esos valores. Debe funcionar para ele
mentos de cualquier tipo.
-}

{-
Especificacion: 
 problema crearPar (a, b) : (a, b)  {
    requiere: {deben ser elementos de cualquier tipo}
    asegura: {resultado es tupla con solo los elementos 'a' y 'b'}
 }
-}
crearPar :: a-> b-> (a, b)
crearPar a b = (a, b)
{-
h) invertir :: (a, b)-> (b, a): invierte los elementos del par pasado como par´ametro. Debe funcionar para elementos
de cualquier tipo.
-}

{-
Especificacion: 
 problema invertir (t: (a, b)) : (b, a)  {
    requiere: {deben ser elementos de cualquier tipo}
 }
-}
invertir :: (a, b)-> (b, a)
invertir (a, b) = (b, a)

{-
i) Reescribir los ejercicios productoInterno, esParMenor y distancia usando el siguiente renombre de tipos:
type Punto2D = (Float, Float)
-}

{-
Especificacion: 
 problema a () :   {
    requiere: {}
    asegura: {}
 }
-}