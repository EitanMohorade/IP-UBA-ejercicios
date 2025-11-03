

# ============================================
# EJERCICIO 7 — Programa fabs (versión corregida)
# ============================================
# Especificación:
# problema fabs (in x: Z) : Z {
#     requiere: {True}
#     asegura: {result = |x|}
# }

# Implementación:
def fabs_int(x: int) -> int:
    # L1
    if x < 0:
        # L2
        return -x
    else:
        # L3
        return x


# Preguntas:
# 1. Describir el grafo de control de flujo.
# 2. Escribir un test suite que ejecute todas las líneas y branches.

# test_menor_a_0
# x= -1
# res_esperado= 1

# test_mayor_a_0
# x= 1
# res_esperado= 1


#no hace falta este ultimo test pero seria lo mas optimo tenerlo
# test_igual_a_0
# x= 0
# res_esperado= 0


