

# ============================================
# EJERCICIO 5 — Programa signo
# ============================================
# Especificación:
# problema signo (in x: R) : Z {
#     requiere: {True}
#     asegura: {(result = 0 ∧ x = 0) ∨ (result = −1 ∧ x < 0) ∨ (result = 1 ∧ x > 0)}
# }

# Implementación:
def signo(x: float) -> int:
    # L1
    result: int = 0
    # L2
    if x < 0:
        # L3
        result = -1
    # L4
    elif x > 0:
        # L5
        result = 1
    # L6
    return result


# Preguntas:
# 1. Describir el grafo de control de flujo.
# 2. Escribir un test suite que ejecute todas las líneas.

# test_menor_a_0
# x=-1
# res_esperado = -1

# test_mayor_a_0
# x=1
# res_esperado = 1

# test_igual_a_0
# x=0
# res_esperado = 0

# 3. ¿El test suite ejecuta todos los branches del programa?

# si