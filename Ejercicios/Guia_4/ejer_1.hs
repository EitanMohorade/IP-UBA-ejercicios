{-
Implementar la funci´on fibonacci:: Integer->Integer que devuelve el i-´esimo n´umero de Fibonacci.
 Recordar que la secuencia de Fibonacci se define como:
 problema fibonacci (n: Z) : Z {
 requiere: { n ≥ 0 }
 asegura: { resultado = fib(n) }
 }
-}
fibonacci :: Int -> Int
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)