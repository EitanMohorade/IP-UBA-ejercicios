{-
a) Implementar la funci´on:
distanciaManhattan:: (Float, Float, Float)-> (Float, Float, Float)-> Float
problema distanciaManhattan (p : R×R×R,q : R×R×R) : R {
requiere: {True}
asegura: {res = sumatoria desde i=0 a n=2 de |pi-qi|}
}
Por ejemplo:
distanciaManhattan (2, 3, 4) (7, 3, 8) ⇝ 9
distanciaManhattan ((-1), 0, (-8.5)) (3.3, 4, (-4)) ⇝ 12.8
-}

{-
b) Reimplementar la funci´on teniendo en cuenta el siguiente tipo: type Punto3D = (Float, Float, Float)
-}
--funcion auxiliar
absoluto :: (Num a, Ord a)=> a -> a
absoluto n  | n >= 0 = n
            | otherwise = n * (-1)
--

--punto a
distanciaManhattanV1 :: (Float, Float, Float) -> (Float, Float, Float) -> Float
distanciaManhattanV1  (x1, y1, z1) (x2, y2, z2) = absoluto (x1 - x2) + absoluto (y1 - y2) + absoluto (z1 - z2) 

--punto b
type Punto3D = (Float, Float, Float)
distanciaManhattanV2 :: Punto3D -> Punto3D -> Float
distanciaManhattanV2  (x1, y1, z1) (x2, y2, z2) = absoluto (x1 - x2) + absoluto (y1 - y2) + absoluto (z1 - z2) 