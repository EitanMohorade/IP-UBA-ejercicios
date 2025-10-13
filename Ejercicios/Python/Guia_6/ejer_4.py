# ============================================================
# EJERCICIO 4
# ============================================================
# Programar en Python usando composición de funciones (sin if).
# Se modela el peso de un pino a partir de su altura en metros:
# - 3 kg por cada centímetro hasta 3 metros.
# - 2 kg por cada centímetro por arriba de 3 metros.
#
# Definir:
# 1. peso_pino(altura): devuelve el peso del pino en kg según su altura.
def peso_pino(altura:int)->int:
    altura_en_cm : int = altura * 100
    peso : int = 0
    while(altura_en_cm > 0):
        if (altura_en_cm <= 300):
            peso += 3
        elif(altura_en_cm > 300):
            peso += 2
        altura_en_cm -= 1
    return peso
# 2. es_peso_util(peso): devuelve True si el peso está entre 400 y 1000 kg.
def es_peso_util(peso:int)->bool:
    return peso >= 400 and peso <= 1000
# 3. sirve_pino(altura): devuelve True si el pino de esa altura sirve para la fábrica.
# 4. Implementar sirve_pino usando composición de funciones.

def sirve_pino(altura:int)-> bool:
    return es_peso_util(peso_pino(altura))

