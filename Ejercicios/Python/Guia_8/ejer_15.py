# Ejercicio 15 - Guía Práctica 8
# Modelar la atención de clientes en un banco usando una cola.
#
# Cada cliente: (nombre_apellido: str, dni: int, cuenta_preferencial: bool, prioridad: bool)
#
# Orden de atención:
#   1. Personas con prioridad (adultos +65, embarazadas, movilidad reducida)
#   2. Clientes preferenciales
#   3. Resto, en orden de llegada.
#
# Parte 1: Dar especificación del problema.
# Parte 2: Implementar
#   atencion_a_clientes(in c: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]
#   que devuelve la cola en el orden de atención.
