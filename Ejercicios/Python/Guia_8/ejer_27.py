# Ejercicio 27 - Guía Práctica 8
# Implementar:
#
# problema calcular_promedio_por_estudiante(in nombre_archivo_notas: str, in nombre_archivo_promedios: str)
# requiere: archivo CSV de entrada con LU, materia, fecha, nota
# asegura: genera un CSV de salida con LU y promedio.
#
# Función auxiliar sugerida:
# problema promedio_estudiante(in notas_de_estudiantes: list[str], in lu: str) : float
# → devuelve el promedio de notas para el LU dado.
def pertenece(s:list[str], e:str)->bool:
    res:int =0
    for i in s:
        if i == e:
            res = 1
    return res == 1

def calcular_promedio_por_estudiante (nom_arch_notas:str, nom_arch_promedios:str ):
    notas=open(nom_arch_notas, "r")
    promedios=open(nom_arch_promedios, "a")
    datos:list[str] = notas.readlines()

    for lu in estudiantes(datos):
        texto:str="LU: "+lu+" promedio: "+str(promedio_estudiante(detectar_estudiantes(datos, lu)))+"\n"
        promedios.write(texto)
                

    notas.close()
    promedios.close()

def promedio_estudiante(notas_de_estudiantes:list[str])->float:
    res:float = 0
    cant: int = 0
    for i in notas_de_estudiantes:
        cant += 1
        count: int = 0
        for j in i:
            if(count == i.index("nota")):
                while (i[count] != ")"):
                    if (i[count] == "("): 
                        count += 1
                        res += int(i[count])#codigo mal hecho, solo toma el valor de un digito, si es 10 lo convierte en 1
                    count += 1
            count += 1
    return res/cant
        

def estudiantes(notas_de_estudiantes:list[str])->list[str]:
    lu : list[str]=[]
    for i in notas_de_estudiantes:
        lu_aux:str=""
        j:int=11
        while i[j] != ")":
            lu_aux += i[j]
            j += 1
        if not pertenece(lu, lu_aux):
            lu.append(lu_aux)
    return lu

def detectar_estudiantes(notas_de_estudiantes:list[str],lu:str)-> list[str]:
    estudiante_lu : list[str]=[]
    for i in notas_de_estudiantes:
        lu_aux:str=""
        j:int=11
        while i[j] != ")":
            lu_aux += i[j]
            j += 1
        if lu_aux == lu:
            estudiante_lu.append(i)
    return estudiante_lu

#print(promedio_estudiante("Ejercicios\Python\Guia_8\estudiantes_notas.csv", "123"))
calcular_promedio_por_estudiante("Ejercicios\Python\Guia_8\estudiantes_notas.csv","Ejercicios\Python\Guia_8\promedio_estudiantes.csv")
