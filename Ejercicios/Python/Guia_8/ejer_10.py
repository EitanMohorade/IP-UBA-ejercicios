from queue import Queue as Cola
# Ejercicio 10 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema buscar_el_maximo(in c: Cola[Z]) : Z
# requiere: c no está vacía
# asegura: res es un elemento de c
# asegura: res es mayor o igual a todos los elementos de c
#
# Comparar con la versión usando pila.
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

def buscar_el_maximo(c:Cola[int])-> int:
    clon: Cola[int] = clon_cola(c)
    res: int = clon.get()
    while (not clon.empty()):
        elemento: int = clon.get()
        if (res < elemento):
            res = elemento
    return res

c:Cola[int]=Cola()
c.put(2123)
c.put(512121)
c.put(512121)
c.put(245)
print(buscar_el_maximo(c))