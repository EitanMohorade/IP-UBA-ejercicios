

# ============================================
# EJERCICIO 6 — Programa fabs (con defecto)
# ============================================
# Especificación:
# problema fabs (in x: R) : R {
#     requiere: {True}
#     asegura: {result = |x|}
# }

# Implementación:
def fabs(x: float) -> float:
    # L1
    result: float = 0
    # L2
    if x < 0:
        # L3
        result = -x
    # Falta el caso x >= 0 (defecto)
    # L4
    return result


# Preguntas:
# 1. Describir el grafo de control de flujo.
# 2. Escribir un test suite que ejecute todas las líneas.

# test_menor_a_0
# x = -1
# res_esperado = 1

# test_mayor_a_0
# x = 1
# res_esperado = 1
# res = 0

# 3. Escribir un test suite que ejecute todos los branches.

# test_menor_a_0
# x = -1
# res_esperado = 1

# 4. Escribir un test suite que ejecute todas las líneas pero no todos los branches.

# 5. ¿Los test suites detectan el defecto? Si no, modificarlos.
#no los detecta, deberia modificarse el codigo para que sea correcto ya que
# test_mayor_a_0
# x = 1
# res_esperado = 1
# res = 0
def fabsV2(x: float) -> float:
    # L1
    result: float = 0
    # L2
    if x < 0:
        # L3
        result = -x
    else:
        # L4
        result = x
    # L5
    return result