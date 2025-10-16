from random import randint
from queue import LifoQueue as Pila

def generar_nros_al_azar(cant:int,desde:int,hasta:int)->Pila[int]:
    res: Pila[int] = Pila()
    for i in range(cant,0,-1):
        res.put(randint(desde, hasta))
    return res
pila_azar = generar_nros_al_azar(3,10,50)
while not pila_azar.empty():
    print(pila_azar.get())

def tamaño_pila(p:Pila[int])->int:
    res:int=0
    while (not p.empty()):
        res += 1
        p.get()
    return res
/
def guardar_pila(p:Pila[int])->list[int]:
    clon:list[int]=[]
    while(not p.empty()):
        clon.append(p.get())
    return clon
def clonar_pila(p:Pila[int],clon:list[int])->None:
    for i in range(len(clon)-1,-1,-1):
        p.put(clon[i])


p:Pila[int]=Pila()
p.put(1)
p.put(12)
p.put(3)

var = guardar_pila(p)
clon = clonar_pila(p,var)

while (not p.empty()):
    print(p.get())

clon = clonar_pila(p,var)
while (not p.empty()):
    print(p.get())


def buscar_el_maximo(p:Pila[int])->int:
    return 1