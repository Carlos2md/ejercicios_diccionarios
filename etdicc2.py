def calcular_precio(cantidad, precioxkg):
    precio=cantidad*precioxkg
    return precio

print("Bienvenido a nuestra Fruteria Dani's")
fruta=str(input("Por Favor ingrese la fruta que desea comprar: "))
cantidad_kg=int(input("Por Favor ingrese la cantidad de fruta a comprar: "))

diccionario={
        "Platano":1.35,
        "Manzana":0.80,
        "Pera":0.85,
        "Naranja":0.70,
        
}

precio=diccionario.get(fruta)


print(calcular_precio(cantidad_kg,precio))

#print(diccionario.get("Nombre"),"tiene",diccionario.get("Edad"),"años, vive en la",diccionario.get("Direccion"),"y su numero de telefono es",diccionario.get("Telefono"))

