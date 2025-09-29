{-
 El Departamento de Matem´atica (DM) de la FCEyN-UBA nos ha encargado que desarrollemos un sistema para el
 tratamiento de n´umeros naturales. Espec´ıficamente les interesa conocer cu´ando un n´umero es perfecto y cu´ando dos n´umeros
 son amigos. Aunque por ah´ı no lo sab´ıas, estos conceptos existen y se definen como:
 Un n´umero natural es perfecto cuando la suma de sus divisores propios (n´umeros que lo dividen menores a ´el) es igual
 al mismo n´umero. Por ejemplo, 6 es un n´umero perfecto porque la suma de sus divisores propios (1,2 y 3) es igual a 6.
 Dos n´umeros naturales distintos son amigos si cada uno de ellos se obtiene sumando los divisores propios del otro.
 Por ejemplo, 220 y 284 son amigos porque los divisores propios de 220 son 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 y 110 que
 sumados dan 284 y los divisores propios de 284 son 1, 2 , 4, 71, 142 que sumados dan 220.
 Para implementar este sistema nos enviaron las siguientes especificaciones en lenguaje semiformal y nos pidieron que hagamos
 el desarrollo enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia
 Introducci´on a la Programaci´on / Algoritmos y Estructuras de Datos I (FCEyN-UBA).
-}

{-Ejercicio 1
Implementar la funci´on divisoresPropios :: Int->[Int]
 problema divisoresPropios (n: Z) : seq⟨Z⟩ {
 requiere: {n > 0}
 asegura: {res contiene a todos los divisores propios de n, ordenados de menor a mayor}
 asegura: {res no tiene elementos repetidos}
 asegura: {res no contiene a ning´un elemento que no sea un divisor propio de n}
 }
-}

{-Ejercicio 2
 Implementar la funci´on sonAmigos :: Int->Int->Bool
 problema sonAmigos (n,m: Z) : Bool {
 requiere: {n > 0}
 requiere: {m > 0}
 requiere: {m̸ = n}
 asegura: {res = True ⇔ n y m son n´umeros amigos}
 }
-}

{-Ejercicio 3
 Implementar la funci´on losPrimerosNPerfectos :: Int->[Int]
 problema losPrimerosNPerfectos (n: Z) : seq⟨Z⟩ {
 requiere: {n > 0}
 asegura: {|res| = n}
 asegura: {res es la lista de los primeros n n´umeros perfectos, de menor a mayor}
 }
 Por cuestiones de tiempos de ejecuci´on, no les recomendamos que prueben este ejercicio con un n > 4
-}

{-Ejercicio 4
 Implementar la funci´on listaDeAmigos :: [Int]->[(Int,Int)]
 problema listaDeAmigos (lista: seq⟨Z⟩) : seq⟨Z × Z⟩ {
 requiere: {Todos los n´umeros de lista son mayores a 0}
 requiere: {Todos los n´umeros de lista son distintos}
 asegura: {res es una lista de tuplas sin repetidos, que contiene a todos los pares de n´umeros que pertenecen a lista
 y son amigos entre s´ı}
 asegura: {|res| es igual a la cantidad de pares de n´umeros amigos que hay en lista.}
 }
-}