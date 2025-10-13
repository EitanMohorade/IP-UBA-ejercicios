{-
 Implementar una funci´on parteEntera :: Float->Integer seg´un la siguiente especificaci´on:
 problema parteEntera (x: R) : Z {
 requiere: { x ≥ 0 }
 asegura: { resultado ≤ x < resultado+1 }
 }
-}
parteEntera :: Float -> Int
parteEntera n | n < 1 = 0
              | otherwise = 1 + parteEntera(n-1)