precios={"Pan": 1.40 , "Huevos" :2.30 , "Cebolla":0.85 , "Aceite":4.35}

articulo = input("Ingrese el nombre del artículo: ")
cantidad = int(input("Ingrese la cantidad de unidades: "))
if articulo in precios:
    precio_total = precios[articulo] * cantidad
    print(f"El precio total por {cantidad} unidades de {articulo} es: {precio_total}")
else:
    print(f"El artículo '{articulo}' no está en la lista de precios.")