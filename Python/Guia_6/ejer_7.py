# ============================================================
# EJERCICIO 7
# ============================================================
# Reescribir las funciones del Ejercicio 6 usando un bucle for con range(inicio, fin, paso).
# Recordar que range genera una secuencia de números desde un valor inicial hasta un final,
# avanzando de a pasos indicados. Revisar la documentación oficial si es necesario.
def monitorear_viaje_del_tiempo_V3(año_partida:int):
    for num in range (año_partida, (-384),(-20)):
        print(num)
