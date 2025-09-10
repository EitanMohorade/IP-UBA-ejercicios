{-
Implementar la funci´on todosMenores :: (Integer, Integer, Integer)-> Bool

problema todosMenores (t : Z×Z×Z) : Bool {
    requiere: {True}
    asegura: {(res = true) ↔ ((f(t0) > g(t0)) ∧(f(t1) > g(t1)) ∧ (f(t2) > g(t2)))}
}

problema f (n : Z) : Z {
    requiere: {True}
    asegura: {(n ≤ 7 → res = n2)∧(n > 7 →res =2n−1)}
}

problema g (n : Z) : Z {
    requiere: {True}
    asegura: {Si n es un n´umero par entonces res = n/2, en caso contrario, res = 3n+1}
}
-}