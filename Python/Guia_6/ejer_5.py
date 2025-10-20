from ejer_2 import es_par
# ============================================================
# EJERCICIO 5
# ============================================================
# Implementar los siguientes problemas con alternativa condicional (if / else):
#
# 1. devolver_el_doble_si_es_par(numero): devuelve el doble del número si es par, el mismo número si no.
def devolver_el_doble_si_es_par(num:int)->int:
    if(es_par(num)):
        return num*2
    return num
# 2. devolver_valor_si_es_par_sino_el_que_sigue(numero): devuelve el mismo número si es par, y el siguiente si es impar.
def devolver_valor_si_es_par_sino_el_que_sigue (num:int) -> int:
    if(es_par(num)):
        return num
    return num+1
# 3. devolver_el_doble_si_es_par_el_triple_si_es_multiplo9(numero): doble si es par, triple si es múltiplo de 9.
def devolver_el_doble_si_es_multiplo_de_3_el_triple_si_es_multiplo_de_9 (num:int)-> int:
    if((num%3)==0 and (num%9) != 0):
        return 2*num
    elif ((num%9) == 0):
        return 3*num
    return num
# 4. lindo_nombre(nombre): si el nombre tiene 5 letras o más devuelve "Tu nombre tiene muchas letras", si no, "Tu nombre tiene menos de 5 letras".
def lindo_nombre(nombre:str)->str:
    if(len(nombre) >= 5):
        return "nombre muy largo!!!!#!#!31"
    return "nombre con menos de 5 letras"
# 5. elRango(numero): imprime “Menor a 3”, “Entre 10 y 20” o “Mayor a 20” según corresponda.
def el_rango(n:int)->str:
    if(n<5):
        return "menor a 5"
    elif (n>=10 and n<=20):
        return "entre 10 y 20"
    return "mayor a 20"
# 6. jubilacion(sexo, edad): imprime “Andá de vacaciones” si corresponde jubilarse, o “Te toca trabajar” si no.
def vacaciones_o_trabajo(sexo:chr, edad:int)->str:
    if(sexo == 'F'):
        if(edad<65 and edad>18):
            return "a trabajar"
        return "a vacacionar"
    if(edad<60 and edad>18):
        return "a trabajar"
    return "a vacacionar"