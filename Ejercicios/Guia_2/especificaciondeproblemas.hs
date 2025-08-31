{-
 Formato de especificaciones:
 Departamento de Computaci´on
 Facultad de Ciencias Exactas y Naturales
 Universidad de Buenos Aires
 problema nombreDelProblema (nombreParametroEntrada1: tipoDeDato1, nombreParametro2: tipoDeDato2) : tipoDatoDeSalida {
 requiere: {Una proposici´on que utiliza par´ametros de entrada}
 requiere: {Otra proposici´on que utiliza par´ametros de entrada}
 asegura: {Proposici´on que puede utilizar par´ametros de entrada y salida para hablar del resultado}
 asegura: {Otra proposici´on que puede utilizar par´ametros de entrada y salida para hablar del resultado}
 }

 Ejercicio 1.
 
 Dadas las siguientes especificaciones, dar valores de entrada y salida que cumplan con los requiere y asegura
 respectivamente:
 a) problema duplicar (x: Z) : Z {
 requiere: {True}
 asegura: {resultado es el doble de x}
 }
 b) problema raizCuadrada (x: Z) : R {
 requiere: {x es positivo}
 asegura: {resultado es la ra´ız cuadrada de x}
 }
 c) problema enteroMasCercanoPositivo (x: R) : Z {
 requiere: {True}
 asegura: {resultado es el entero m´as cercano de x}
 asegura: {resultado es positivo}
 }
 d) problema raicesCuadradasUno (s: seq⟨Z⟩) : seq⟨R⟩ {
 requiere: {Todos los elementos de s son positivos}
 requiere: {No hay elementos repetidos en s}
 asegura: {resultado tiene la misma cantidad de elementos que s}
 asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de la
 secuencia s}
 asegura: {El orden de la secuencia resultado es el mismo que en la secuencia s, luego de aplicar el problema
 raizCuadrada}
 }
 e) problema raicesCuadradasDos (s: seq⟨Z⟩) : seq⟨R⟩ {
 requiere: {Todos los elementos de s son positivos}
 requiere: {No hay elementos repetidos en s}
 asegura: {resultado tiene la misma cantidad de elementos que s}
 asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de la
 secuencia s}
 }

f) problema raicesCuadradasTres (s: seq⟨Z⟩) : seq⟨R⟩ {
 requiere: {Todos los elementos de s son positivos}
 requiere: {No hay elementos repetidos en s}
 asegura: {resultado tiene la misma cantidad de elementos que s}
 asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a uno o varios elementos de
 la secuencia s}
 }
 g) problema raicesCuadradasCuatro (s: seq⟨Z⟩) : seq⟨R⟩ {
 requiere: {Existen elementos de s que son positivos}
 requiere: {No hay elementos repetidos en s}
 asegura: {Los elementos de resultado son la salida de aplicar el problema raizCuadrada a todos los elementos de s
 que son positivos}
 }
 h) problema raicesCuadradasCinco (s: seq⟨Z⟩) : seq⟨R⟩ {
 requiere: {Todos los elementos de s son positivos}
 asegura: {Cada posici´on de resultado, donde la posici´on es menor o igual a las de s, es igual a la salida de aplicar
 raizCuadrada al elemento que se encuentra en esa posici´on en s}
 }
 i) problema raicesCuadradasSeis (s: seq⟨Z⟩) : seq⟨R⟩ {
 requiere: {Todos los elementos de s son positivos}
 asegura: {La longitud de resultado es como m´aximo la misma que s}
 asegura: {Cada posici´on de resultado, donde la posici´on es menor o igual a las de s, es igual a la salida de aplicar
 raizCuadrada al elemento que se encuentra en esa posici´on en s}
 }

 Ejercicio 2.
 
 A partir de las especificaciones del Ejercicio 1, responder las siguientes preguntas:
 1. En los problemas raicesCuadradas que utilizan el problema raizCuadrada, ¿Se puede eliminar el requiere “Todos los
 elementos de s son positivos”? Justificar.
 2. ¿Qu´e consecuencia tiene en el resultado la diferencia de asegura entre los problemas raicesCuadradasUno y raicesCuadra
dasDos? Buscar un ejemplo de valor de entrada donde cada problema tenga distinto valor de salida.
 3. De acuerdo con la respuesta del´ıtem anterior, ¿un algoritmo que satisface la especificaci´on de raicesCuadradasUno, tambi´en
 satisface la especificaci´on de raicesCuadradasDos? ¿y al rev´es?
 4. Explicar en palabras las diferencias entre los problemas raicesCuadradasCinco y raicesCuadradasSeis. ¿C´omo influye el
 asegura de longitud m´axima? Dada la entrada s = ⟨3,9,11,15,18⟩, ¿es ⟨√3,√9⟩ una salida v´alida para ambos problemas?
 Y sea la entrada s = ⟨3,9,11⟩, ¿es ⟨√3,√9,√11,√13⟩ una salida v´alida para el problema raicesCuadradasCinco?
 5. ¿Qu´e cambia en el problema raicesCuadradasCuatro agregar un asegura que diga que resultado tiene la misma longitud
 que s? Pensar ejemplos de valores de salida que cambien con este nuevo asegura.
 6. Si los problemas raicesCuadradasDos y raicesCuadradasTres tienen el mismo resultado para la misma entrada (una se
cuencia espec´ıfica de n´umeros), ¿quiere decir que son el mismo problema?
 7. ¿Qu´e ocurre si eliminamos los requiere “no hay repetidos”? Dada la entrada s = ⟨4,1,1⟩, ¿es ⟨2,2,1⟩ una salida v´alida para
 el problema raicesCuadradasDos?

Ejercicio 3.

Dada la siguiente especificaci´on del problema de ordenar una secuencia de enteros, en la que se debe tomar una
 secuencia de n´umeros enteros y devolver los mismos elementos ordenados de menor a mayor:
 problema ordenar (s: seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: {True}
 asegura: {resultado es una secuencia en la cual cada elemento es estrictamente mayor que el anterior}
 }
 responder la siguientes preguntas:
 a) Dada s = ⟨4,3,5⟩ como secuencia de entrada, ¿es resultado = ⟨3,4,5⟩ una soluci´on v´alida seg´un la especificaci´on?
 b) Dado s = ⟨4,3,3,5⟩ como secuencia de entrada, ¿es resultado = ⟨3,3,4,5⟩ una soluci´on v´alida seg´un la especificaci´on?
 Corregir la especificaci´on modificando el requiere.
 c) Si tomamos s = ⟨4,3,5⟩ como secuencia de entrada, ¿es resultado = ⟨3,4⟩ una soluci´on v´alida seg´un la especificaci´on?
 Corregir la especificaci´on modificando el asegura.
 d) Si tomamos s = ⟨4,3,5⟩ como secuencia de entrada, ¿es resultado = ⟨3,4,5,6⟩ una soluci´on v´alida seg´un la especificaci´on?
 Corregir la especificaci´on modificando el asegura.
 e) Dada s = ⟨8,5,7⟩ como secuencia de entrada, ¿es resultado = ⟨1,2,3⟩ una soluci´on v´alida seg´un la especificaci´on?
 f) Escribir una especificaci´on que permita recibir cualquier secuencia de enteros s como par´ametro y garantice que resultado
 contiene el resultado de ordenar correctamente los elementos s de menor a mayor.
 
 Ejercicio 4.
 
 Se desea especificar el problema de reemplazar cada elemento de una secuencia de enteros por su doble y se cuenta
 con la siguiente especificaci´on:
 problema duplicarTodos (s: seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: {True}
 asegura: {resultado tiene la misma cantidad de elementos que s}
 }
 a) ¿Qu´e problemas tiene la especificaci´on dada? Dar ejemplos de valores para resultado que satisfagan la especificaci´on pero no
 sean respuestas correctas.
 b) Indicar cu´al/es de los siguientes asegura deber´ıa/n ser agregado/s a la especificaci´on. Justificar en cada caso por qu´e deber´ıan
 o no ser agregados.
 asegura: {Para cada valor x que pertenece a s, hay alg´un valor en resultado que es la salida de duplicar(x)}
 asegura: {En cada posici´on de resultado, el valor es mayor al valor en esa misma posici´on de s}
 asegura: {En cada posici´on de resultado, el valor es igual a la salida de aplicar duplicar al valor en esa misma posici´on
 de s}
 asegura: {Todos los elementos de resultado son n´umeros pares}
 Nota: el problema duplicar(x) est´a especificado en el Ejercicio 1.

 Ejercicio 5.
 
 (Frecuencia de bondis) A Ciudad Universitaria (CU) llegan 8 l´ıneas de colectivos: 28, 33, 34, 37, 45, 107, 160
 y 166. Con el fin de controlar la frecuencia diaria de cada l´ınea, un grupo de investigaci´on del Departamento de Computaci´on
 instal´o c´amaras y un sistema de reconocimiento de im´agenes en el ingreso al predio. Durante el d´ıa, el sistema identifica el
 n´umero de l´ınea de cada colectivo que ingresa y lo registra en una secuencia ordenada.
 a) Especificar el problema cantidadColectivosDeLinea que a partir de una secuencia de colectivos registrada por el sistema
 de reconocimiento y el n´umero de una l´ınea que llega a CU, devuelva cu´antos colectivos de esa l´ınea ingresaron durante el
 d´ıa.
 b) Especificar el problema lineaConMejorFrecuencia que, a partir de dos n´umeros de l´ıneas y una secuencia registrada por el
 sistema, devuelva cu´al de las dos l´ıneas tiene mejor frecuencia diaria. Sugerencia: utilizar cantidadColectivosDeLinea.

Ejercicio 6.

(Control de Calificaciones en el Departamento de Ciencias)
 En el prestigioso Departamento de Ciencias de una reconocida universidad, un grupo de estudiantes se ha embarcado en su
 jornada acad´emica, cursando diversas materias bajo el cuidadoso seguimiento del cuerpo docente. En este departamento, cada
 estudiante ha sido registrado con su respectivo nombre y apellido, asegur´andose de que no existan duplicados.
 La informaci´on relevante de las cursadas de los estudiantes se encuentra almacenada en un sistema que contiene una secuencia
 de tuplas en formato Materia × Calificaci´on obtenida. Las calificaciones se encuentran en un rango num´erico entre 0 y 10.
 El Departamento ha establecido una pol´ıtica de aprobaci´on y recursado que dicta que si un estudiante aprueba una materia
 con una calificaci´on igual o superior a 4, no deber´a volver a cursarla, quedando esta materia registrada como aprobada en su
 expediente acad´emico. Sin embargo, si no logra alcanzar la calificaci´on m´ınima de aprobaci´on, tendr´a la posibilidad de recursar
 la materia en un futuro intento.
 Adem´as, existe en el sistema una estructura de datos llamada CalificacionesDelDC que contiene la informaci´on de los estu
diantes y las calificaciones en sus cursadas. Esta estructura es una secuencia de tuplas en el formato Alumno×Cursada, donde
 Alumno es el nombre y apellido del estudiante y Cursada es la secuencia de tuplas mencionada previamente.
 Considerando esta informaci´on y los siguientes renombres de tipos:
 Renombre Alumno = String
 Renombre Materia = String
 Renombre Cursada = seq⟨Materia×R⟩
 Renombre CalificacionesDelDC = seq⟨Alumno×Cursada⟩
 a) Especificar problema promedioDeAlumno (alumno: Alumno, calificaciones: CalificacionesDelDC) : R
 b) Especificar el problema que, dado el listado de materias cursadas por un estudiante, indique en qu´e materia tuvo mayor
 calificaci´on. ¿C´omo se debe modificar la especificaci´on para devolver el listado de materias en las cuales tuvo mejor calificaci´on?
 c) Especificar el problema que, dada una materia y las calificaciones del DC, devuelve todos los estudiantes que cursaron y
 aprobaron esa materia. ¿C´omo debe modificarse la especificaci´on para que los nombres se devuelvan en orden alfab´etico?,
 ¿este cambio reduce o ampl´ıa la cantidad de programas que resolver´ıan el problema?
 d) Especificar el problema de devolver una secuencia con los promedios de todos los estudiantes.
 Principio de sustituci´on

 Ejercicio 7.
 
 Contamos con las siguientes especificaciones del problema pares:
 problema pares1 (s: seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: {s no tiene elementos repetidos}
 asegura: {Los elementos de resultado son pares y pertenecen a s}
 asegura: {Los elementos de s que son pares, pertenecen a resultado}
 asegura: {resultado no tiene elementos repetidos}
 }
 problema pares2 (s: seq⟨Z⟩) : seq⟨Z⟩ {
 requiere: {s no tiene elementos repetidos}
 asegura: {Los elementos de resultado son pares y pertenecen a s}
 asegura: {Los elementos de s que son pares, pertenecen a resultado}
 asegura: {resultado no tiene elementos repetidos}
 asegura: {resultado est´a ordenada de manera creciente}
 }
 a) Si contamos con un algoritmo P que satisface pares1, ¿satisface P la especificaci´on pares2? Justificar.
 b) Si contamos con un algoritmo P que satisface pares2, ¿satisface P la especificaci´on pares1? Justificar.
 c) ¿Cu´al es la relaci´on de fuerza entre la postcondici´on de pares1 y la de pares2?


Ejercicio 8.

Contamos con las siguientes especificaciones del problema sumarAbsMayorA5:
 problema sumarAbsMayorA5-version1 (s: seq⟨Z⟩) : Z {
 requiere: {True}
 asegura: {resultado es la sumatoria de todos los elementos de s cuyo valor absoluto es mayor a 5}
 }
 problema sumarAbsMayorA5-version2 (s: seq⟨Z⟩) : Z {
 requiere: {Todos los elementos de s son positivos}
 asegura: {resultado es la sumatoria de todos los elementos de s cuyo valor absoluto es mayor a 5}
 }
 problema sumarAbsMayorA5-version3 (s: seq⟨Z⟩) : Z {
 requiere: {Todos los elementos de s son mayores a 10}
 asegura: {resultado es la sumatoria de todos los elementos de s cuyo valor absoluto es mayor a 5}
 }
 a) ¿Cu´al es la relaci´on de fuerza entre los requiere de cada especificaci´on?
 b) ¿Cu´al de las especificaciones tiene el dominio m´as restringido y cu´al menos?
 c) Desde el punto de vista de un programador, ¿qu´e especificaci´on es m´as f´acil de implementar? Justificar.
 d) Desde el punto de vista de un usuario, ¿qu´e contrato es m´as conveniente? Justificar
-}