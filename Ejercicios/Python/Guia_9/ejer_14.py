

# ============================================
# EJERCICIO 14 — Programa existeElemento
# ============================================
# Especificación:
# problema existeElemento (s: seq⟨Z⟩, e: Z) : Bool {
#     asegura: {result = True ↔ s[j] = e para algún j tal que 0 ≤ j < |s|}
# }

def existeElemento(s: list[int], e: int) -> bool:
    # L1
    result: bool = False
    # L2,L3,L4
    for i in range(len(s)):
        # L5
        if s[i] == e:
            # L6
            result = True
            # L7
            break
    # L8
    return result


# Preguntas:
# 1. Escribir el grafo de control de flujo.
# # 2. Escribir un test suite que cubra todas las líneas.

# def test_elemento_presente():
#     s = [1, 2, 3, 4, 5]
#     e = 3
#     assert existeElemento(s, e) == True


# 3. Extenderlo para cubrir todos los branches.

# def test_elemento_ausente():
#     s = [1, 2, 3, 4, 5]
#     e = 6
#     assert existeElemento(s, e) == False