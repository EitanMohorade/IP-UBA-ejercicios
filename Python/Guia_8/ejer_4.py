from queue import LifoQueue as Pila
# Ejercicio 4 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema buscar_nota_maxima(in p: Pila[seq⟨Char⟩ × Z]) : seq⟨Char⟩ × Z
# requiere: p no está vacía
# requiere: los elementos de p no tienen valores repetidos en la segunda posición de las tuplas
# asegura: res es una tupla de p
# asegura: No hay ningún elemento en p cuya segunda componente sea mayor que la de res
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




def buscar_nota_maxima(p: Pila[tuple[list[str], int]]) -> tuple[list[str], int]:
    clon:Pila[tuple[list[str], int]]= clon_pila(p)
    res: tuple[list[str], int]= clon.get()
    while(not clon.empty()):
        aux: tuple[list[str], int]= clon.get()
        if(res[1] < aux[1]):
            res = aux
    return res
p:Pila[tuple[list[str], int]] = Pila()
p.put((['a','b','v'],1212))
p.put((['a','b','v'],127))
p.put((['a','b','v'],152))
p.put((['a','b','v'],122))
p.put((['a','b','v'],254))

print(buscar_nota_maxima(p))