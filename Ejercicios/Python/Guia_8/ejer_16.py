# Ejercicio 16 - Guía Práctica 8
# Implementar una solución para el siguiente problema:
#
# problema calcular_promedio_por_estudiante(in notas: seq⟨seq⟨Char⟩ × R⟩) : Diccionario⟨seq⟨Char⟩, R⟩
# requiere: los nombres no son cadenas vacías
# requiere: las notas están entre 0 y 10
# asegura: cada clave de res es un nombre presente en notas
# asegura: el valor de cada clave es el promedio de sus notas
#
# Ejemplo:
#   notas = [("Sole", 9.5), ("Maxi", 8.0), ("Sole", 9.0)]
#   → {"Sole": 9.25, "Maxi": 8.0}
