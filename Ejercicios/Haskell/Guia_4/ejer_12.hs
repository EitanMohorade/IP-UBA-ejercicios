{-
 Para n ∈ N se define la sucesi´on:
 an =2+
 1
 1
 2 +
 . . .
 2 + 1
 2 + 1
 2
 (aparece n veces el 2).
 Lo cual resulta en la siguiente definici´on recursiva: a1 = 2,an = 2+ 1
 an−1
 . Utilizando esta sucesi´on, especificar e implementar
 una funci´on raizDe2Aprox :: Integer->Float que dado n ∈ N devuelva la aproximaci´on de √2 definida por √2 ≈ an−1.
 Por ejemplo:
 raizDe2Aprox 1 ⇝ 1
 raizDe2Aprox 2 ⇝ 1,5
 raizDe2Aprox 3 ⇝ 1,4
-}

{-especificacion
problema raizDe2Aprox(n:Z) R {
    requiere:{n > 0}
    asegura:{resultado devuelve la aproximacion de raiz de dos definida por raiz de dos casi igual a la sucesion-1}
}
-}

raizDe2Aprox :: Int -> Float
raizDe2Aprox n = (sucesion n)-1

sucesion :: Int -> Float
sucesion n | n == 1 = 2
           | otherwise = 2 + (1 / sucesion (n-1) )