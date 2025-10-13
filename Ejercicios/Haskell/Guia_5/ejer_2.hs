{-
Definir las siguientes funciones sobre listas:
 1. pertenece :: (Eq t) => t-> [t]-> Bool seg´un la siguiente especificaci´on:
 problema pertenece (e: T, s: seq⟨T⟩) : B {
 requiere: { True }
 asegura: { resultado = true ↔ e ∈ s }
 }
 -}
pertenece :: (Eq t) =>t -> [t] -> Bool
pertenece _ [] = False
pertenece e (x:xs) | e == x = True
                   | otherwise = pertenece e xs

 {-
 2. todosIguales :: (Eq t) => [t]-> Bool, que dada una lista devuelve verdadero s´ı y solamente s´ı todos sus ele
mentos son iguales.
 -}
todosIguales :: (Eq t) => [t] -> Bool 
todosIguales [] = True
todosIguales [x] = True
todosIguales (x : y :xs) | x == y = todosIguales (y:xs)
                      | otherwise = False

 {-
 3. todosDistintos :: (Eq t) => [t]-> Bool seg´un la siguiente especificaci´on:
 problema todosDistintos (s: seq⟨T⟩) : B {
 requiere: { True }
 asegura: { resultado = false ↔ existen dos posiciones distintas de s con igual valor }
 }
 -}
todosDistintos :: ( Eq t) => [t] -> Bool 
todosDistintos [x] = True
todosDistintos (x:xs) | (pertenece x xs) = False
                      | otherwise = todosDistintos xs 

 {-
 4. hayRepetidos :: (Eq t) => [t]-> Bool seg´un la siguiente especificaci´on:
 problema hayRepetidos (s: seq⟨T⟩) : B {
 requiere: { True }
 asegura: { resultado = true ↔ existen dos posiciones distintas de s con igual valor }
 }
-}

{-
5. quitar :: (Eq t) => t-> [t]-> [t], que dados un entero x y una lista xs, elimina la primera aparici´on de x en
 la lista xs (de haberla).
 -}
quitar :: (Eq t, Ord t) => t -> [t] -> [t] 
quitar _ [] = []
quitar i (x:xs) | i == x = xs
                | otherwise = x : quitar i xs

 {-
 6. quitarTodos :: (Eq t ) => t-> [t]-> [t], que dados un entero x y una lista xs, elimina todas las apariciones
 de x en la lista xs (de haberlas). Es decir:
 problema quitarTodos (e: T, s: seq⟨T⟩) : seq⟨T⟩ {
 requiere: { True }
 asegura: { resultado es igual a s pero sin el elemento e. }
 }
 -}

 {-
 7. eliminarRepetidos :: (Eq t) => [t]-> [t] quedeja en la lista una ´unica aparici´on de cada elemento, eliminando
 las repeticiones adicionales.
 -}


 {-
 8. mismosElementos :: (Eq t) => [t]-> [t]-> Bool, que dadas dos listas devuelve verdadero s´ı y solamente s´ı
 ambas listas contienen los mismos elementos, sin tener en cuenta repeticiones, es decir:
 problema mismosElementos (s: seq⟨T⟩, r: seq⟨T⟩) : B {
 requiere: { True }
 asegura: { resultado = true ↔ todo elemento de s pertenece r y viceversa}
 }
-}

 {-
 9. capicua :: (Eq t) => [t]-> Bool seg´un la siguiente especificaci´on:
 problema capicua (s: seq⟨T⟩) : B {
 requiere: { True }
 asegura: { (resultado = true) ↔ (s = reverso(s)) }
 }
 Por ejemplo capicua [´a’,’c’, ’b’, ’b’, ’c’, ´a’] es true, capicua [´a’, ’c’, ’b’, ’d’, ´a’] es false
-}