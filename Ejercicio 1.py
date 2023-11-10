
diccionario_divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

divisa = input("Ingresa el nombre de una divisa: ")

if divisa in diccionario_divisas:
    simbolo = diccionario_divisas[divisa]
    print(f"El símbolo de {divisa} es {simbolo}")
else:
    print(f"La divisa {divisa} no está en el diccionario.")


