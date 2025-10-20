from queue import Queue as Cola

# Ejercicio 12 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema intercalar(in c1: Cola, in c2: Cola) : Cola
# requiere: c1 y c2 tienen la misma cantidad de elementos
# asegura: res contiene todos los elementos de c1 y c2 intercalados respetando el orden
# asegura: el primer elemento de res es el primer elemento de c1
# asegura: el tamaño de res es igual al doble del tamaño de c1
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

def intercalar(c1: Cola[int], c2: Cola[int])-> Cola[int]:
    clon1: Cola[int]= clon_cola(c1)
    clon2: Cola[int]= clon_cola(c2)
    res: Cola[int]= Cola()
    while(not clon1.empty() and not clon2.empty()):
        
        res.put(clon1.get())
        res.put(clon2.get())
    return res

c1:Cola[int]=Cola()
c1.put(0)
c1.put(1)
c1.put(0)
c1.put(1)

c2:Cola[int]=Cola()
c2.put(2)
c2.put(3)
c2.put(2)
c2.put(3)

var: Cola[int] = intercalar(c1,c2)
while (not var.empty()):
    print(var.get())