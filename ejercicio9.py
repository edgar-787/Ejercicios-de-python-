texto = "Hola Mundo CUYO"
vocales = "aeiouAEIOU"
contador = 0
for letra in texto:
    if letra in vocales:
        contador += 1
print("Número de vocales en", texto, ":", contador)
