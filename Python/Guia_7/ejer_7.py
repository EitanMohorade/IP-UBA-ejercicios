# ============================================================
# EJERCICIO 7 - Programas interactivos con secuencias
# ============================================================
# Implementar las siguientes funciones que interactúan con el usuario:
#
# 1. ingresar_estudiantes():
#    solicita nombres al usuario hasta que escriba "listo" o presione ENTER vacío.
#    Devuelve la lista de nombres ingresados.
def ingresar_estudiantes()->list[str]:
    res: list[str]= []
    n: str = input("ponga nombre: ")
    while (n != "listo"):
        res.append(n)
        n = input("Ingrese nombre (o 'listo' para terminar): ")
    return res
#print(ingresar_estudiantes())

# 2. historial_monedero():
#    simula el historial de un monedero electrónico (ej: SUBE).
#    Opciones:
#      "C" → cargar crédito
#      "D" → descontar crédito
#      "X" → finalizar simulación
#    Devuelve una lista de tuplas con los movimientos realizados.
def pertenece(s: list[str],e:str)->bool:
    res:int=0
    for i in s:
        if (i == e):
            res = 1
    return res == 1

def historial_monedero()->list[tuple[str,int]]:
    accion:str= input("que accion quieres realizar?:")
    valor:int=0
    res:list[tuple[str,int]]=[]
    while (accion != "X"):
        if(accion == "C"):
            valor:int= input("cargaras credito, cuanto cargaras?:")  
            res.append(("C", valor))
        elif(accion == "D"):
            valor:int= input("cuanto se te debe descontar?:")
            res.append(("D", valor))
        accion:str= input("que accion quieres realizar?:")
    return res
print(historial_monedero())

# 3. juego_siete_y_medio():
#    simula el juego del 7½ con números aleatorios entre 1 y 12 (sin 8 ni 9).
#    Suma puntos según el valor de las cartas:
#       - 10, 11, 12 valen 0.5 puntos.
#    El jugador elige si seguir o plantarse. Pierde si supera 7.5.
#    Devuelve la lista de cartas obtenidas.
#
# 4. analizar_contrasena(pw):
#    analiza la fortaleza de una contraseña y devuelve:
#       "VERDE" → si cumple:
#           longitud > 8, al menos 1 mayúscula, 1 minúscula y 1 número.
#       "ROJA" → si longitud < 5.
#       "AMARILLA" → en los demás casos.