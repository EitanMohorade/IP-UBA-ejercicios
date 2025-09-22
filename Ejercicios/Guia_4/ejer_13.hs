{-
Especificar e implementar la siguiente funci´on:
 f(n,m) =
 n
 i=1
 m
 j=1
 
-}

{-especificacion
problema dobleSumatoria (n: Z, m: Z) Z{
    requiere: {n y m > 0}
    asegura: {resultado es la sumatoria de i=1 hasta n de la sumatoria de j = 1 hasta m de i elevado a la j}
}
-}

dobleSumatoria :: Int -> Int -> Int
dobleSumatoria n m | n == 0 || m == 0 = 0
                   | otherwise = (sumatoriaInterna m n) + dobleSumatoria (n-1) m

sumatoriaInterna :: Int -> Int -> Int
sumatoriaInterna 1 i = i
sumatoriaInterna 0 i = 0
sumatoriaInterna m 0 = 1
sumatoriaInterna m i = (sumatoriaInterna (m-1) i) + i^m   
