# ============================================
# EJERCICIO 8 — Programa mult10
# ============================================
# Especificación:
# problema mult10 (in x: Z) : Z {
#     requiere: {True}
#     asegura: {result = x * 10}
# }

# Implementación:
def mult10(x: int) -> int:
    # L1
    result: int = 0
    # L2
    count: int = 0
    # L3
    while count < 10:
        # L4
        result = result + x
        # L5
        count = count + 1
    # L6
    return result


# Preguntas:
# 1. Describir el grafo de control de flujo.
# 2. ¿La ejecución del test suite resulta en la ejecución de todas las líneas del programa?
#    si. Una llamada a mult10 entra al bucle (ejecuta L4,L5 varias veces) y dsp sale (L6).

# 3. ¿La ejecución del test suite resulta en la ejecución de todas las decisiones (branches) del programa?
#  si. La condición del while toma True durante iteraciones y finalmente False al salir.

# 4. Casos de test (COMENTADOS, estilo pytest) para incluir en el mismo archivo como comentarios:
   # mult10A:
   #   Entrada: x = 3
   #   Salida esperada: 30
   #
   # mult10B:
   #   Entrada: x = 0
   #   Salida esperada: 0
   #
   # Tests (pytest) -- COMENTADOS:
   # import pytest
   #
   # def test_mult10_A():
   #     assert mult10(3) == 30
   #
   # def test_mult10_B():
   #     assert mult10(0) == 0

