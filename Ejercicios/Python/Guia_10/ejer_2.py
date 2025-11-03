#  Ejercicio 2. Veterinaria- Filtrar c´odigos de barra
#  El hijo del due˜no de la veterinaria, cuya actividad principal es ver tik toks, cree que los productos cuyos c´odigos de barras
#  terminan en n´umeros primos son especialmente auspiciosos y deben ser destacados en la tienda. Luego de convencer a su padre
#  de esta idea, solicita una funci´on en Python que facilite esta gesti´on. Se pide implementar una funci´on que, dada una secuencia de
#  enteros, cada uno representando un c´odigo de barras de un producto, cree y devuelva una nueva lista que contenga ´unicamente
#  aquellos n´umeros de la lista original cuyos ´ultimos tres d´ıgitos formen un n´umero primo (por ejemplo, 101, 002 y 011).
#  Nota: Un n´umero primo es aquel que solo es divisible por s´ı mismo y por 1. Algunos ejemplos de n´umeros primos de hasta
#  tres d´ıgitos son: 2, 3, 5, 101, 103, 107, etc.
#  problema filtrar
#  codigos
#  primos (in codigos barra : seq⟨Z⟩) : seq⟨Z⟩ {
#  requiere: {Todos los enteros de codigos barra tienen, por lo menos, 3 d´ıgitos.}
#  requiere: {No hay elementos repetidos en codigos barra.}
#  asegura: {Los ´ultimos 3 d´ıgitos de cada uno de los elementos de res forman un n´umero primo.}
#  asegura: {Todos los elementos de codigos barra cuyos ´ultimos 3 d´ıgitos forman un n´umero primo est´an en res.}
#  asegura: {Todos los elementos de res est´an en codigos barra.}
#  }
from math import floor
def cant_digitos(numero:int)-> int:
    res:int=0
    aux: int = numero
    while(aux > 1):
        aux = aux/10
        res += 1
    return res 

def sumar_primeros_3_digitos (numero: int) -> int:
    res: int = 0
    digitos:int = cant_digitos(numero)
    aux:int = numero
    
    if(digitos >= 3):
        for _ in range(3):
            res += aux%10
            aux = floor(aux/10)
    else:
        for _ in range(digitos):
            res += aux%10
            aux = floor(aux/10)
    return res



def es_primo(numero: int) -> bool:
    res: int = 1
    for i in range(2, numero):
        if numero%i == 0:
            res = 0
    return res == 1

def codigos_primos (codigos_barra: list[int]) -> list[int]:
    lista_con_primos: list[int] = []
    for codigo in codigos_barra:
        primeros_3_digitos: int = sumar_primeros_3_digitos(codigo) 
        if es_primo(primeros_3_digitos):
            lista_con_primos.append(codigo)
    return lista_con_primos

codigos_barra: list[int] = [241124251,12512521,4364373445,21412521,124,215,2,5,92]

print(codigos_primos(codigos_barra))