from queue import LifoQueue as Pila
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


def visitar_sitio(d: dict[str, Pila[str]], u: str, sitio: str):
    aux:Pila[int] = Pila()
    
    if(u in d.keys()):
        u.put(sitio)
    else:
        aux.put(sitio)
        d[u] = aux

def navegar_atras(d: dict[str, Pila[str]], u: str) -> str:
    return d[u].get()


p1:Pila[str]=Pila()
p1.put("yahoo")
p1.put("rinkon")
p1.put("wiki")

p2:Pila[str]=Pila()
p2.put("wiki")
p2.put("wiki")
p2.put("wiki")

p3:Pila[str]=Pila()
p3.put("wiki")
p3.put("wiki")
p3.put("wiki")

historiales: dict[str, Pila[str]] ={
    "mario": p1,
    "olga": p2,
    "tristanaDelLol": p3
    }

print(historiales.items())
visitar_sitio(historiales, "pepe", "yt")
print(historiales.items())

print(navegar_atras(historiales, "mario"))

print("********************")

while not p1.empty():
    print(p1.get())