# Ejercicio 21 - Guía Práctica 8
# Implementar:
#
# problema la_palabra_mas_frecuente(in nombre_archivo: str) : str
# requiere: archivo existente con al menos una palabra
# asegura: res es una palabra del archivo
# asegura: ninguna palabra aparece más veces que res
#
# Sugerencia: usar un diccionario {palabra: frecuencia}
def cantidad_de_apariciones(nom_archivo:str, palabra:str)->int:
    res:int=0
    archivo = open(nom_archivo, "r")
    for i in archivo.readlines():
        if(i == palabra or i == palabra + "\n"):
            res += 1
    archivo.close()
    return res

def la_palabra_mas_frecuente(nom_archivo: str)->str:
    archivo = open(nom_archivo, "r")
    e = archivo.readlines()
    res:str= archivo.readline()
    for i in e:
        if (cantidad_de_apariciones(nom_archivo, res) < cantidad_de_apariciones(nom_archivo, i)):
            res = i
    archivo.close()
    return res

print(la_palabra_mas_frecuente("Ejercicios\Python\Guia_8\ejer_19.txt"))