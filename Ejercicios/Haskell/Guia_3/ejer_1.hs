{-
a) Implementar la funci´on parcial f :: Integer-> Integer definida por extensi´on de la siguiente manera:

 f(1) = 8
 f(4) = 131
 f(16) = 16

 y cuya especificaci´on es:
 problema f (n : Z) : Z {
    requiere: {n = 1 ∨ n = 4 ∨ n=16}
     asegura: {(n = 1 → res = 8) ∧ (n = 4 →res =131) ∧ (n = 16 →res =16)}
 }
-}
f :: Integer-> Integer

f x | x == 1 = 8
    | x == 4 = 131
    | x == 16 = 16

 

{-
b) An´alogamente, especificar e implementar la funci´on parcial g :: Integer-> Integer
 g(8) = 16
 g(16) = 4
 g(131) = 1
-}
g :: Integer-> Integer

g x | x == 131 = 1
    | x == 16 = 4
    | x == 8 = 16


{-
Especificacion: 
 problema g (n : Z) : Z {
    requiere: {n = 8 ∨ n = 16 ∨ n = 131}
    asegura: {(n = 8 → res = 16) ∧ (n = 16 →res = 4) ∧ (n = 131 →res =1)}
 }
-}
{-
c) A partir de las funciones definidas en los ´ıtems a) y b), implementar las funciones parciales h = f ◦ g y k = g ◦ f
-}
h :: Integer-> Integer
k :: Integer-> Integer

h x = g(f x)
k x = f(g x)