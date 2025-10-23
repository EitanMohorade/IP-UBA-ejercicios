# Ejercicio 25 - Guía Práctica 8
# Implementar:
#
# problema agregar_frase_al_principio(in nombre_archivo: str, in frase: str)
# requiere: archivo existente y accesible, frase no vacía
# asegura: agrega 'frase' como primera línea del archivo (modifica el archivo original).
def agregar_frase_al_principio(nom_archivo: str, frase: str):
    archivo=open(nom_archivo, "r")
    respaldo:list[str]=[]
    for i in archivo:
        respaldo.append(i)
    archivo.close()
    archivo=open(nom_archivo, "w")
    archivo.write(frase+"\n")
    for i in range(0, len(respaldo)):
        archivo.write(respaldo[i])
    archivo.close()
    
agregar_frase_al_principio("Ejercicios\Python\Guia_8\ejer_22.txt", "estoy al principio")