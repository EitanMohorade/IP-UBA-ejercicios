
# ============================================================
# EJERCICIO 2 - Recorrido: filtrando, modificando y procesando secuencias
# ============================================================
# Implementar las siguientes funciones sobre listas o strings.
#
# 1. ceros_en_posiciones_pares(s):
#    modifica la lista original reemplazando por 0 los elementos en posiciones pares.
def es_par(n:int)->bool:
    return n%2 == 0
def ceros_en_posiciones_pares(s:list[int])->None:
    for i in s:
        if(es_par(i)):
            i = 0
# 2. ceros_en_posiciones_pares2(s):
#    devuelve una nueva lista igual a la anterior, pero con 0 en las posiciones pares.
def ceros_en_posiciones_pares_V2(s:list[int])->list[int]:
    copia : list[int] = s.copy
    return ceros_en_posiciones_pares(copia)
# 3. sin_vocales(s):
#    devuelve una cadena igual a s pero sin las vocales ('a', 'e', 'i', 'o', 'u').
def pertenece(e:str,s:list[str])->bool:
    res: int = 0
    for i in s:
        if(i == e):
            res = 1
    return res == 1
vocales: list[str]=['a', 'e', 'i', 'o', 'u']
def sin_vocales(s:list[str])->list[str]:
    global vocales
    res:list[str]=[]
    for i in s:
        if(not pertenece(i,vocales)):
            res.append(i)
    return res

# 4. reemplaza_vocales(s):
#    devuelve una cadena donde las vocales fueron reemplazadas por un espacio ' '.
def reemplazar_vocales(s:list[str])->list[str]:
    global vocales
    res:list[str]=[]
    for i in s:
        if(pertenece(i, vocales)):
            res.append("-")
        else:
            res.append(i)
    return res

# 5. da_vuelta_str(s):
#    devuelve la cadena invertida.
def dar_vuelta_una_palabra(palabra:str)->str:
    res:str=""
    for i in range(len(palabra),0,-1):
        res += palabra[i-1]
    return res

def da_vuelta_str(s:list[str])-> list[str]:
    res:list[str]=[]
    for i in s:
        res.append(dar_vuelta_una_palabra(i))
    return res
print(da_vuelta_str(["hola","aloh","saludos","uno"]))
# 6. eliminar_repetidos(s):
#    devuelve una cadena con los mismos caracteres que s, pero sin repetir ninguno.
def eliminar_x_elemento(p:str, s:list[str]):
    for i in range(0,len(s)):
        if(s[i]==p):
            s.remove[i]

def eliminar_repetidos(s:list[str])->list[str]:
    res:list[str]=[]
    for i in s:
        eliminar_x_elemento(i,s)
        res.append[i]
    return res