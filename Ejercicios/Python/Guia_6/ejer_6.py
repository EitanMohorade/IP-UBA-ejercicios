# ============================================================
# EJERCICIO 6
# ============================================================
# Implementar las siguientes funciones usando repetición condicional while:
#
# 1. Imprimir los números del 1 al 10.
def imprimir_1_al_10()->int:
    i:int=1
    while(i<=10):
        print(i)
        i += 1
# 2. Imprimir los números pares entre 10 y 40.
def imprimir_10_al_40 ()->int:
    i:int = 10
    while(i<=40):
        print(i)
        i+=1
# 3. Imprimir la palabra "eco" 10 veces.
def imprimir_eco_10 ()-> str:
    i:int=1
    while (i<= 10):
        print("eco")
        i += 1

# 4. Cuenta regresiva desde un número dado hasta 1, luego imprimir "Despegue".
def cuenta_regresiva(num:int):
    while(1<=num):
        print(num)
        num -= 1
    return "despegue"

# 5. Simular un viaje en el tiempo: recibe año de partida y llegada, imprime cada salto de 20 años.
def monitorear_viaje_del_tiempo(año_partida:int, año_llegada:int):
    while(año_llegada<año_partida):
        año_partida -= 1
        print("viajo un año al pasado, ahora está en:" + año_partida)
    
# 6. Repetir el viaje anterior pero viajando hacia atrás desde el año actual hasta 384 a.C. en saltos de 20 años.
def monitorear_viaje_del_tiempo_V2(año_partida:int):
    while(año_partida>(-384)):
        año_partida -= 20
        print("viajo 20 años atras, ahora esta en el año:" + año_partida)

