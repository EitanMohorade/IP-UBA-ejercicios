{-
Una reconocida empresa de comercio electr´onico nos pide desarrollar un sistema de stock de mercader´ıa. La mercader´ıa de
 la empresa va a ser representada como una secuencia de nombres de los productos, donde puede haber productos repetidos.
 El stock va a ser representado como una secuencia de tuplas de dos elementos, donde el primero es el nombre del producto y
 el segundo es la cantidad que hay en stock (en este caso no hay nombre de productos repetidos). Tambi´en se cuenta con una
 lista de precios de productos representada como una secuencia de tuplas de dos elementos, donde el primero es el nombre
 del producto y el segundo es el precio.
 Para implementar este sistema nos enviaron las siguientes especificaciones y nos pidieron que hagamos el desarrollo
 enteramente en Haskell, utilizando los tipos requeridos y solamente las funciones que se ven en la materia Introducci´on a la
 Programaci´on / Algoritmos y Estructuras de Datos I (FCEyN-UBA)
-}
type Texto = String
type Stock = [(Nombre, Cantidad)]
type Nombre = Texto 
type Cantidad = Int
type Mercaderia = [Nombre]
type Precios = [(Nombre, Precio)]
type Precio = Float 

{-Ejercicio 1
 Implementar la funci´on generarStock :: [String]->[(String, Int)]
 problema generarStock (mercader´ıa: seq⟨String⟩) : seq⟨String × Z⟩ {
 requiere: {True}
 asegura: { La longitud de res es igual a la cantidad de productos distintos que hay en mercader´ıa}
 asegura: {Para cada producto que pertenece a mercader´ıa, existe un i tal que 0 ≤ i < |res| y res[i]0=producto y
 res[i]1 es igual a la cantidad de veces que aparece producto en mercader´ıa}
 }
-}
generarStock :: Mercaderia -> Stock
generarStock [] = []
generarStock (x:xs) = (x, (mercarderiaRepetida x (x:xs)) ) : generarStock (eliminarMercaderia x (x:xs))

--auxiliar
mercarderiaRepetida :: Nombre -> Mercaderia -> Cantidad
mercarderiaRepetida x [] = 0
mercarderiaRepetida x (y:ys) | x == y = 1 + mercarderiaRepetida x ys
                             | otherwise = mercarderiaRepetida x ys

eliminarMercaderia :: Nombre -> Mercaderia -> Mercaderia
eliminarMercaderia x [] = []
eliminarMercaderia x (y:ys) | x == y = eliminarMercaderia x ys
                             | otherwise = y : eliminarMercaderia x ys 
--
{-Ejercicio 2
  Implementar la funci´on stockDeProducto :: [(String, Int))]->String->Int
 problema stockDeProducto (stock: seq⟨String × Z⟩, producto: String ) : Z {
 requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
 requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
 asegura: {si no existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0 entonces res es igual a 0 }
 asegura: {si existe un i tal que 0 ≤ i < |stock| y producto = stock[i]0 entonces res es igual a stock[i]1 }
 }
-}
stockDeProducto :: Stock -> Nombre  -> Int
stockDeProducto [] _ = 0
stockDeProducto ((x,c):xs) n | x == n = c
                             | otherwise = stockDeProducto xs n


{-Ejercicio 3
 Implementar la funci´on dineroEnStock :: [(String, Int))]->[(String, Float)]->Float
 problema dineroEnStock (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : R {
 requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
 requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
 requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
 requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
 requiere: {Todo producto de stock aparece en la lista de precios}
 asegura: {res es igual a la suma de los precios de todos los productos que est´an en stock multiplicado por la cantidad
 de cada producto que hay en stock}
 }
 Para resolver este ejercicio pueden utilizar la funci´on del Preludio de Haskell fromIntegral que dado un valor de tipo
 Int devuelve su equivalente de tipo Float.
-}
dineroEnStock :: Stock -> Precios -> Float
dineroEnStock [] _ = 0
dineroEnStock (x:xs) ((n2,p):ys) = (valorDeStockEnPrecios x ((n2,p):ys)) + (dineroEnStock xs ((n2,p):ys)) 

--auxiliar
valorDeStockEnPrecios :: (Nombre, Cantidad) -> Precios -> Float
valorDeStockEnPrecios _ [] = 0
valorDeStockEnPrecios (n1,c) ((n2,p):ys) | n1 == n2 = ((fromIntegral c) * p)
                                         | otherwise = valorDeStockEnPrecios (n1,c) ys
--

{-Ejercicio 4
Implementar la funci´on aplicarOferta :: [(String, Int)]->[(String, Float)]->[(String,Float)]
 problema aplicarOferta (stock: seq⟨String × Z⟩, precios: seq⟨String × R⟩ ) : seq⟨String × R⟩ {
 requiere: {No existen dos nombres de productos (primeras componentes) iguales en stock}
 requiere: {No existen dos nombres de productos (primeras componentes) iguales en precios}
 requiere: {Todas las cantidades (segundas componentes) de stock son mayores a cero}
requiere: {Todos los precios (segundas componentes) de precios son mayores a cero}
 requiere: {Todo producto de stock aparece en la lista de precios}
 asegura: {|res| = |precios|}
 asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) > 10, entonces res[i]0 = precios[i]0 y
 res[i]1 = precios[i]1∗ 0,80}
 asegura: {Para todo 0 ≤ i < |precios|, si stockDeProducto(stock, precios[i]0) ≤ 10, entonces res[i]0 = precios[i]0 y
 res[i]1 = precios[i]1 }
 }
-}
aplicarOferta :: Stock -> Precios -> Precios
aplicarOferta [] _ = []
--aplicarOferta ((n1,c):xs) ((n2,p):ys) | (stockDeProducto ((n1,c):xs) n1) > 10 = aplicarOferta xs (modificarPrecio1 n1 ((n2,p):ys)) 
  --                                    | otherwise = (n2,p) : aplicarOferta xs ((n2,p):ys)
aplicarOferta ((n1,c):xs) ((n2,p):ys) | (stockDeProducto ((n1,c):xs) n1) > 10 = (modificarPrecio2 n1 ((n2,p):ys)) : aplicarOferta xs ys
                                      | otherwise = (n2,p) : aplicarOferta xs ys

--auxiliar
modificarPrecio1 :: Nombre -> Precios -> Precios --modifica precio y devuelve lista entera con precio modificado segun el nombre
modificarPrecio1 _ [] = []
modificarPrecio1 n1 ((n2,p):ys) | n1 == n2 = (n2, (p*0.80)) : modificarPrecio1 n1 ys 
                               | otherwise = [(n2,p)] ++ modificarPrecio1 n1 ys

modificarPrecio2 :: Nombre -> Precios -> (Nombre, Precio) --modifica el precio y devuelve dupla de ese precio modificado
modificarPrecio2 n1 ((n2,p):ys) | n1 == n2 = (n2, (p*0.80)) 
                                | otherwise = modificarPrecio2 n1 ys
--