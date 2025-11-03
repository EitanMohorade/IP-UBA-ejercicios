# Ejercicio 12. Ta-Te-Ti-Facilito
#  Ana y Beto juegan al Ta-Te-Ti-Facilito. El juego es en un tablero cuadrado de lado entre 5 y 10. Cada jugador va poniendo su
#  f
#  icha en cada turno. Juegan intercaladamente y comienza Ana. Ana pone siempre una ”X” en su turno y Beto pone una ”O” en el
#  suyo. Gana la persona que logra poner 3 fichas suyas consecutivas en forma vertical. Si el tablero est´a completo y no gan´o nadie,
#  entonces se declara un empate. El tablero comienza vac´ıo, representado por ” ” en cada posici´on. Notar que dado que juegan por
#  turnos y comienza Ana poniendo una ”X” se cumple que la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad
#  de ”X” son uno m´as que la cantidad de ”O”. Se nos pide implementar una funci´on en python quien gano el tateti facilito que
#  determine si gan´o alguno, o si Beto hizo trampa (puso una ”O” cuando Ana ya hab´ıa ganado).
#  problema quien
#  gano
#  el
#  tateti
#  facilito (in tablero:seq⟨seq⟨Char⟩⟩) : Z {
#  requiere: {tablero es una matriz cuadrada.}
#  requiere: {5 ≤ |tablero[0]| ≤ 10.}
#  requiere: {tablero s´olo tiene ”X”, ”O” y ”” (espacio vac´ıo) como elementos.}
#  requiere: {En tablero la cantidad de ”X” es igual a la cantidad de ”O” o bien la cantidad de ”X” es uno m´as que la
#  cantidad de ”O”.}
#  asegura: {res = 1 ⇔ hay tres ”X” consecutivas en forma vertical(misma columna) y no hay tres ”O” consecutivas en
#  forma vertical(misma columna).}
#  asegura: {res = 2 ⇔ hay tres ”O” consecutivas en forma vertical (misma columna) y no hay tres ”X” consecutivas en
#  forma vertical(misma columna).}
#  asegura: {res = 0 ⇔ no hay tres ”O” ni hay tres ”X” consecutivas en forma vertical.}
#  asegura: {res = 3 ⇔ hay tres ”X” y hay tres ”O” consecutivas en forma vertical (evidenciando que beto hizo trampa).}
#  }