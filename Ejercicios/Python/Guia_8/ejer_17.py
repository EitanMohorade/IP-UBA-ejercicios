# Ejercicio 17 - Guía Práctica 8
# Sistema de historial de navegación por usuario.
#
# Diccionario: historiales[usuario] = Pila[str]
#
# problema visitar_sitio(inout historiales, in usuario: str, in sitio: str)
# requiere: Strings no vacíos
# asegura: agrega 'sitio' a la pila de 'usuario', creándola si no existía
#
# problema navegar_atras(inout historiales, in usuario: str) : str
# requiere: usuario existe y su pila no está vacía
# asegura: devuelve el tope de la pila y lo elimina.
#
# Ejemplo:
#   visitar_sitio(historiales, "Usuario1", "google.com")
#   visitar_sitio(historiales, "Usuario1", "facebook.com")
#   navegar_atras(historiales, "Usuario1")
