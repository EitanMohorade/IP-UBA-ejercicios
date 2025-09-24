{-
Definir las siguientes funciones sobre listas:
 1. longitud :: [t]-> Integer, que dada una lista devuelve su cantidad de elementos.
 2. ultimo :: [t]-> t seg´un la siguiente especificaci´on:
 problema ultimo (s: seq⟨T⟩) : T {
 requiere: { |s| > 0 }
 asegura: { resultado = s[|s| − 1] }
 }
 -}

 {-
 3. principio :: [t]-> [t] seg´un la siguiente especificaci´on:
 problema principio (s: seq⟨T⟩) : seq⟨T⟩ {
 requiere: { |s| > 0 }
 asegura: { resultado = subseq(s,0,|s| − 1) }
 }
-}

 {-
 4. reverso :: [t]-> [t] seg´un la siguiente especificaci´on:
 problema reverso (s: seq⟨T⟩) : seq⟨T⟩ {
 requiere: { True }
 asegura: { resultado tiene los mismos elementos que s pero en orden inverso.}
 }
-}