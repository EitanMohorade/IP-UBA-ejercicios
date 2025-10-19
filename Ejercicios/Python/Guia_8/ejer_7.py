from queue import LifoQueue as Pila
# Ejercicio 7 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema intercalar(in p1: Pila, in p2: Pila) : Pila
# requiere: p1 y p2 tienen la misma cantidad de elementos
# asegura: res solo contiene los elementos de p1 y p2
# asegura: res contiene todos los elementos de p1 y p2 intercalados respetando el orden original
# asegura: el tope de la pila res es el tope de p2
# asegura: el tamaño de res es igual al doble del tamaño de p1
#
# Nota: hay que recorrer dos veces para mantener el orden correcto.
def clon_pila(p: Pila)-> Pila:
    aux: Pila= Pila()
    clon: Pila= Pila()
    while(not p.empty()):
        aux.put(p.get())
    while(not aux.empty()):
        e:str=aux.get()
        clon.put(e)
        p.put(e)
    return clon


def intercalar(p1: Pila, p2: Pila)-> Pila:
    clon1: Pila = clon_pila(p1)
    clon2: Pila = clon_pila(p2)
    res:Pila= Pila()
    while (not clon1.empty() and not clon2.empty()):
        res.put(clon2.get())
        res.put(clon1.get())
    return res

p1:Pila=Pila()
p1.put(1)
p1.put(0)
p1.put(1)
p1.put(0)

p2:Pila=Pila()
p2.put("a")
p2.put("b")
p2.put("a")
p2.put("b")

res:Pila = intercalar(p1, p2)

while (not res.empty()):
    print(res.get())