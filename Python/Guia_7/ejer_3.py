# ============================================================
# EJERCICIO 3 - Evaluación de notas
# ============================================================
# Implementar una función que determine el estado de aprobación
# de una materia a partir de una lista de notas.
#
# resultado_materia(notas):
#    Devuelve:
#       1 → si todas las notas >= 4 y el promedio >= 7.
#       2 → si todas las notas >= 4 y el promedio está entre 4 y 7.
#       3 → si alguna nota < 4 o el promedio < 4.
def promedio_notas(notas:list[int])->int:
    res:int=0
    for i in notas:
        res += i
    return res/len(notas)

def todas_aprobadas(notas:list[int])->bool:
    res:int=len(notas)
    for i in notas:
        if(i<4):
            notas.remove(i)
    return res == len(notas)

def resultado_materia(notas:list[int])->int:
    res:int=0
    if(todas_aprobadas(notas)):
        if(promedio_notas(notas)>=7):
            res=1
        else:
            res=2
    else:
        res=3
    return res