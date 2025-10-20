# Ejercicio 22 - Guía Práctica 8
# Implementar:
#
# problema clonar_sin_comentarios(in nombre_archivo_entrada: str, in nombre_archivo_salida: str)
# requiere: archivo de entrada existente
# asegura: copia todas las líneas excepto las que comienzan con '#' o solo espacios antes de '#'
#
# Ejemplo:
#   Entrada:
#       # comentario
#       texto válido # esto se conserva
#   Salida:
#       texto válido # esto se conserva
def clonar_sin_comentarios(nom_archivo_entrada:str, nom_archivo_salida:str): 
    archivo_e=open(nom_archivo_entrada, "r")
    archivo_s=open(nom_archivo_salida,"w")
    for i in archivo_e:
        if(i[0] != "#"):
            archivo_s.write(i)
    archivo_e.close()
    archivo_s.close()


print(clonar_sin_comentarios("/home/eitan/IP-UBA-ejercicios/Ejercicios/Python/Guia_8/Archivos/ejer_22.txt","/home/eitan/IP-UBA-ejercicios/Ejercicios/Python/Guia_8/Archivos/ejer_22_clon.txt"))
