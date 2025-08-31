## Ajuste de patrones
Es la forma en que definis lo que le sucederá al dato dependiendo de ciertos casos, al estilo swith/case en otros lenguajes.

```bash
    lucky :: (Integral a) => a -> String
    lucky 7 = "¡El siete de la suerte!"
    lucky x = "Lo siento, ¡no es tu día de suerte!"
```

acá definis que tipo de restriccion hay detras del '=>' y luego que valores debe tomar y que devolverá, despues le asignas los casos segun corresponda.

## Guardas
Estas son formas como el if/else if/else pero escritas mas prolijas

```bash
    bmiTell :: (RealFloat a) => a -> a -> String
    bmiTell weight height
        | weight / height ^ 2 <= 18.5 = "Tienes infrapeso ¿Eres emo?"
        | weight / height ^ 2 <= 25.0 = "Supuestamente eres normal... Espero que seas feo."
        | weight / height ^ 2 <= 30.0 = "¡Estás gordo! Pierde algo de peso gordito."
        | otherwise                   = "¡Enhorabuena, eres una ballena!"
```

## Let .. In
Let en si sirve para definir variables locales, luego en el In se define lo que se hará con las fucniones, variables o datos puestos en el let, ejemplo:

```bash
    hipotenusa a b =
  let x = a
      y = b
  in sqrt (x^2 + y^2)
```

La diferencia clave con en Where es que este se definen despues las variables

```bash
    hipotenusa a b = sqrt (x^2 + y^2)
        where x = a
            y = b
```