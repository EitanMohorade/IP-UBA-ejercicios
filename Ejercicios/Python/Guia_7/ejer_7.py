# ============================================================
# EJERCICIO 7 - Programas interactivos con secuencias
# ============================================================
# Implementar las siguientes funciones que interactúan con el usuario:
#
# 1. ingresar_estudiantes():
#    solicita nombres al usuario hasta que escriba "listo" o presione ENTER vacío.
#    Devuelve la lista de nombres ingresados.
#
# 2. historial_monedero():
#    simula el historial de un monedero electrónico (ej: SUBE).
#    Opciones:
#      "C" → cargar crédito
#      "D" → descontar crédito
#      "X" → finalizar simulación
#    Devuelve una lista de tuplas con los movimientos realizados.
#
# 3. juego_siete_y_medio():
#    simula el juego del 7½ con números aleatorios entre 1 y 12 (sin 8 ni 9).
#    Suma puntos según el valor de las cartas:
#       - 10, 11, 12 valen 0.5 puntos.
#    El jugador elige si seguir o plantarse. Pierde si supera 7.5.
#    Devuelve la lista de cartas obtenidas.
#
# 4. analizar_contrasena(pw):
#    analiza la fortaleza de una contraseña y devuelve:
#       "VERDE" → si cumple:
#           longitud > 8, al menos 1 mayúscula, 1 minúscula y 1 número.
#       "ROJA" → si longitud < 5.
#       "AMARILLA" → en los demás casos.