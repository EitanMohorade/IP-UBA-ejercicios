# Ejercicio 23 - Guía Práctica 8
# Implementar:
#
# problema invertir_lineas(in nombre_archivo_entrada: str, in nombre_archivo_salida: str)
# requiere: archivo de entrada existente
# asegura: copia las líneas en orden inverso.
#
# Ejemplo:
#   Entrada:
#     Esta es la primera línea.
#     Y esta es la segunda.
#   Salida:
#     Y esta es la segunda.
#     Esta es la primera línea.
def invertir_lineas(nom_archivo_e:str, nom_archivo_s:str):
    archivo_e=open(nom_archivo_e, "r")
    archivo_s=open(nom_archivo_s, "w")
    e=archivo_e.readlines()
    for i in range(len(e)-1,-1,-1):
        print(i)
        archivo_s.write(e[i]) #COMO HAGO PARA SALTAR LINEAS ACA
    archivo_e.close()
    archivo_s.close()

invertir_lineas("/home/eitan/IP-UBA-ejercicios/Ejercicios/Python/Guia_8/Archivos/ejer_22.txt","/home/eitan/IP-UBA-ejercicios/Ejercicios/Python/Guia_8/Archivos/ejer_22_clon.txt")
        