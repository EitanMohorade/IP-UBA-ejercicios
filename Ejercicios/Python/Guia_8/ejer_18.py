# Ejercicio 18 - Guía Práctica 8
# Sistema de gestión de inventario usando diccionarios.
#
# inventario: dict[str, dict[str, int | float]]
#
# 1. problema agregar_producto(inout inventario, in nombre: str, in precio: R, in cantidad: Z)
#    requiere: cantidad ≥ 0, precio ≥ 0, nombre no vacío y no repetido.
#    asegura: agrega el producto con {"precio": precio, "cantidad": cantidad}.
def agrega_producto(inv: dict[str, dict[str, int]], n:str,p: int, c:int):
    inv[n] = {"precio": p, "cantidad":c}
# 2. problema actualizar_stock(inout inventario, in nombre: str, in cantidad: Z)
#    requiere: nombre existente, cantidad ≥ 0
#    asegura: actualiza la cantidad manteniendo el precio.
def actualizar_stock(inv: dict[str, dict[str, int]], nombre: str, cantidad: int):
    inv[nombre]["cantidad"] = cantidad
# 3. problema actualizar_precio(inout inventario, in nombre: str, in precio: R)
#    requiere: nombre existente, precio ≥ 0
#    asegura: actualiza el precio manteniendo la cantidad.
def actualizar_precio(inv: dict[str, dict[str, int]], nombre: str, precio: int):
    inv[nombre]["precio"] = precio
# 4. problema calcular_valor_inventario(in inventario) : R
#    asegura: suma de (precio * cantidad) de todos los productos.
def calcular_valor_inventario(inv: dict[str, dict[str, int]])-> int:
    res:int=0
    for i in inv.values():
        res += i["cantidad"] * i["precio"]
    return res
inventario:dict[dict[str,int]]={
    "cartera":{"precio":0, "cantidad":21},
    "remera":{"precio":13, "cantidad":21},
    "bolso":{"precio":13, "cantidad":1},
    "lapices":{"precio":63, "cantidad":3}
    }

# print(inventario)
# print("----------")
# agrega_producto(inventario, "libbros", 99, 2)
# print(inventario)
# print("----------")
# actualizar_stock(inventario, "cartera", 213)
# print("----------")
# print(inventario)

print(calcular_valor_inventario(inventario))