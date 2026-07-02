texto = "hola mundo hola profe "
palabras = texto.split()
frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print("Frecuencia:", frecuencia)
