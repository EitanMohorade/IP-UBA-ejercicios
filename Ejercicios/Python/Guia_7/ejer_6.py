# ============================================================
# EJERCICIO 6 - Operaciones sobre matrices
# ============================================================
# Implementar las siguientes funciones:
#
# 1. es_matriz(s):
#    devuelve True si s es una lista no vacía y todas las filas tienen la misma longitud.
def es_matriz(s:list[list[int]])->bool:
    res:int=0
    if(len(s)>0):
        res = len(s[0])
        for i in s:
            if(len(i) != res):
                res=0
    return res != 0
# 2. filas_ordenadas(m):
#    devuelve una lista de booleanos indicando si cada fila está ordenada.
def filas_ordenadas(s:list[list[int]])-> None:
    res: list[bool]=[]
    for i in s:
        if(ordenadas(i)):
            res.append[True]
        else:
            res.append[False]
# 3. columna(m, c):
#    devuelve una lista con los elementos de la columna c.
def columna(m:list[list[int]], c:int)->list[int]:
    res:list[int]=[]
    for i in m:
        res.append[i[c]]
    return res
# 4. columnas_ordenadas(m):
#    devuelve una lista de booleanos indicando si cada columna está ordenada.
#
# 5. transponer(m):
#    devuelve la matriz transpuesta de m (intercambia filas y columnas).
#
# 6. quien_gana_tateti(m):
#    recibe una matriz 3x3 con caracteres 'X', 'O' o ' '.
#    Devuelve:
#       0 → si gana O
#       1 → si gana X
#       2 → si no hay ganador
#
# 7. (Opcional) exponenciacion_matriz(d, p):
#    genera una matriz cuadrada aleatoria de dimensión d
#    y la eleva a la potencia p multiplicándola por sí misma p veces.
#    Requiere numpy para generar matrices aleatorias.