{-
Usando los siguientes tipos:
type Anio = Integer
type EsBisiesto = Bool
Programar la funci´on bisiesto :: Anio-> EsBisiesto seg´un la siguiente especificaci´on:
problema bisiesto (a˜no : Z) : Bool {
requiere: {True}
asegura: {(res = false) ↔ (a˜no no es m´ultiplo de 4, o bien, a˜no es m´ultiplo de 100 pero no de 400)}
}
Por ejemplo:
bisiesto 1901 ⇝ False
bisiesto 1900 ⇝ False
bisiesto 1904 ⇝ True
bisiesto 2000 ⇝ True
-}