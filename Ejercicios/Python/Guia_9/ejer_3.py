
# ============================================
# EJERCICIO 3 — Programa sumar
# ============================================
# Especificación:
# problema sumar (in x: Z, in y: Z) : Z {
#     requiere: {True}
#     asegura: {result = x + y}
# }

# Implementación:
def sumar(x: int, y: int) -> int:
    # L1
    result: int = 0
    # L2
    result = result + x
    # L3
    result = result + y
    # L4
    return result


# Preguntas:
# 1. Describir el diagrama de control de flujo (control-flow graph) del programa sumar.
# 2. Escribir un conjunto de casos de test (test suite) que ejecute todas las líneas del programa.
# OBSERVACION: con un test solo ya recorreria todas las lineas ya que no hay decisiones.

# test_sumar_ambos_positivos
# x=1 y=1
# res= 2

# test_sumar_ambos_negativos
# x=-1 y=-1
# res= -2

# test_sumar_positivo_negativo
# x=1 y=-1
# res= 0

# test_sumar_uno_0
# x=1 y=0
# res= 1