{-
 Implementar una funci´on sumaRacionales :: Int->Int->Float que dados dos naturales n,m
 sume todos los n´umeros racionales de la forma p/q con 1 ≤ p ≤ n y 1 ≤ q ≤ m, es decir:
 problema sumaRacionales (n : N, m : N) : R {
 requiere: { True}
 n
 asegura: { resultado =
 }
 p=1
 m
 q=1
 p
 q }
-}

sumaRacionales :: Int->Int->Float --suma todas las sumatorias desde m=1 hasta n  de 1/m
sumaRacionales n 0 = 0
sumaRacionales n m = (sumatoriaInterna n m) + sumaRacionales n (m-1) 

--auxiliar
sumatoriaInterna :: Int -> Int -> Float-- suma la sumatoria desde i=1 hasta m de i/m
sumatoriaInterna 1 i = (1 / fromIntegral(i)) 
sumatoriaInterna 0 i = 0
sumatoriaInterna m 0 = 1
sumatoriaInterna m i = (sumatoriaInterna (m-1) i) + (fromIntegral(m) / fromIntegral(i)) 
--