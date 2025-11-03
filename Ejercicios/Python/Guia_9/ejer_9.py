

# ============================================
# EJERCICIO 9 — Programa sumar con while y signos
# ============================================
# Especificación:
# problema sumar (in x: Z, in y: Z) : Z {
#     requiere: {True}
#     asegura: {result = x + y}
# }

# Implementación:
def sumar_signo(x: int, y: int) -> int:
    # L1
    sumando: int = 0
    # L2
    abs_y: int = 0
    # L3
    if y < 0:
        # L4
        sumando = -1
        # L5
        abs_y = -y
    else:
        # L6
        sumando = 1
        # L7
        abs_y = y
    # L8
    result: int = x
    # L9
    count: int = 0
    # L10
    while count < abs_y:
        # L11
        result = result + sumando
        # L12
        count = count + 1
    # L13
    return result


# Preguntas:
# 1. Describir el grafo de control de flujo.
# 2. ¿La ejecución del test suite resulta en la ejecución de todas las líneas?
#si, con tests para y>0, y<0 y y=0 se ejecutan todas las líneas.
#
# 3. ¿La ejecución del test suite resulta en la ejecución de todos los decisions (branches)?
# si. y<0 cubre la rama True del if; y>=0 la rama False; y=0 cubre while False; y>0 cubre while True.
#
# 4. Casos de test:
#    sumarA:
#      Entrada: x = 5, y = 3
#      Salida esperada: 8
#
#    sumarB:
#      Entrada: x = 5, y = -2
#      Salida esperada: 3
#
#    sumarC:
#      Entrada: x = 5, y = 0
#      Salida esperada: 5
#
#    def test_sumar_A():
#        assert sumar_signo(5, 3) == 8
#
#    def test_sumar_B():
#        assert sumar_signo(5, -2) == 3
#
#    def test_sumar_C():
#        assert sumar_signo(5, 0) == 5

