# Ejercicio 15. Hospital- Empleado del mes
#  Dado un diccionario con la cantidad de horas trabajadas por empleado, en donde la clave es el ID del empleado y el valor es
#  una lista de las horas trabajadas por d´ıa, queremos saber quienes trabajaron m´as para darles un premio. Se deber´a buscar la o
#  las claves para la cual se tiene el m´aximo valor de cantidad total de horas, y devolverlas en una lista.
#  problema empleados
#  del
#  mes (horas:dicc<Z, seq⟨Z⟩) : seq⟨Z⟩ {
#  requiere: {No hay valores en horas que sean listas vac´ıas.}
#  asegura: {Si ID pertence a res entonces ID pertence a las claves de horas.}
#  asegura: {Si ID pertenece a res, la suma de sus valores de horas es el m´aximo de la suma de elementos de horas de todos
#  los otros IDs.}
#  asegura: {Para todo ID de claves de horas, si la suma de sus valores es el m´aximo de la suma de elementos de horas de
#  los otros IDs, entonces ID pertenece a res.}
#  }