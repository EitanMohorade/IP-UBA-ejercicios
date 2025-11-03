
# ============================================
# EJERCICIO 2 — Programa min y análisis de tests
# ============================================
# Especificación:
# problema min (in x: Z, in y: Z) : Z {
#     requiere: {True}
#     asegura: {(x < y → result = x) ∧ (x ≥ y → result = y)}
# }

# Implementación:
def min(x: int, y: int) -> int:
    # L1
    result: int = 0
    # L2
    if x < y:
        # L3
        result = x
    else:
        # L4 (defecto: debería ser "result = y")
        result = x
    # L5
    return result


# -------------------------
# Casos de test:
# -------------------------
# minA:
#   Entrada: x = 0, y = 1
#   Salida esperada: 0
#
# minB:
#   Entrada: x = 1, y = 1
#   Salida esperada: 1
#
# -------------------------
# Preguntas del ejercicio:
# -------------------------
# 1. Describir el diagrama de control de flujo (control-flow graph) del programa min.
# 2. ¿La ejecución del test suite resulta en la ejecución de todas las líneas del programa min?
#si minA  recorre camino true y minB el false
# 3. ¿La ejecución del test suite resulta en la ejecución de todas las decisiones (branches) del programa?
# si
# 4. ¿Es el test suite capaz de detectar el defecto de la implementación del problema de encontrar el mínimo?
# no, para que lo detecte se tuvo que haber creado otro test en el que "y" sea el menor
# 5. Agregar nuevos casos de test y/o modificar los existentes para que el test suite detecte el defecto.
# minC:
#   Entrada: x = 2, y = 1
#   Salida esperada: 1
#   debe ser un assertFalse para q el test este bien implementado y de correcto