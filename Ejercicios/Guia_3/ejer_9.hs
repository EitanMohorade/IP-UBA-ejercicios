{-
A partir de las siguientes implementaciones en Haskell, describir en lenguaje natural qu´e hacen y especificarlas.
a) f1 :: Float-> Float
f1 n | n == 0 = 1
     | otherwise = 0

     
Especificacion: 
 problema f () :  {
    requiere: {}
    asegura: {}
 }
-}

{-
b) f2 :: Float-> Float
f2 n | n == 1 = 15
     | n ==-1 =-15

Especificacion: 
 problema f () :  {
    requiere: {}
    asegura: {}
 }
-}

{-
c) f3 :: Float-> Float
f3 n | n <= 9 = 7
     | n >= 3 = 5

Especificacion: 
 problema f () :  {
    requiere: {}
    asegura: {}
 }
-}

{- 
d) f4 :: Float-> Float-> Float
f4 x y = (x+y)/2

Especificacion: 
 problema f () :  {
    requiere: {}
    asegura: {}
 }
-}

{-
e) f5 :: (Float, Float)-> Float
f5 (x, y) = (x+y)/2


Especificacion: 
 problema f () :  {
    requiere: {}
    asegura: {}
 }
-}

{-
f) f6 :: Float-> Int-> Bool
f6 a b = truncate a == b


Especificacion: 
 problema f () :  {
    requiere: {}
    asegura: {}
 }
-}