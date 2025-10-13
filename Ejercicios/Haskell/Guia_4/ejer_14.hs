{-
 Especificar e implementar una funci´on sumaPotencias :: Int->Int->Int->Int que
 dados tres naturales q,n,m sume todas las potencias de la forma qa+b con 1 ≤ a ≤ n y 1 ≤ b ≤ m.
-}

{-especificar
problema sumaPotencias(q: Z, n: Z, m: Z){
    requiere: {q, n y m > 0}
    asegura: {resultado es la suma de todas las potencias de la forma q^a+b con 1 ≤ a ≤ n y 1 ≤ b ≤ m}
}
-}

sumaPotenciasV1 :: Int->Int->Int->Int--suma las posibles q^a+b con  1 ≤ a ≤ n y 1 ≤ b ≤ m sin repetirse
sumaPotenciasV1 q n m | (q^(absoluto(n+m))) == (q^2) = (q^(absoluto(n+m))) 
                    | otherwise = (sumaPotenciasV1 q (n-1) m) + (q^(absoluto(n+m)))
--auxiliar
absoluto :: Int -> Int
absoluto n | n < 0 = n * (-1)
           | otherwise = n
--
sumaPotenciasV2 :: Int->Int->Int->Int-- suma la sumatoria desde a=1 hasta n de la sumatoria desde b=1 hasta m de q elevado a a+b
sumaPotenciasV2 q 0 m = 0
sumaPotenciasV2 q n m = (sumaPotenciasV2 q (n-1) m) + ((sumatoriaInterna m q) * q^n)

--auxiliar
sumatoriaInterna :: Int -> Int -> Int-- suma la sumatoria desde i=1 hasta m de m elevado a i
sumatoriaInterna 1 i = i
sumatoriaInterna 0 i = 0
sumatoriaInterna m 0 = 1
sumatoriaInterna m i = (sumatoriaInterna (m-1) i) + i^m   
--