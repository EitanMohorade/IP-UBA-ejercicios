# Ejercicio 16 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema calcular_promedio_por_estudiante(in notas: seq⟨seq⟨Char⟩ × R⟩) : Diccionario⟨seq⟨Char⟩, R⟩
# requiere: los nombres no son cadenas vacías
# requiere: las notas están entre 0 y 10
# asegura: cada clave de res es un nombre presente en notas
# asegura: el valor de cada clave es el promedio de sus notas
#
# Ejemplo:
#   notas = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
#   → {"Sole": 9.25, "Maxi": 8.0}

def cant_apariciones(s: list[tuple[str,int]], e:str)->int:
    res:int=0
    for i in s:
        if(i[0] == e):
            res += 1
    return res

def calcular_promedio_por_estudiante(notas: list[tuple[str,int]])-> dict[str,int]:
    res:dict[str, int]= {}
    for e in notas:
        if (e[0] in res.keys()):
            res[e[0]] += e[1]
        else:
            res[e[0]] = e[1]
    for k,v in res.items():
        res[k] = v / cant_apariciones(notas, k)
    return res


notas: list[tuple[str,int]]= [("Sole", 9.5), ("Maxi", 8.0),("Sole", 9.0)]
print(calcular_promedio_por_estudiante(notas))
