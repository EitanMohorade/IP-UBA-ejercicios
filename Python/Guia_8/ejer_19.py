# Ejercicio 19 - Guía Práctica 8
# Trabajando con archivos de texto.
#
# 1. contar_lineas(in nombre_archivo: str) : int
#    → cantidad de líneas del archivo.
def contar_lineas(nom_archivo: str)->int:
    res:int=0
    archivo = open(nom_archivo, "r")
    for i in archivo.readlines():
        res += 1
    archivo.close()
    return res
# 2. existe_palabra(in nombre_archivo: str, in palabra: str) : bool
#    → True si 'palabra' aparece al menos una vez.
def existe_palabra(nom_archivo: str, palabra: str) ->bool:
    res:int=0
    archivo = open(nom_archivo, "r")
    for i in archivo.readlines():
        if(i == palabra or i == palabra + "\n"):
            res =1
    archivo.close()
    return res == 1
# 3. cantidad_de_apariciones(in nombre_archivo: str, in palabra: str) : int
#    → cantidad de veces que 'palabra' aparece en el archivo.
def cantidad_de_apariciones(nom_archivo:str, palabra:str)->int:
    res:int=0
    archivo = open(nom_archivo, "r")
    for i in archivo.readlines():
        if(i == palabra or i == palabra + "\n"):
            res += 1
    archivo.close()
    return res
    


print(contar_lineas("/home/eitan/IP-UBA-ejercicios/Ejercicios/Python/Guia_8/Archivos/ejer_19.txt"))
print(existe_palabra("/home/eitan/IP-UBA-ejercicios/Ejercicios/Python/Guia_8/Archivos/ejer_19.txt", "hola buenas"))
print(cantidad_de_apariciones("/home/eitan/IP-UBA-ejercicios/Ejercicios/Python/Guia_8/Archivos/ejer_19.txt", "hola buenas"))
