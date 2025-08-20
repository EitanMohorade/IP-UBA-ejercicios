--funcion basica con un parametro--
doubleMe x = x + x
--funcion basica con dos parametros--
--doubleUs x y = x*2 + y*2--
--redefinir doubleUs usando doubleMe--
doubleUs x y = doubleMe x + doubleMe y
--introduccion del if--
doubleSmallNumber x = if x > 100
                        then x
                        else x*2

--el caracter ' no es relevante en Haskell--
conanO'Brien = "¡Soy yo, Conan O'Brien!"
