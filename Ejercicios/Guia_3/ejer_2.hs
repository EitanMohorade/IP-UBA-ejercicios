{-
    Especificar e implementar las siguientes funciones, incluyendo su signatura.
    a) absoluto: calcula el valor absoluto de un n´umero entero.
-}
{-
Especificacion: 
 problema absoluto (n: Z) : Z {
    requiere: {true}
    asegura: {resultado es n en positivo}
 }
-}
absoluto :: Integer -> Integer
absoluto n  | n >= 0 = n
            | otherwise = n * (-1)
{-
    b) maximoAbsoluto: devuelve el m´aximo entre el valor absoluto de dos n´umeros enteros.
-}

{-
Especificacion: 
 problema maximoAbsoluto (a: Z, b: Z) : Z {
    requiere: {a y b deben ser distintos}
    asegura: {resultado es el mayor entre el resultado de aplicar funcion 'absoluto' a 'a' y 'b'}
 }
-}
maximoAbsoluto :: Integer -> Integer -> Integer 
maximoAbsoluto a b = max (absoluto a) (absoluto b)
{-
    c) maximo3: devuelve el m´aximo entre tres n´umeros enteros.
-}

{-
Especificacion: 
 problema maximo3 (a: Z, b: Z, c: Z) : Z {
    requiere: {true}
    asegura: {resultado es el maximo entre 'a', 'b' y 'c'}
 }
-}
maximo3 :: Integer -> Integer -> Integer -> Integer
maximo3 a b c = maximoAbsoluto c (maximoAbsoluto a b)
{-
    d) algunoEsCero: dados dos n´umeros racionales, decide si alguno es igual a 0 (resolverlo con y sin pattern matching).
-}

{-
    Especificacion: 
    problema algunoEsCero (a: Q, b: Q) :  {
        requiere: {true}
        asegura: {resultado decide si porlomenos 'a' o 'b' es 0}
 }
-}

--con pattern matching
algunoEsCeroV1 :: Integer -> Integer -> Bool
algunoEsCeroV1 a 0 = True
algunoEsCeroV1 0 b = True
algunoEsCeroV1 a b = False 

--sin pattern matching

algunoEsCeroV2 :: Integer -> Integer -> Bool
algunoEsCeroV2 a b 
    | a == 0 = True
    | b == 0 = True
    | otherwise = False

{-
    e) ambosSonCero: dados dos n´umeros racionales, decide si ambos son iguales a 0 (resolverlo con y sin pattern matching).
-}

{-
Especificacion: 
 problema ambosSonCero (a: Q, b: Q) : Bool  {
    requiere: {true}
    asegura: {resultado decide si  'a' y 'b' son 0 }
 }
-}

--con pattern matching
ambosSonCeroV1 :: Integer -> Integer -> Bool
ambosSonCeroV1 0 0 = True
ambosSonCeroV1 a b = False

--sin pattern matching

ambosSonCeroV2 :: Integer -> Integer -> Bool
ambosSonCeroV2 a b 
    | a == 0 && b == 0 = True
    | otherwise = False


{-
    f) enMismoIntervalo: dados dos n´umeros reales, indica si est´an relacionados por la relaci´on de equivalencia en R cuyas
    clases de equivalencia son: (−∞,3],(3,7] y (7,∞), o dicho de otra manera, si pertenecen al mismo intervalo.
-}

{-
Especificacion: 
 problema enMismoInvervalo (a: R, b: R) : Bool  {
    requiere: {true}
    asegura: {resultado decide si 'a' y 'b' pertenecen ambos en alguno de los intervalos (−∞,3],(3,7] y (7,∞) al mismo tiempo}
 }
-}

enMismoIntervalo :: Integer -> Integer -> Bool
enMismoIntervalo a b
                    | a <= 3 && b <= 3 = True 
                    | a > 7 && b > 7 = True
                    | (a > 3 && a <= 7) && (b > 3 && b <= 7) = True
                    | otherwise = False

{-
    g) sumaDistintos: que dados tres n´umeros enteros calcule la suma sin sumar repetidos (si los hubiera).
-}

{-
Especificacion: 
 problema sumaDistintos (a: Z, b: Z, c: Z) : Z {
    requiere: {no hay numeros repetidos}
    asegura: {resultado es la suma entre 'a' 'b' y 'c'}
 }
-}

sumaDistintos :: Integer -> Integer -> Integer -> Integer
sumaDistintos a b c = a + b + c 
{-
    h) esMultiploDe: dados dos n´umeros naturales, decide si el primero es m´ultiplo del segundo.
-}


{-
Especificacion: 
 problema esMultiploDe (a: N, b: N) : Bool  {
    requiere: {true}
    asegura: {resultado decide si 'a' es multiplo de 'b'}
 }
-}

esMultiploDe :: Integer -> Integer -> Bool
esMultiploDe a b
                | rem b a == 0 = True
                | otherwise = False
{-
    i) digitoUnidades: dado un n´umero entero, extrae su d´ıgito de las unidades.
-}

{-
Especificacion: 
 problema digitoUnidades (n: Z) : Z {
    requiere: {true}
    asegura: {resultado es el digito de la unidad de n}
 }
-}

digitoUnidades :: Integer -> Integer
digitoUnidades a = absoluto(a `mod` 10)

{-
    j) digitoDecenas: dado un n´umero entero mayor a 9, extrae su d´ıgito de las decenas.
-}

{-
Especificacion: 
 problema digitoDecenas (n: Z) : Z {
    requiere: {n debe ser mayor estricto a 9}
    asegura: {resultado es el digito de las decenas de n}
 }
-}

digitoDecenas :: Integer -> Integer
digitoDecenas a = absoluto((a  `div` 10)  `mod` 10)