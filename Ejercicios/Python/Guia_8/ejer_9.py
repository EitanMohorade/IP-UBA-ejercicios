from queue import Queue as Cola
# Ejercicio 9 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema cantidad_elementos(in c: Cola) : Z
# requiere: True
# asegura: res es igual a la cantidad de elementos que contiene c
#
# Restricciones:
# - No se puede usar Queue.qsize().
# - Comparar el resultado con la versión usando pila.
def clon_cola(c:Cola[int])->Cola[int]:
    res:Cola[int]=Cola()
    aux:Cola[int]=Cola()

    while (not c.empty()):
        aux.put(c.get())
    while(not aux.empty()):
        elem: int =aux.get() 
        res.put(elem)    
        c.put(elem)
    return res

def cantidad_elementos(c:Cola[int])-> int:
    clon: Cola[int] = clon_cola(c)
    res:int = 0
    while (not clon.empty()):
        res += 1
        clon.get()
    return res

c:Cola[int]=Cola()
c.put(21)
c.put(1)
c.put(2)
c.put(245)
print(cantidad_elementos(c))