from random import randint
from queue import LifoQueue as Pila

# Ejercicio 1 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema generar_nros_al_azar(in cantidad: Z, in desde: Z, in hasta: Z) : Pila[Z]
# requiere: cantidad ≥ 0
# requiere: desde ≤ hasta
# asegura: El tamaño de res es igual a cantidad
# asegura: Todos los elementos de res son valores entre desde y hasta (inclusive), 
#          seleccionados aleatoriamente con probabilidad uniforme.
#
# Sugerencia: usar random.randint(desde, hasta)
# Importar el módulo random con: import random
# Puede usarse la clase LifoQueue del módulo queue como pila:
#   from queue import LifoQueue as Pila
#   p = Pila(); p.put(x); p.get(); p.empty()


def generar_nros_al_azar(cant:int,desde:int,hasta:int)->Pila[int]:
    res: Pila[int] = Pila()
    for i in range(cant,0,-1):
        res.put(randint(desde, hasta))
    return res

pila_azar = generar_nros_al_azar(3,10,50)

while not pila_azar.empty():
    print(pila_azar.get())

p:Pila[int]=Pila()
p.put(1)
p.put(12)
p.put(3)

