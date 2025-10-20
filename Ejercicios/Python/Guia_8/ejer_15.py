from queue import Queue as Cola
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
def clon_cola (c:Cola[tuple[str, int, bool, bool]])->Cola[tuple[str, int, bool, bool]]:
    aux:Cola[tuple[str, int, bool, bool]]=Cola()
    res:Cola[tuple[str, int, bool, bool]]=Cola()
    while (not c.empty()):
        aux.put(c.get())
    while (not aux.empty()):
        e: tuple[str, int, bool, bool] = aux.get()
        res.put(e)
        c.put(e)
    return res

def atencion_a_clientes(c: Cola[tuple[str, int, bool, bool]]) -> Cola[tuple[str, int, bool, bool]]:
    clon:Cola[tuple[str, int, bool, bool]]=clon_cola(c)
    res:Cola[tuple[str, int, bool, bool]]=Cola()
    aux:Cola[tuple[str, int, bool, bool]]=Cola()
    while(not clon.empty()):
        e:Cola[tuple[str, int, bool, bool]]= clon.get()
        if(e[3]):
            res.put(e)
        else:
            aux.put(e)
    while(not aux.empty()):
        res.put(aux.get())
    return res



p:Cola[tuple[str, int, bool, bool]]=Cola()
p.put(("a",1,True,False))
p.put(("v",1,True,True))
p.put(("c",1,True,False))
p.put(("d",1,True,True))
p.put(("e",1,True,True))
p.put(("f",1,True,False))
clon: Cola[tuple[str, int, bool, bool]]= clon_cola(p)

while(not clon.empty()):
    print(clon.get())

var:Cola[tuple[str, int, bool, bool]]= atencion_a_clientes(p)
print("**********")


while(not var.empty()):
    print(var.get())