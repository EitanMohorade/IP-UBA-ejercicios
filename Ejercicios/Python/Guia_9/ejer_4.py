

# ============================================
# EJERCICIO 4 — Programa restar
# ============================================
# Especificación:
# problema restar (in x: Z, in y: Z) : Z {
#     requiere: {True}
#     asegura: {result = x - y}
# }

# Implementación:
def restar(x: int, y: int) -> int:
    # L1
    result: int = 0
    # L2
    result = result + x
    # L3 (defecto: debería ser "result = result - y")
    result = result + y
    # L4
    return result


# Preguntas:
# 1. Describir el diagrama de control de flujo.
# 2. Escribir un test suite que ejecute todas las líneas del programa.
# OBSERVACION: sin decisiones no hace falta muchos test para recorrer todas las lineas.

# test_ambos_positivos
# x=1 y=1
# res esperado= 0
# res que sale = 2

# 3. ¿El test suite detecta el defecto en L3? Si no, modificarlo para hacerlo.

def restarV2(x: int, y: int) -> int:
    # L1
    result: int = 0
    # L2
    result = x - y
    
    return result

# test_ambos_positivos
# x=1 y=1
# res esperado= 0