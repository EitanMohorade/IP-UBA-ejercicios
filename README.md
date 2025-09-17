# IP-UBA-ejercicios
Ejercicios prácticos de **Introducción a la Programación**  
"Segundo cuatrimestre 2025"  

## Instalación

Para instalar Haskell seguí los pasos desde la página oficial:

🔗 [Haskell GHCup](https://www.haskell.org/ghcup/)

Ahí vas a encontrar el comando que tenés que copiar y pegar en la terminal para configurar el compilador y el intérprete de Haskell (GHC y GHCi).  

## Uso básico

- Los archivos de Haskell tienen extensión **`.hs`**  
    
```bash 
-- Para abrir el intérprete
ghci

-- Para cargar un archivo
:l nombreArchivo.hs

-- Para recargar el archivo después de guardar cambios
:r

-- Para salir de ghci
:q
```

## Ver valores de Tipos
```bash
-- Para ver el tipo de una expresión o función
:t expresion

-- Para ver la definición interna de un nombre (si es posible)
:i nombre
```

## Manejo de modulos
```bash
-- Para importar un módulo
import Data.List

-- Para cargar varios módulos
:l archivo1.hs archivo2.hs
```