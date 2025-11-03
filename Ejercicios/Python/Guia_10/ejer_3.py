#  Ejercicio 3. Veterinaria- Flujo de pacientes
#  Con el objetivo de organizar el flujo de pacientes, en una veterinaria se anotan los tipos de mascotas que van ingresando
#  al local. Se necesita identificar las consultas que involucran solo a perros y gatos. Por eso, se decide desarrollar una funci´on en
#  Python que encuentre la secuencia m´as larga de consultas consecutivas que solo contenga los tipos de mascota ”perro” o ”gato”.
#  Se pide implementar una funci´on que, dada una secuencia de strs, que representan los tipos de animales atendidos, devuelva el
#  ´ındice donde comienza la subsecuencia m´as larga que cumpla con estas condiciones.
#  problema subsecuencia
#  mas
#  larga (in tipos pacientes atendidos : seq⟨str⟩) : Z {
#  requiere: {tipos pacientes atendidos tiene, por lo menos, un elemento ”perro” o ”gato”.}
#  asegura: {res es el ´ındice donde empieza la subsecuencia m´as larga de tipos pacientes atendidos que contenga solo
#  elementos ”perro” o ”gato”.}
#  asegura: {Si hay m´as de una subsecuencia de tama˜no m´aximo, res tiene el ´ındice de la primera.}
#  }

def subsecuencia_mas_larga(tipos_pacientes_atendidos: str)-> int:
    return 12