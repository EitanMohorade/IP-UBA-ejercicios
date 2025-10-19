from queue import Queue as Cola
# Ejercicio 11 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema buscar_nota_minima(in c: Cola[seq⟨Char⟩ × Z]) : seq⟨Char⟩ × Z
# requiere: c no está vacía
# requiere: los elementos de c no tienen valores repetidos en la segunda componente
# asegura: res es una tupla de c
# asegura: no hay ningún elemento en c cuya segunda componente sea menor que la de res

def clon_cola(c:Cola[tuple[str, int]])->Cola[tuple[str, int]]:
    res:Cola[tuple[str, int]]=Cola()
    aux:Cola[tuple[str, int]]=Cola()

    while (not c.empty()):
        aux.put(c.get())
    while(not aux.empty()):
        elem: tuple[str, int] =aux.get() 
        res.put(elem)    
        c.put(elem)
    return res

def buscar_nota_minima(c: Cola[tuple[str, int]])-> tuple[str, int]:
    clon: Cola[tuple[str, int]] = clon_cola(c)
    res: tuple[str, int] = (clon.get())[1]

    while(not clon.empty()):
        aux:Cola[tuple[str, int]]= (clon.get())[1]
        if(aux < res):
            res = aux
    return res

c:Cola[int]=Cola()
c.put(("asf",2))
c.put(("asf",1))
c.put(("asf",512121))
c.put(("asf",245))
print(buscar_nota_minima(c))