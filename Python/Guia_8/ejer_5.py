from queue import LifoQueue as Pila
# Ejercicio 5 - Guía Práctica 8
# Implementar una solución, que use pila, para el siguiente problema:
#
# problema esta_bien_balanceada(in s: seq⟨Char⟩) : Bool
# requiere: s solo puede tener números enteros, espacios y los símbolos '(', ')', '+', '-', '*', '/'
# asegura: res = True ↔ 
#           (la cantidad de paréntesis de apertura '(' es igual a la de cierre ')') y
#           (para todo prefijo de s, la cantidad de paréntesis de cierre no supera a la de apertura)
#
# Cada paréntesis de cierre debe tener uno de apertura antes.
# Ejemplos válidos:
#   "1 + (2 * 3) = (20 / 5)"
#   "10 * (1 + (2 * (1)))"
# Ejemplo no válido:
#   "1 + )2 * 3(("

def clon_pila(p: Pila[str])-> Pila[str]:
    aux: Pila[str]= Pila()
    clon: Pila[str]= Pila()
    while(not p.empty()):
        aux.put(p.get())
    while(not aux.empty()):
        e:str=aux.get()
        clon.put(e)
        p.put(e)
    return clon

def tamaño(p: Pila[str])-> Pila[str]:
    clon:Pila[str]=clon_pila(p)
    res:int=0
    while(not clon.empty()):
        clon.get()
        res += 1
    return res

def esta_bien_balanceada (s:list[str])->bool:
    pila: Pila[str] = Pila()
    res:int = 0

    for e in s:
        if(e == '(' or e == ')'):
            pila.put(e)

    longitud: int =tamaño(pila) 

    if (longitud%2 == 0):
        while (not pila.empty()):
            elem1: str = pila.get()
            elem2: str = pila.get()
            if(elem1 == ')' and elem2 == '('):
                res += 2
    else:
        res = -1

    return res != -1 and res == longitud


print(esta_bien_balanceada(['(',')','32','*','3','(',')']))

