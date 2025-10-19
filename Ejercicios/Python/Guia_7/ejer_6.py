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
def ordenadas(s:list[int])->bool:
    res:int=0
    for i in range (0,len(s)-1):
        if (s[i] > s[i+1]):
            res +=1
    return res == 0
        
def filas_ordenadas(s:list[list[int]],out:list[bool])-> None:
    out.clear()
    for i in s:
        if(ordenadas(i)):
            out.append(True)
        else:
            out.append(False)
# var : list[bool]=[]
# filas_ordenadas([[1,3,4],[3,5,6],[7,4,5]],var)
# print(var)

# 3. columna(m, c):
#    devuelve una lista con los elementos de la columna c.
def columna(m:list[list[int]], c:int)->list[int]:
    res:list[int]=[]
    for i in m:
        res.append(i[c])
    return res

# 4. columnas_ordenadas(m):
#    devuelve una lista de booleanos indicando si cada columna está ordenada.

def columna_ordenadas(m:list[list[int]])->list[bool]:
    res: list[bool]=[]
    for s in range(0,len(m)):
        if(ordenadas(columna(m,s))):
            res.append(True)
        else:
            res.append(False)
    return res
        
#print(columna_ordenadas([[1,3,4],[3,5,5],[7,4,10]]))

# 5. transponer(m):
#    devuelve la matriz transpuesta de m (intercambia filas y columnas).
def agregar_columna_x(m:list[list[int]], c:int)->list[int]:
    res : list[int] = []
    for s in m:
        res.append(s[c])
    return res

def trasponer(m:list[list[int]])->list[list[int]]:
    res : list[list[int]] = []
    for i in range(0,len(m)):
        res.append(agregar_columna_x(m,i))
    return res


# 6. quien_gana_tateti(m):
#    recibe una matriz 3x3 con caracteres 'X', 'O' o ' '.
#    Devuelve:
#       0 → si gana O
#       1 → si gana X
#       2 → si no hay ganador
def iguales_a(l:list[str],x:str)->bool:
    res:int=0
    for e in l:
        if(e != x):
            res += 1
    return res == 0

def ganador_por_linea(m:list[list[str]],e:str)->bool:
    res:int=0
    for s in m:
        if(iguales_a(s,e)):
            res += 1
    return res != 0

def ganador_por_cruz_1(m:list[list[str]],e:str)->bool:
    res:int=0
    for s in m:
        if(s[res]==e):
            res += 1
    return res == 3

def ganador_por_cruz_2(m:list[list[str]],e:str)->bool:
    res:int=len(m)-1
    for s in m:
        if(s[res]==e):
            res -= 1
    return res == -1

#print(ganador_por_cruz_2([["O","O","X"],["O","X","O"],["X","X","O"]],"X"))

def quien_gana_tateti(m:list[list[str]])->int:
    res:int=2
    if (ganador_por_linea(m, "X") or ganador_por_cruz_1(m, "X") or ganador_por_cruz_2(m, "X")):
        res = 1
    elif(ganador_por_linea(m, "O") or ganador_por_cruz_1(m, "O") or ganador_por_cruz_2(m, "O")):
        res = 0
    return res
#print(quien_gana_tateti([["O","O","X"],["O"," ","O"],[" ","X","O"]]))
# 7. (Opcional) exponenciacion_matriz(d, p):
#    genera una matriz cuadrada aleatoria de dimensión d
#    y la eleva a la potencia p multiplicándola por sí misma p veces.
#    Requiere numpy para generar matrices aleatorias.
