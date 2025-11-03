

# ============================================
# EJERCICIO 10 — Programa mcd (máximo común divisor)
# ============================================
# Implementación:
def mcd(x: int, y: int) -> int:
    # L1 requiere: x e y no negativos
    # L2
    tmp: int = 0
    # L3
    while y != 0:
        # L4
        tmp = x % y
        # L5
        x = y
        # L6
        y = tmp
    # L7
    return x


# Preguntas:
# 1. Describir el grafo de control de flujo.
# 2. Escribir un test suite que ejecute todas las líneas y branches.
#    def test_mcd_A():
#        assert mcd(48, 18) == 6
#
#    def test_mcd_B():
#        assert mcd(7, 0) == 7
#
#    def test_mcd_C():
#        assert mcd(0, 5) == 5