texto = "programacion con el mero mero"

frecuencia = {}
for caracter in texto:
    if caracter in frecuencia:
        frecuencia[caracter] += 1
    else:
        frecuencia[caracter] = 1

print("Frecuencia de caracteres:", frecuencia)
