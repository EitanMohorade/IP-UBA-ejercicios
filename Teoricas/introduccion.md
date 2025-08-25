## Listas
* Crear listas en GHCi
let numeros = [1,2,3,4]  

* Concatenar listas
[1,2,3,4] ++ [9,10,11,12]    [1,2,3,4,9,10,11,12]
"hello" ++ " " ++ "world"    "hello world"

* Operador (:) agrega al inicio
'U':"n gato negro"           "Un gato negro"
5:[1,2,3,4]                  [5,1,2,3,4]

* Acceder por índice (empieza en 0)
"Steve Buscemi" !! 6         'B'
[9.4,33.2,96.2] !! 1         33.2


OJO: El operador ++ recorre toda la lista izquierda antes de concatenar → menos eficiente que usar : para agregar un solo elemento al inicio.

## Rangos
[1..20]          [1,2,3,...,20]
['a'..'z']       "abcdefghijklmnopqrstuvwxyz"
['K'..'Z']       "KLMNOPQRSTUVWXYZ"

* Rangos con saltos
[2,4..20]        [2,4,6,8,...,20]

## Listas intensionales (list comprehensions)
[x*2 | x <- [1..10]]  
 [2,4,6,8,10,12,14,16,18,20]

[x | x <- [10..20], x /= 13, x /= 15, x /= 19]  
 [10,11,12,14,16,17,18,20]

[x*y | x <- [2,5,10], y <- [8,10,11]]  
 [16,20,22,40,50,55,80,100,110]

## Tuplas

Similares a las listas, pero pueden contener tipos distintos.

let tupla = (1, "a")  
tupla    (1,"a")


Importante: las tuplas son rígidas → (1, "a") no es lo mismo que (1, "a", True).
Se distinguen entre duplas, tríplas, cuádruplas, etc.

* Funcion zip
Es una funcion la cual genera duplas en base a dos listas
```bash
    ghci> zip [5,3,2,6,2,7,2,5,4,6,6] ["soy","una","tortuga"]
    [(5,"soy"),(3,"una"),(2,"tortuga")]
```


### Datos curiosos

* Haskell no requiere que definas funciones en un orden específico.

* if en Haskell siempre necesita un else, porque todo debe devolver un valor.

* Las listas son homogéneas, o sea,todos los elementos deben ser del mismo tipo.

* En GHCi podés usar let para definir variables:

    let a = 1
