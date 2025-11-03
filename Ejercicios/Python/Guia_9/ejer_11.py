


# ============================================
# EJERCICIO 11 — Programa triangle
# ============================================
# Retorna:
# 1 = equilátero
# 2 = isósceles
# 3 = escaleno
# 4 = inválido

def triangle(a: int, b: int, c: int) -> int:
    # L1
    if (a <= 0 or b <= 0 or c <= 0):
        # L2
        return 4  # inválido
    # L3
    if not ((a + b > c) and (a + c > b) and (b + c > a)):
        # L4
        return 4  # inválido
    # L5
    if a == b and b == c:
        # L6
        return 1  # equilátero
    # L7
    if a == b or b == c or a == c:
        # L8
        return 2  # isósceles
    # L9
    return 3  # escaleno


# Preguntas:
# 1. Describir el grafo de control de flujo.
# 2. Escribir un test suite que ejecute todas las líneas y branches.
