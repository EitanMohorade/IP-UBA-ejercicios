# ============================================================
# EJERCICIO 5 - Matrices (versión pertenece_a_cada_uno)
# ============================================================
# Implementar distintas versiones de la función que indica
# si un elemento pertenece a cada una de las listas dentro de una lista de listas.
#
# 1. pertenece_a_cada_uno_v1(s, e, res):
#    recibe la lista de listas s, el elemento e y una lista booleana out.
def pertenece_a_cada_uno_v1(s:list[list[int]], e:int):
    res:list[bool] = []
    for i in s:
        if (pertenece(i,e)):
            res.append[True]
        else:
            res.append[False]
# 2. pertenece_a_cada_uno_v2(s, e, res):
#    igual que la anterior, pero asegurando que |res| = |s|.
#
# 3. pertenece_a_cada_uno_v3(s, e):
#    devuelve una nueva lista de booleanos indicando si e pertenece a cada sublista.
def pertenece_a_cada_uno_v3(s:list[list[int]], e:int)->list[bool]:
    return pertenece_a_cada_uno_v1(s,e)
# Luego:
# - Analizar la relación entre las versiones y sus especificaciones.
# - ¿Se pueden usar las implementaciones entre sí?