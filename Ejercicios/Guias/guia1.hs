-- Ejercicio 1.
-- Sean p y q variables proposicionales.
-- ¿Cuáles de las siguientes expresiones son fórmulas bien formadas?
-- a) (p q)
-- b) p q True
-- c) (p
-- d) (p)
-- e) (p q)
-- f) (True True True)

-- Ejercicio 2.
-- Determinar el valor de verdad de las siguientes fórmulas:
-- a) (a b)
-- b) (c (y x) b)
-- c) (c y)
-- d) ((c y) (c y))
-- e) ((c y) (x b))
-- f) (((c y) (x b)) (c (y x) b))
-- g) (c y)
-- h) (p False)
-- i) (p = q)
-- Casos:
-- 1) a, b, c verdaderos; x, y falsos.
-- 2) a, b, c falsos; x, y verdaderos.

-- Ejercicio 3.
-- Usando tablas de verdad, determinar si las fórmulas son tautologías,
-- contradicciones o contingencias:
-- a) (p p)
-- b) (p p)
-- c) ((p q) (p q))
-- d) ((p q) p)
-- e) ((p q) (p q))
-- f) ((p q) (p q))
-- g) (p p)
-- h) ((p q) p)
-- i) (p (q r)) ((p q) (p r))
-- j) (p (q r)) ((p q) (p r))

-- Ejercicio 4.
-- Relación de fuerza de fórmulas (más fuerte / más débil).
-- a) True, False
-- b) (p q), (p q)
-- c) True, True
-- d) p, (p q)
-- e) False, False
-- f) p, (p q)
-- g) p, q
-- h) p, (p q)

-- Ejercicio 5.
-- ¿Cuál es la fórmula proposicional más fuerte y cuál la más débil
-- de las que aparecen en el ejercicio anterior?

-- Ejercicio 6.
-- Demostrar mediante tablas de verdad las reglas de equivalencia:
-- a) (False p) False  (Dominación de la conjunción)
-- b) (True p) True    (Dominación de la disyunción)
-- c) (True p) p       (Neutro de la conjunción)
-- d) (False p) p      (Neutro de la disyunción)
-- e) (p p) p          (Idempotencia conjunción)
-- f) (p p) p          (Idempotencia disyunción)
-- g) (p) True         (Inversa disyunción)
-- h) (p) False        (Inversa conjunción)
-- i) (p p)            (Doble negación)
-- j) (p (p q)) p      (Absorción conjunción)
-- k) (p (p q)) p      (Absorción disyunción)
-- l) (p q) (p q)      (De Morgan conjunción)
-- m) (p q) (p q)      (De Morgan disyunción)
-- n) (p q) (q p)      (Conmutatividad conjunción)
-- n) (p q) (q p)      (Conmutatividad disyunción)
-- o) (p (q r)) ((p q) r) (Asociatividad conjunción)
-- p) (p (q r)) ((p q) r) (Asociatividad disyunción)
-- q) (p (q r)) ((p q) (p r)) (Distributividad conjunción)
-- r) (p (q r)) ((p q) (p r)) (Distributividad disyunción)
-- s) (p q) (q p)      (Contraposición)
-- t) (p q) (p q)      (Implicación material)
-- u) (p q) ((p q) (q p)) (Equivalencia material)

-- Ejercicio 7.
-- Simplificar usando equivalencias. Indicar regla usada.
-- a) ((p p) p)
-- b) (p q)
-- c) (((p (p q)) q) (p (p q)))
-- d) (p (p q))
-- e) (((p q) (p q)) (p p))

-- Ejercicio 8.
-- Determinar equivalencia entre pares de fórmulas.
-- a) ((p p) p) p      ≡ True
-- b) ((p q) (p q))    ≡ (p q)
-- c) (p q) (p r)      ≡ p (q r)
-- d) (p) ((p q) q)
-- e) ((True p) (p False)) ≡ (p q)
-- f) (p (p q))        ≡ (p q)
-- g) (p (q s))        ≡ (s (p q))
-- h) (p (q (q r)))    ≡ ((p q) (p (q r)))

-- Ejercicio 9.
-- Demostrar que cualquier fórmula con ¬, ∧, ∨, →, ↔
-- puede expresarse solo con ¬ y ∧.

-- Ejercicio 10.
-- Variables proposicionales:
-- f = fin de semana
-- e = Juan estudia
-- m = Juan escucha música
-- a) Escribir proposiciones:
--   - Si es fin de semana, Juan estudia o escucha música, pero no ambas.
--   - Si no es fin de semana entonces Juan no estudia.
--   - Cuando Juan estudia los fines de semana, lo hace escuchando música.
-- b) Asumiendo las anteriores, ¿se deduce que Juan no estudia?

-- Ejercicio 11.
-- Si todos conocen a Juan entonces todos conocen a Camila.
-- Si todos conocen a Juan, y todos conocen a Camila, entonces conocen a Gonzalo.
-- Pregunta: ¿Se sigue que si todos conocen a Juan, entonces todos conocen a Gonzalo?

-- Ejercicio 12.
-- Laly y Leo: siempre que duermen en lo de su abuela, vuelven con galletitas.
-- Un día llegan con galletitas → ¿podemos concluir que durmieron en lo de la abuela?
-- Identificar la falacia de afirmar el consecuente.

--------------------------------
-- 2. Lógica Ternaria (V/F/I) --
--------------------------------

-- Ejercicio 13.
-- Determinar valor de verdad (en R):
-- a) 5 > 0
-- b) 1 = 1
-- c) (5+3=8) 1=2
-- d) 1/0 = 1/0
-- e) 0/1 = 0
-- f) 1/0 = 0

-- Ejercicio 14.
-- Diferencia entre operador L y operador ∧. Describir tabla de verdad.

-- Ejercicio 15.
-- Diferencia entre operador L y operador ∨. Describir tabla de verdad.

-- Ejercicio 16.
-- Diferencia entre operador L y operador →. Describir tabla de verdad.

-- Ejercicio 17.
-- Determinar valores de las siguientes fórmulas en lógica ternaria:
-- a) (x L b)
-- b) ((c L (y L a)) L b)
-- c) (c L y)
-- d) ((c L y) (c L y))
-- e) ((c L y) L (a L b))
-- f) (((c L y) L (a L b)) (c L (y L a) L b))
-- g) (c L y)
-- Casos: b, c verdaderos; a falso; x, y indefinidos.

-- Ejercicio 18.
-- Determinar valores de las fórmulas cuando:
-- p = verdadero, q = falso, r = indefinido.
-- a) ((9=9) L p)
-- b) ((3=2) L (p L q))
-- c) ((3 < 4) L ((3=4) L r))
-- d) ((3 > 9) L (r L (q L p)))
-- e) ((p L q) L r)
-- f) ((p L q) L r)
-- g) ((p L r) L ((q L q) L (p L (q L r))))
-- h) ((p L q) L (1=0))
-- i) (p L ((5+7+3=0) (22-1 > 3)))
-- j) ((p L r) L r)
-- k) ((p L (1 > log 0)) (22=4 L (p L q)))
-- l) ((p L (q L r)) L ((p L q) L (p L r)))

-- Ejercicio 19.
-- Proponer fórmulas (usando p, q, r) que nunca se indefinan y cumplan:
-- a) Al menos una verdadera.
-- b) Ninguna verdadera.
-- c) Exactamente una verdadera.
-- d) Solo p y q verdaderas.
-- e) No todas al mismo tiempo verdaderas.
-- f) r verdadera.

-----------------------------------------------
-- 3. Fórmulas del Lenguaje de Especificación --
-----------------------------------------------

-- Ejercicio 20.
-- Indicar cuáles son fórmulas bien formadas:
-- a) ((1=0) (x=y))
-- b) (x+10) = y
-- c) (x y)
-- d) (z True) (y=x)
-- e) (z=0) (z=1)
-- f) y + (y < 0)

-- Ejercicio 21.
-- La fórmula ((3+7=8) True) es bien formada. ¿Por qué?
-- Justificar.
