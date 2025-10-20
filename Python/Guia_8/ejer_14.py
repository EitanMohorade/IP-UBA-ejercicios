from queue import Queue as Cola
# Ejercicio 14 - Guía Práctica 8
# Modelar una guardia hospitalaria usando una cola.
#
# problema pacientes_urgentes(in c: Cola[Z × seq⟨Char⟩ × seq⟨Char⟩]) : Z
# requiere: todas las tuplas tienen un entero entre 1 y 10 como primer componente
# asegura: res es la cantidad de pacientes con prioridad menor a 4
def clon_cola (c:Cola[tuple[int, str, str]])->Cola[tuple[int, str, str]]:
    aux:Cola[tuple[int, str, str]]=Cola()
    res:Cola[tuple[int, str, str]]=Cola()
    while (not c.empty()):
        aux.put(c.get())
    while (not aux.empty()):
        e: tuple[int, str, str] = aux.get()
        res.put(e)
        c.put(e)
    return res

def pacientes_urgentes (c: Cola[tuple[int, str, str]])-> int:
    clon: Cola[tuple[int, str, str]]= clon_cola(c)
    res:int=0
    while(not clon.empty()):
        if ((clon.get())[0] < 4):
            res += 1
    return res

p: Cola[tuple[int, str, str]]=Cola()
p.put((98,"d","5fd"))
p.put((8,"d","5fd"))
p.put((4,"d","5fd"))
p.put((9,"d","5fd"))
p.put((1,"d","5fd"))

print(pacientes_urgentes(p))