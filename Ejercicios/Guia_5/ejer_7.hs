
{-
En este ejercicio trabajaremos con lockers de una facultad.
 Para resolverlo usaremos un tipo MapaDelockers que ser´a una secuencia de locker.
 Cada locker es una tupla con la primera componente correspondiente al n´umero de identificaci´on, y la segunda componente
 el estado.
 El estado es a su vez una tupla cuya primera componente dice si esta ocupado (False) o libre (True), y la segunda
 componente es un texto con el c´odigo de ubicaci´on del locker.
 type Identificacion = Integer
 type Ubicacion = Texto
 type Estado = (Disponibilidad, Ubicacion)
 type Locker = (Identificacion, Estado)
 type MapaDeLockers = [Locker]
 type Disponibilidad = Bool
-} 
type Texto = [Char]
type Identificacion = Int
type Ubicacion = Texto
type Estado = (Disponibilidad, Ubicacion)
type Locker = (Identificacion, Estado)
type MapaDeLockers = [Locker]
type Disponibilidad = Bool
{-
 1. Implementar existeElLocker :: Identificacion->MapaDeLockers->Bool, una funci´on para saber si un locker
 existe en la facultad.
-}
existeElLocker :: Identificacion->MapaDeLockers->Bool
existeElLocker _ [] = False
existeElLocker n ((id, u):xs) | n == id = True
                              | otherwise = existeElLocker n xs
{-
 2. Implementar ubicacionDelLocker :: Identificacion->MapaDeLockers->Ubicacion, una funci´on que dado un
 locker que existe en la facultad, me dice la ubicaci´on del mismo.
-} 
ubicacionDelLocker :: Identificacion->MapaDeLockers->Ubicacion
ubicacionDelLocker n ((id, (dispo, ubi)):xs) | n == id = ubi
                                             | otherwise = ubicacionDelLocker n xs
{-
 3. Implementar estaDisponibleElLocker :: Identificacion->MapaDeLockers->Bool, una funci´on que dado un
 locker que existe en la facultad, me devuelve Verdadero si esta libre.
-}
estaDisponibleElLocker :: Identificacion->MapaDeLockers->Bool
estaDisponibleElLocker n ((id, (dispo, ubi)):xs) |n == id = dispo
                                                 | otherwise = estaDisponibleElLocker n xs
{-
 4. Implementar ocuparLocker :: Identificacion->MapaDeLockers->MapaDeLockers, una funci´on que dado un loc
ker que existe en la facultad, y est´a libre, lo ocupa.
 Por ejemplo, un posible mapa de lockers puede ser:
lockers =
 [
 (100,(False,"ZD39I")),
 (101,(True,"JAH3I")),
 (103,(True,"IQSA9")),
 (105,(True,"QOTSA")),
 (109,(False,"893JJ")),
 (110,(False,"99292"))
 ]
-}
ocuparLocker :: Identificacion->MapaDeLockers->MapaDeLockers
ocuparLocker n ((id, (dispo, ubi)):xs) | n == id && dispo = ((id, (False, ubi)):xs)
                                       | otherwise = ocuparLocker n xs