{-
Definir las siguientes funciones sobre listas:
 1. sumaAcumulada :: (Num t) => [t]-> [t] seg´un la siguiente especificaci´on:
 problema sumaAcumulada (s: seq⟨T⟩) : seq⟨T⟩ {
 requiere: {T es un tipo num´erico}
 requiere: {cada elemento de s es mayor estricto que cero}
 asegura: {|s| = |resultado| ∧ el valor en la posici´on i de resultado es i
 k=0 s[k]}
 }
 Por ejemplo sumaAcumulada [1, 2, 3, 4, 5] es [1, 3, 6, 10, 15].
-}

 {-
2. descomponerEnPrimos :: [Integer]-> [[Integer]] seg´un la siguiente especificaci´on:
 problema descomponerEnPrimos (s: seq⟨Z⟩) : seq⟨seq⟨Z⟩⟩ {
 requiere: { Todos los elementos de s son mayores a 2 }
 asegura: { |resultado| = |s| }
 asegura: {todos los valores en las listas de resultado son n´umeros primos}
 asegura: {multiplicar todos los elementos en la lista en la posici´on i de resultado es igual al valor en la posici´on
 i de s}
 }
 Por ejemplo descomponerEnPrimos [2, 10, 6] es [[2], [2, 5], [2, 3]].
-}