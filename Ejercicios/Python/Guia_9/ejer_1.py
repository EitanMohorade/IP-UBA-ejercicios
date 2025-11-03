
# ============================================
# EJERCICIO 1 — Programa max y tests
# ============================================
# Sea el siguiente programa:
def max(x: int, y: int) -> int:
    # L1
    result: int = 0
    # L2
    if x < y:
        # L3
        result = y
    else:
        # L4
        result = x
    # L5
    return result


# -------------------------
# Casos de test:
# -------------------------
# test1:
#   Entrada: x = 0, y = 0
#   Resultado esperado: result = 0
#
# test2:
#   Entrada: x = 0, y = 1
#   Resultado esperado: result = 1
#
# -------------------------
# Preguntas del ejercicio:
# -------------------------
# 1. Describir el diagrama de control de flujo (control-flow graph) del programa max.
# 2. Detallar qué líneas del programa cubre cada test.
# 
#   Test | L1 | L2 | L3 | L4 | L5
#   ------------------------------
#   test1 | X | X  | ?  | X  | X
#   test2 | X | X  | X  | ?  | X
#
# 3. Detallar qué decisiones (branches) del programa cubre cada test.
# 
#   Test | L2-True | L2-False
#   --------------------------
#   test1 | ? |X
#   test2 | X | ?
#
# 4. Decidir si la afirmación es verdadera o falsa:
#    “El test suite compuesto por test1 y test2 cubre el 100% de las líneas del programa
#     y el 100% de las decisiones (branches) del programa”. Justificar.
#la afirmacion es cierta ya que en las decisiones if else las recorren en true y false el test1 y test2, por lo que tambien recorre todas las lineas