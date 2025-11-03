#  Ejercicio 14. Hospital- Alarma epidemiol´ogica
#  Necesitamos detectar la aparici´on de posibles epidemias. Para esto contamos con un lista de enfermedades infecciosas y los
#  registros de atenci´on por guardia dados por una lista expedientes. Cada expediente es una tupla con ID paciente y enfermedad
#  que motiv´o la atenci´on. Debemos devolver un diccionario cuya clave son las enfermedades infecciosas y su valor es la proporci´on
#  de pacientes que se atendieron por esa enfermedad. En este diccionario deben aparecer solo aquellas enfermedades infecciosas
#  cuya proporci´on supere cierto umbral.
#  problema alarma
#  epidemiologica (in registros : seq⟨Z × str⟩,in infecciosas : seq⟨str⟩,in umbral : R) : dict<str, R> {
#  requiere: {0 < umbral < 1.}
#  asegura: {claves de res pertenecen a infecciosas.}
#  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
#  enfermedad sobre el total de registros es mayor o igual al umbral, entonces res[enfermedad] = porcentaje.}
#  asegura: {Para cada enfermedad perteneciente a infecciosas, si el porcentaje de pacientes que se atendieron por esa
#  enfermedad sobre el total de registros es menor que el umbral, entonces enfermedad no aparece en res.}
#  }