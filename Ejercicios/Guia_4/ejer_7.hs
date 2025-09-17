{-
 Implementar la funci´on iesimoDigito :: Integer->Integer->Integer que dado un n ∈ Z mayor o igual
 a 0 y un i∈Z mayor o igual a 1 y menor o igual a la cantidad de d´ıgitos de n, devuelve el i-´esimo d´ıgito de n.
 problema iesimoDigito (n: Z, i: Z) : Z {
 requiere: { n ≥ 0∧1 ≤i ≤cantDigitos(n) }
 asegura: { resultado = (n div 10cantDigitos(n)−i) mod 10 }
 }

problema cantDigitos (n: Z) : N {
 requiere: { n ≥ 0 }
 asegura: { n = 0 →resultado = 1}
 asegura: { n̸ = 0 →(n div 10resultado−1 > 0∧n div 10resultado = 0) }
 }

-}