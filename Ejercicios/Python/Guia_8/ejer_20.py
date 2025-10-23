# Ejercicio 20 - Guía Práctica 8
# Implementar una solución para:
#
# problema agrupar_por_longitud(in nombre_archivo: str) : dict[int, int]
# requiere: archivo existente y accesible
# asegura: para cada longitud n de palabra, res[n] = cantidad de palabras de longitud n
#
# Ejemplo:
#   {1: 2, 2: 10, 5: 4}
#   → 2 palabras de largo 1, 10 de largo 2 y 4 de largo 5.
def cantidad_de_apariciones(nom_archivo:str, palabra:str)->int:
    res:int=0
    archivo = open(nom_archivo, "r")
    for i in archivo.readlines():
        if(i == palabra or i == palabra + "\n"):
            res += 1
    archivo.close()
    return res

def longitud_palabra(p:str)->int:
    res:int=0
    for i in p:
        res += 1
    return res-1

def agrupar_por_longitud(nom_archivo: str) -> dict[int,int]:
    res:dict[int,int]={}
    archivo =open(nom_archivo,"r")
    e=archivo.readlines()
    for i in e:
        res[longitud_palabra(i)] = cantidad_de_apariciones(nom_archivo, i)
    return res 
    

print(agrupar_por_longitud("Ejercicios\Python\Guia_8\ejer_19.txt"))
archivo= open("Ejercicios\Python\Guia_8\ejer_19.txt", "r")
