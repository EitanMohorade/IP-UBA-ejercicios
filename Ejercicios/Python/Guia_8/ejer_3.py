from queue import LifoQueue as Pila
# Ejercicio 3 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema buscar_el_maximo(in p: Pila[Z]) : Z
# requiere: p no está vacía
# asegura: res es un elemento de p
# asegura: res es mayor o igual a todos los elementos de p
def clon_pila (p:Pila[int])->Pila[int]:
    clon: Pila[int] = Pila()
    aux: Pila[int] = Pila()

    while(not p.empty()):
        aux.put(p.get())
    while(not aux.empty()):
        e:int=aux.get() 
        clon.put(e)
        p.put(e)
    return clon

def buscar_el_maximo(p:Pila[int])->int:
    clon: Pila[int] = clon_pila(p)
    res: int = clon.get()
    while (not clon.empty()):
        e:int=clon.get()
        if (res < e):
            res: int = e
    return res

p:Pila[int]=Pila()
p.put(123)
p.put(5)
p.put(7)
p.put(92)
p.put(2142)

print(buscar_el_maximo(p))
