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
    archivo_s.write(e[len(e)-1] + "\n") #es una excepcion ya que el ultimo elemento del archivo no tiene salto de linea
    for i in range(len(e)-2,-1,-1):
        archivo_s.write(e[i]) 
    archivo_e.close()
    archivo_s.close()

invertir_lineas("Ejercicios\Python\Guia_8\ejer_22.txt","Ejercicios\Python\Guia_8\ejer_22_clon.txt")
        