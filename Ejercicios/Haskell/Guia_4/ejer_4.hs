{-
 Especificar e implementar la funci´on sumaImpares :: Integer->Integer que dado n ∈ N sume los primeros
 n n´umeros impares. Por ejemplo: sumaImpares 3 
1+3+5 ⇝ 9.
-}
sumaImpares :: Int -> Int
sumaImpares n | mod n 2 == 0 = (n+1) + (n-1)
              | otherwise = sumaImpares (n-1) + n + 2