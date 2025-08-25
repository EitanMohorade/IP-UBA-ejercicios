## Tipos en Haskell

Con Haskell no se debe especificar qué tipo de dato estamos usando, este ya lo detecta por sí solo.  
Por ejemplo:  

```haskell
    True    -- se detecta como Booleano (Bool)
    "hoola" -- se detecta como [Char]
```
    [Char] se define con corchetes ya que representan una lista, en este caso, una lista de caracteres.

Usando :t 'algo' en ghci te dirá qué tipo será.

## Tipos en funciones

En las funciones también hay tipos.
Por ejemplo:

addThree x y z = x + y + z


El compilador tomará como tipo:

addThree :: Int -> Int -> Int -> Int

## Variable de tipo

Es importante aclarar que los tipos siempre empiezan en mayúscula, ya que son categorías definidas como puede ser Char, Bool, Float, etc.

En cambio, si una función devuelve el valor de una lista cualquiera, el tipo de esta función "no estaría definido".
A esto se le llaman variables de tipo, ya que pueden tomar cualquier tipo y siempre aparecen en minúscula.

Las funciones que son variables de tipos se llaman funciones polimórficas.

## Clases de tipos

Estas no son como las clases en lenguajes orientados a objetos.

Cuando se habla de tipos en funciones, puede que estas tengan un conjunto de tipos que deben cumplir aunque sean una variable de tipo.

Por ejemplo, la función (==) es una variable de tipo, pero su clase es Eq ya que es una comparación por igualdad de tipos.

Si a == b, entonces a y b deben ser del mismo tipo, ej: no puede ser un Int y un Bool.

* Anotaciones de tipo: estos son una forma de decir explicitamente el tipo que debe tener una expresion, se usa añadiendo :: al final de la exprecion y luego especificando el tipo. Ejemplo:

```bash
    ghci> read "5" :: Int
    5
    ghci> read "5" :: Float
    5.0
    ghci> (read "5" :: Float) * 4
    20.0
    ghci> read "[1,2,3,4]" :: [Int]
    [1,2,3,4]
    ghci> read "(3, 'a')" :: (Int, Char)
    (3, 'a')
```
Sirve mas que nada para decirle a Haskell que x expresion debe ser de este tipo en caso de que no se sepa cual es.