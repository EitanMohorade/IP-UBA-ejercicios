from random import randint
from queue import Queue as Cola
# Ejercicio 8 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema generar_nros_al_azar(in cantidad: Z, in desde: Z, in hasta: Z) : Cola[Z]
# requiere: cantidad ≥ 0
# requiere: desde ≤ hasta
# asegura: el tamaño de res es igual a cantidad
# asegura: todos los elementos de res son valores entre desde y hasta (inclusive) 
#          seleccionados aleatoriamente con probabilidad uniforme.
#
# Sugerencia:
#   import random
#   from queue import Queue as Cola
#   c = Cola(); c.put(1); c.get(); c.empty()
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
def generar_nros_al_azar(c: int, d:int, h:int)-> Cola[int]:
    res: Cola[int]=Cola()
    while (c > 0):
        res.put(randint(d,h))
        c -= 1
    return res

c: Cola[int]= generar_nros_al_azar(3,1,10)
clon: Cola[int] = clon_cola(c)
while (not clon.empty()):
    print(clon.get())

while (not c.empty()):
    print(c.get())