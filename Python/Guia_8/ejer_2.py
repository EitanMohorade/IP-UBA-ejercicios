from queue import LifoQueue as Pila

# Ejercicio 2 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema cantidad_elementos(in p: Pila) : Z
# requiere: True
# asegura: res es igual a la cantidad de elementos que contiene p
#
# Restricciones:
# - No se puede usar LifoQueue.qsize().
# - Usar get() modifica la pila, por lo que debe restaurarse al final (p es de tipo in).
def clon_pila (p:Pila[int])->Pila[int]:
    aux = Pila()
    clon = Pila()

    while not p.empty():
        aux.put(p.get())

    while not aux.empty():
        elem = aux.get()
        p.put(elem)      
        clon.put(elem)    

    return clon

def tamaño_pila(p:Pila[int])->int:
    clon = clon_pila(p)
    res:int=0
    while (not clon.empty()):
        res += 1
        clon.get()
    return res

p:Pila[int]=Pila()
p.put(1)
p.put(12)
p.put(3)
print(tamaño_pila(p))
