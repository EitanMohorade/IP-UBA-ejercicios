# Ejercicio 24 - Guía Práctica 8
# Implementar:
#
# problema agregar_frase_al_final(in nombre_archivo: str, in frase: str)
# requiere: archivo existente y accesible, frase no vacía
# asegura: agrega 'frase' como nueva línea al final del archivo (modifica el archivo original).
def agregar_frase_al_final(nom_archivo:str, frase:str):
    archivo=open(nom_archivo, "r")
    respaldo:list[str]=[]
    for i in archivo:
        respaldo.append(i)
    archivo.close()
    archivo=open(nom_archivo, "w")
    for i in range(0, len(respaldo)):
        archivo.write(respaldo[i])
    archivo.write("\n" +frase)
    archivo.close()


agregar_frase_al_final("/home/eitan/IP-UBA-ejercicios/Ejercicios/Python/Guia_8/Archivos/ejer_22.txt", "estoy al final") 