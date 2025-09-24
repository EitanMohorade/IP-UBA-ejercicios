{-
 En este ejercicio trabajaremos con la lista de contactos del tel´efono.
 a) Implementar una funci´on que me diga si una persona aparece en mi lista de contactos del tel´efono: enLosContactos ::
 Nombre-> ContactosTel-> Bool
 -}

 {-
 b) Implementar una funci´on que agregue una nueva persona a mis contactos, si esa persona est´a ya en mis contactos entonces
 actualiza el tel´efono. agregarContacto :: Contacto-> ContactosTel-> ContactosTel
-}

 {-
 c) Implementar una funci´on que dado un nombre, elimine un contacto de mis contactos. Si esa persona no est´a no hace
 nada. eliminarContacto :: Nombre-> ContactosTel-> ContactosTel
 Para esto definiremos los siguientes tipos:
 type Texto = [Char]
 type Nombre = Texto
 type Telefono = Texto
 type Contacto = (Nombre, Telefono)
 type ContactosTel = [Contacto]
 Sugerencia: Implementar las funciones auxiliares elNombre y elTelefono para que dado un Contacto devuelva el dato
 del nombre y el tel´efono respectivamente
-}