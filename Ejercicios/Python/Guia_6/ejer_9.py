# ============================================================
# EJERCICIO 9
# ============================================================
# Analizar el siguiente código y responder:
#
# def rt(x: int, g: int) -> int:
#     g = g + 1
#     return x + g
#
# g: int = 0
# def ro(x: int) -> int:
#     global g
#     g = g + 1
#     return x + g
#
# Preguntas:
# 1. ¿Cuál es el resultado de evaluar tres veces seguidas ro(1)?
# 2. ¿Cuál es el resultado de evaluar tres veces seguidas rt(1, 0)?
# 3. Realizar ejecución simbólica en ambas funciones.
# 4. Dar la especificación (entrada/salida esperada) de cada función.