{-
Implementar la funci´on esFibonacci :: Integer->Bool seg´un la siguiente especificaci´on:
 problema esFibonacci (n: Z) : B {
 requiere: { n ≥ 0 }
 asegura: { resultado = true ↔ n es alg´un valor de la secuencia de Fibonacci definida en el ejercicio 1}
 }
-}
esFibonnacci :: Int -> Bool
esFibonnacci n = fibonacciModificado n 1 

--ejer 1
fibonacci :: Int -> Int
fibonacci n | n == 0 = 0
            | n == 1 = 1
            | otherwise = fibonacci(n-1) + fibonacci(n-2)
--
fibonacciModificado :: Int ->Int -> Bool --verifica si fibonnacci i llega a estar en n
fibonacciModificado n  i | (fibonacci i) < n = fibonacciModificado n (i+1)
                         | (fibonacci i) == n = True
                         | otherwise = False 