

# ============================================
# EJERCICIO 13 — Programa vaciarSecuencia
# ============================================
# Especificación:
# problema vaciarSecuencia (inout s: seq⟨Z⟩) {
#     asegura: {|s| = |s@pre| ∧ s[j] = 0 para todo j tal que 0 ≤ j < |s|}
# }

def vaciarSecuencia(s: list[int]):
    # L1,L2,L3
    for i in range(len(s)):
        # L4
        s[i] = 0


# Preguntas:
# 1. Escribir el grafo de control de flujo.
# 2. Escribir un test suite que cubra todas las líneas.
# 3. Extenderlo para cubrir todos los branches.

