# ============================================================
# EJERCICIO 1 - Recorrido y búsqueda en secuencias
# ============================================================
# Implementar las siguientes funciones sobre secuencias (listas).
# Probar distintas formas de recorrido y de uso de funciones de Python.
#
# 1. pertenece(s, e): devuelve True si el elemento e aparece en la lista s.
#    Implementar al menos 3 versiones diferentes.
def perteneceV1(s:list, e)-> bool:
    for item in range(0, len(s),1):
        if(s[item] == e):
            return True
    return False

def perteneceV2(s:list, e)-> bool:
    i:int = 0
    while(len(s)>i):
        if (s[i] == e):
            return True
        i += 1

def perteneceV3(s:list, e)-> bool:
    return s.index(e) != None

# 2. divide_a_todos(s, e): devuelve True si e divide a todos los elementos de s.
#    Requiere que e != 0.
def divide_a_todos(s:list, e:int)->bool:
    for item in range(0,len(s)):
        if (s[item]%e != 0):
            return False
    return True

# 3. suma_total(s): devuelve la suma de todos los elementos de s.
#    No usar la función sum().
def suma_total(s:list) -> int:
    res: int = 0
    for item in range(0,len(s)):
        res += s[item]
    return res

# 4. maximo(s): devuelve el mayor número de la lista.
#    No usar la función max().
def maximo(s:list)->int:
    res: int = s[0]
    for item in range(0,len(s)):
        if (s[item] >= res):
            res = s[item]
    return res

# 5. minimo(s): devuelve el menor número de la lista.
#    No usar la función min().
def minimo(s:list)->int:
    res: int = s[0]
    for item in range(0,len(s)):
        if (s[item] <= res):
            res = s[item]
    return res


# 6. ordenados(s): devuelve True si los elementos de s están en orden creciente.
def ordenados(s:list)-> bool:
    for item in range(1,len(s)):
        if (s[item] < s[item-1]):
            return False
    return True

# 7. pos_maximo(s): devuelve el índice del mayor elemento de s.
#    Si la lista está vacía, devuelve -1.
#    Si hay varios máximos, devuelve la primera aparición.
def pos_maximo(s:list)->int:
    if(len(s)!=0):
        return s.index(maximo(s))
    return -1
# 8. pos_minimo(s): devuelve el índice del menor elemento de s.
#    Si la lista está vacía, devuelve -1.
#    Si hay varios mínimos, devuelve la última aparición.
def pos_minimo(s:list)->int:
    if(len(s)!=0):
        return s.index(minimo(s))
    return -1

# 9. long_mayor_a_siete(s): devuelve True si alguna palabra de la lista
#    tiene longitud mayor a 7.
def long_mayor_a_siete(s:list)->bool:
    for item in range (0, len(s)):
        if (len(s[item])>= 7):
            return True
    return False

# 10. es_palindroma(s): devuelve True si la cadena s es igual a su reverso.
def es_palindroma(s:list)-> bool:
    for item in range(0, len(s)):
        if(s[item] != s[len(s)-item-1]):
            return False
    return True

# 11. iguales_consecutivos(s): devuelve True si hay 3 números iguales consecutivos.
def iguales_consecutivos(s:list)-> bool:
    for item in range(0,len(s)):
        if(s[len(s)-1-item] == s[len(s)-2-item] == s[len(s)-3-item] ):
            return True
    return False


# 12. vocales_distintas(s): devuelve True si el string tiene al menos
#    3 vocales distintas ('a', 'e', 'i', 'o', 'u').
#auxiliar
def eliminar_x_elemento(s:list, x)->list:
    for item in range(0,len(s)):
        if(perteneceV1(s, x)):
            s.remove(x)
    return s

def vocales_distintas(s:list)->bool:
    vocales:list = ['a','e','i','o','u']
    cantidad_vocales_distintas: int = 0
    for item in range (0, len(vocales)):
        if (perteneceV1(s,vocales[item])):
            eliminar_x_elemento(s,vocales[item])
            cantidad_vocales_distintas += 1
    if(cantidad_vocales_distintas >= 3):
        return True
    return False
# 13. pos_secuencia_ordenada_mas_larga(s):
#    devuelve la posición donde empieza la subsecuencia ordenada más larga.
#    Si hay empate, devuelve la primera que aparece.
def pos_secuencia_ordenada_mas_larga(s:list)->int:
    return 1

# 14. cantidad_digitos_impares(s):
#    recibe una lista de enteros no negativos y devuelve
#    la cantidad total de dígitos impares entre todos ellos.

#auxiliar
def separar_en_digitos(num:int)->list:
    res:list=[]
    while(num>0):
        res.append(num%10)
        num = num // 10
    return res

print(separar_en_digitos(214))

def cantidad_digitos_impares(s:list)->int:
    res : int = 0
    for item in range(0,len(s)):
        if(s[item]%2 != 0):
            res +=1
    return res
