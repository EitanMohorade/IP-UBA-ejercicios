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

def pasar_a_pila(e:str)->Pila[str]:
    res:Pila[str]=Pila()
    for i in range(len(e)-1, -1,-1):
        res.put(e[i])
    return res

def evaluar_una_expresion(p:Pila[str]):
    expresion:Pila[str]=Pila()
    simbolos: list[str] = ['+', '-', '*', '/']
    count: int = 0
    while (count == 0):
        valor:str=p.get()
        if (valor != ' ' and (not pertenece(valor, simbolos))):
            expresion.put(valor)
        elif(pertenece(valor, simbolos)):
            expresion.put(valor)
            count = 1
    while(not expresion.empty()):
        valor:str=expresion.get()
        if (valor == '+'):
            p.put( int(expresion.get()) + int(expresion.get()) )
        elif (valor == '-'):
            p.put( int(expresion.get()) - int(expresion.get()))
        elif (valor == '*'):
            p.put( int(expresion.get()) * int(expresion.get()))
        elif (valor == '/'): 
            p.put( int(expresion.get()) / int(expresion.get()))
    #print(p.get())
def cant_expresiones(s:str)->int:
    simbolos: list[str] = ['+', '-', '*', '/']
    res: int=0
    for l in s:
        if(pertenece(l, simbolos)):
            res += 1 
    return res
def evaluar_expresion(s:str) -> float:
    expresion:Pila[str]=pasar_a_pila(s)
    limite:int=cant_expresiones(s)
    count:int = 0
    while count < limite:
        count += 1
        evaluar_una_expresion(expresion)
    return expresion.get()
expresion = "3 4 + 5 * 2 - 3 -"

var = pasar_a_pila(expresion)

print(evaluar_expresion(expresion))
