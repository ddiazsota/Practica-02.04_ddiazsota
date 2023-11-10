persona={}

categorias = ["nombre", "edad", "sexo", "telefono", "correo"]

while True:
    for categoria in categorias:
        dato = input(f"Ingrese {categoria} (o 'k' para salir): ")
        if dato == 'q':
            break
        persona[categoria] = dato
        print(f"Información actualizada: {persona}")
    else:
        continue
    break
