def imprimir_saludos(nombre: str) -> str:
    return "hola" + nombre 

def raiz_cuadrada_de(n:int) -> int:
    return n**2

def fahrenheit_a_celsius(temp_far: int) -> int:
    return ((temp_far - 32)*5)/5

def imprimir_dos_veces(estribillo: str)-> str:
    return estribillo * 2

def es_multiplo_de(n: int, m: int) -> bool:
    return n%m == 0

def es_primo(n:int) -> bool:
    y : int = 2
    if (n == 2):
        return True
    elif (n < 2):
        return False
    while (y < n):
        if (es_multiplo_de(n,y)):
            return False
        y += 1
    return True

def es_par(n:int) -> bool:
    if (es_multiplo_de(n, 2)):
        return True
    return False

def cantidad_de_pizzas(comensales: int , min_cant_porciones: int ) -> int: #cada pizza tiene 8 porciones
    total_porciones : int = comensales * min_cant_porciones
    pizza : int = 8
    while (pizza < total_porciones):
        pizza += 8
    return pizza/8
print(cantidad_de_pizzas(4,11))
