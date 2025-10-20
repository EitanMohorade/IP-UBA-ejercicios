from queue import Queue as Cola
from random import randint
# Ejercicio 13 - Guía Práctica 8
# Bingo
#
# 1. problema armar_secuencia_de_bingo() : Cola[Z]
#    requiere: True
#    asegura: res contiene los números del 0 al 99 sin repetidos y en orden aleatorio.
#
# 2. problema jugar_carton_de_bingo(in carton: seq⟨Z⟩, in bolillero: Cola[Z]) : Z
#    requiere: carton tiene 12 números sin repetidos entre 0 y 99
#    requiere: bolillero contiene los 100 números (0–99) sin repetidos y en orden aleatorio
#    asegura: res es la cantidad mínima de jugadas necesarias para que salgan todos los números del cartón.
def clon_cola (c:Cola[int])->Cola[int]:
    aux:Cola[int]=Cola()
    res:Cola[int]=Cola()
    while (not c.empty()):
        aux.put(c.get())
    while (not aux.empty()):
        e: int = aux.get()
        res.put(e)
        c.put(e)
    return res

def pertenece_cola (c:Cola[int], e: int)-> bool:
    clon:Cola[int]= clon_cola(c)
    res:int=0
    while(not clon.empty()):
        if(e == clon.get()):
            res = 1
    return res == 1

def pertenece_lista(l:list[int], e: int)->bool:
    res:int=0
    for i in l:
        if(i == e):
            res = 1
    return res == 1

def tamaño_cola(c:Cola[int])-> int:
    clon:Cola[int]=clon_cola(c)
    res:int=0
    while(not clon.empty()):
        clon.get()
        res += 1
    return res

def armar_secuencia_de_bingo()->Cola[int]:
    res:Cola[int]= Cola()
    
    while (tamaño_cola(res) < 100):
        rdm:int=randint(0,99)
        if(not pertenece_cola(res, rdm)):
            res.put(rdm)
    return res


def jugar_carton_de_bingo(carton: list[int],bolillero: Cola[int]) -> int:
    clon:Cola[int]= clon_cola(bolillero)
    aux:int=0
    res:int=0
    while(aux != len(carton)):
        e:int=clon.get()
        if (pertenece_lista(carton, e)):
            aux += 1
        res +=1
    return res

p:Cola[int]= armar_secuencia_de_bingo()
# print(tamaño_cola(p))
clon:Cola[int]=clon_cola(p)
while(not clon.empty()):
    print(clon.get())

carton:list[int]= [3, 6]
print("jugadas minimas con el carton: ", jugar_carton_de_bingo(carton, p))