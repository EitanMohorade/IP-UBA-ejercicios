# Ejercicio 1. Veterinaria- Stock
#  En la veterinaria ”Exactas’s pets”, al finalizar cada d´ıa, el personal registra en papeles los nombres y la cantidad actual de
#  los productos cuyo stock ha cambiado. Para mejorar la gesti´on, desde la direcci´on de la veterinaria han pedido desarrollar una
#  soluci´on en Python que les permita analizar las fluctuaciones del stock. Se pide implementar una funci´on, que reciba una lista
#  de tuplas donde cada tupla contiene el nombre de un producto y su stock en ese momento. La funci´on debe procesar esta lista
#  y devolver un diccionario que tenga como clave el nombre del producto y como valor una tupla con su m´ınimo y m´aximo stock
#  hist´orico registrado.
#  problema stock
#  productos (in stock
#  cambios : seq⟨str ×Z⟩) : seq⟨Z⟩ {
#  requiere: {Todos los elementos de stock cambios est´an formados por un str no vac´ıo y un entero ≥ 0.}
#  asegura: {res tiene como claves solo los primeros elementos de las tuplas de stock cambios (o sea, un producto).}
#  asegura: {res tiene como claves todos los primeros elementos de las tuplas de stock cambios.}
#  asegura: {El valor en res de un producto es una tupla de cantidades. Su primer elemento es la menor cantidad de ese
#  producto en stock cambios y como segundo valor el mayor.}
#  }
def pertenece_en_diccionario(diccionario: dict[str, tuple[int, int]], producto: tuple[str, int]) -> bool:
    res: int = 0
    for productos in diccionario.keys():
        if productos == producto[0]:
            res = 1
    return res == 1

def minimo_stock_de(stock_cambios: list[tuple[str, int]], producto: tuple[str, int]) -> int:
    minimo: int = producto[1]
    for stock in stock_cambios:
        if stock[0] == producto[0]:
            if stock[1] < minimo:
                minimo = stock[1]
    return minimo

def maximo_stock_de(stock_cambios: list[tuple[str, int]], producto: tuple[str, int]) -> int:
    maximo: int = producto[1]
    for stock in stock_cambios:
        if stock[0] == producto[0]:
            if stock[1] > maximo:
                maximo = stock[1]
    return maximo

def stock_productos(stock_cambios: list[tuple[str, int]]) -> dict[str, tuple[int, int]]:
    diccionario: dict[str, tuple[int, int]] = {}
    for stock in stock_cambios:
        if not pertenece_en_diccionario(diccionario, stock):
            diccionario[stock[0]] = (minimo_stock_de(stock_cambios, stock), maximo_stock_de(stock_cambios, stock))
    return diccionario

stock_cambios: list[tuple[str, int]] = [("calzones", 23),("calzones", 23),("medias", 5),("medias", 23),("calzones", 13),("medias", 55),("calzones", 1)]

resultado: dict[str, tuple[int, int]] = stock_productos(stock_cambios)

print(resultado)