# Ejercicio 26 - Guía Práctica 8
# Implementar:
#
# problema listar_textos_de_archivo(in nombre_archivo: str) : list[str]
# requiere: archivo existente y accesible
# asegura: devuelve una lista con los textos legibles (letras, números, espacios, '_') de longitud ≥ 5
#
# Nota: abrir en modo binario 'rb' y filtrar caracteres legibles con chr(byte).
def pertenece(l: list[str], e:str)->bool:
    res:int=0
    for i in l:
        if(i == e):
            res=1
    return res==1

def hacer_legible(e:str)->str:
    may:list[str]=["M","N","B","V","C","X","Z","Ñ","L","K","J","H","G","F","D","S","A","P","O","I","U","Y","T","R","E","W","Q"]
    min:list[str]=["m","n","b","v","c","x","z","ñ","l","k","j","h","g","f","d","s","a","p","o","i","u","y","t","r","e","w","q"]
    num:list[str]=["0","1","2","3","4","5","6","7","8","9"]
    res:str=""
    for i in e:
        if(pertenece(may, i) or pertenece(min, i) or pertenece(num, i) or i == "_"):
            res += i
    return res        
    
def listar_textos_de_archivo(nom_archivo:str)->list[str]:
    archivo=open(nom_archivo, "r")
    res:list[str]=[]
    for i in archivo:
        if (len(i)>= 5):
            res.append(hacer_legible(i))
    return res

print(listar_textos_de_archivo("Ejercicios\Python\Guia_8\ejer_22.txt"))