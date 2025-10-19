from queue import LifoQueue as Pila
# Ejercicio 6 - Guía Práctica 8
# Evaluar una expresión en notación polaca inversa (postfija) usando una pila.
#
# problema evaluar_expresion(in s: seq⟨Char⟩) : R
# requiere: s solo contiene números enteros y operadores binarios +, -, * y /
# requiere: todos los elementos están separados por un espacio
# requiere: la expresión es sintácticamente válida
# asegura: res es el valor obtenido al evaluar la expresión postfija
#
# Algoritmo sugerido:
# 1. Separar los tokens por espacios.
# 2. Recorrer los tokens:
#    a) Si es número → apilar.
#    b) Si es operador → desapilar los dos operandos, operar, apilar el resultado.
# 3. El resultado queda en la cima de la pila.
#
# Ejemplo:
#   expresion = "3 4 + 5 * 2 -"
#   resultado = evaluar_expresion(expresion)
#   print(resultado)  # → 33

def pertenece (e: str, s:list[str])-> bool:
    res:int=0
    for i in s:
        if(i == e):
            res = 1
    return res == 1

def clon_pila (p:Pila[str])->Pila[str]:
    clon: Pila[str] = Pila()
    aux: Pila[str] = Pila()

    while(not p.empty()):
        aux.put(p.get())
    while(not aux.empty()):
        e:str=aux.get() 
        clon.put(e)
        p.put(e)
    return clon

def evaluar_expresion(s:str)-> int:
    p:Pila[int]=Pila()
    simbolos: list[str] = ['+', '-', '*', '/']
    for e in s:
        if (e != ' ' and (not pertenece(e, simbolos))):
            p.put(int(e))
        elif(pertenece(e, simbolos)):
            clon:Pila[str]= clon_pila(p)
            while(not clon.empty()):
                if (e == '+'):
                    p.put(clon.get() + clon.get())
                elif (e == '-'):
                    p.put(clon.get() - clon.get())
                elif (e == '*'):
                    p.put(clon.get() * clon.get())
                elif (e == '/'): 
                    p.put(clon.get() / clon.get())
    return p.get()

expresion = "3 4 + 5 * 2 -"

#resultado = evaluar_expresion(expresion)
#print(resultado) 

# p: Pila[int] = Pila()
# p.put(1)
# p.put(3)
# p.put(6)
# p.put(int("4"))
# p.put(p.get() + p.get())
# print(p.get())
var:list[int]=[]
for e in "213":
    var.append(int(e))
print(var)

FALTA AHSVCER SAAOFS AS,SA,F