diccionario = {}
print("Ingrese las palabras y su traducción como este ejemplo 'palabra:traduccion' (o escriba 'terminar' para finalizar):")

while True:
    entrada = input()
    
    if entrada == 'terminar':
        break
    pares = entrada.split(",")
    
    for i in pares:
        partes = i.split(":")
        if len(partes) == 2:
            palabra, traduccion = partes
            diccionario[palabra.strip()] = traduccion.strip()
        else:
            print(f"Formato incorrecto para el par: {i}. Use 'palabra:traduccion'.")
            continue
    
frase_español=input("Introduzca una frase en español")
palabras = frase_español.split()
frase_traducida = [diccionario.get(palabra, palabra) for palabra in palabras]
frase_ingles = " ".join(frase_traducida)
print(f"La frase traducida es: {frase_ingles}")


    

