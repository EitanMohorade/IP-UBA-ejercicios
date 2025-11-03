#  Ejercicio 13. Hospital- Atenci´on por Guardia
#  Desde el Hospital Fernandez nos pidieron solucionar una serie de problemas relacionados con la informaci´on que maneja sobre
#  los pacientes y el personal de salud. En primer lugar debemos resolver en qu´e orden se deben atender los pacientes que llegan a
# la guardia. En enfermer´ıa, hay una primera instancia que clasifica en dos colas a los pacientes: una urgente y otra postergable
#  (esto se llama hacer triage). A partir de dichas colas que contienen la identificaci´on del paciente, se pide devolver una nueva cola
#  seg´un la siguiente especificaci´on.
#  problema orden
#  de
#  atencion (in urgentes: cola<Z>, in postergables: cola<Z>) : cola<Z> {
#  requiere: {No hay elementos repetidos en urgentes.}
#  requiere: {No hay elementos repetidos en postergables.}
#  requiere: {La intersecci´on entre postergables y urgentes es vac´ıa.}
#  requiere: {|postergables| = |urgentes|.}
#  asegura: {No hay repetidos en res.}
#  asegura: {res es permutaci´on de la concatenaci´on de urgentes y postergables.}
#  asegura: {Si urgentes no es vac´ıa, en la cabeza de res hay un elemento de urgentes.}
#  asegura: {En res no hay dos seguidos de urgentes.}
#  asegura: {En res no hay dos seguidos de postergables.}
#  asegura: {Para todo c1 y c2 de tipo ”urgente” pertenecientes a urgentes si c1 aparece antes que c2 en urgentes entonces
#  c1 aparece antes que c2 en res.}
#  asegura: {Para todo c1 y c2 de tipo ”postergable” pertenecientes a postergables si c1 aparece antes que c2 en postergables
#  entonces c1 aparece antes que c2 en res.}
#  }