diccionario = {}
entrada= input("Ingrese las palabras y su traducción como este ejemplo 'palabra:traduccion' (o escriba 'terminar' para finalizar):")
print(type(entrada))
print(entrada)
par=entrada.split(",")
if entrada.lower() == 'terminar':
     print("Formato incorrecto. Por favor, use 'palabra:traduccion'.")
for i in entrada.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i])
        print(end='')
    else:
        print(i, end=' ')


