

# ============================================
# EJERCICIO 12 — Programa multByAbs
# ============================================
# Especificación:
# problema multByAbs (in x: Z, in y: Z) : Z {
#     asegura: {result = x * |y|}
# }

def multByAbs(x: int, y: int) -> int:
    # L1
    abs_y: int = fabs_int(y)  # usa el ejercicio anterior
    # L2
    if abs_y < 0:
        # L3
        return -1
    else:
        # L4
        result: int = 0
        # L5
        i: int = 0
        # L6
        while i < abs_y:
            # L7
            result = result + x
            # L8
            i += 1
        # L9
        return result


# Preguntas:
# 1. Describir el grafo de control de flujo.
# 2. Detallar qué líneas o branches no pueden ser cubiertos y por qué.
# 3. Escribir un test suite que cubra todas las líneas y branches posibles.

