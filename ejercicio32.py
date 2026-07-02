numero = 17

es_primo = True
if numero < 2:
    es_primo = False
else:
    i = 2
    while i * i <= numero:
        if numero % i == 0:
            es_primo = False
            break
        i += 1

if es_primo:
    print(numero, "es un numero primo")
else:
    print(numero, "no es un numero primo")
