print("Bienvenido a nuestra agenda")
nombre=str(input("Por Favor ingrese su nombre: "))
edad=int(input("Por Favor ingrese su edad: "))
direccion=str(input("Por Favor ingrese su direccion: "))
telefono=int(input("Por Favor ingrese su telefono: "))

diccionario={
        "Nombre":nombre,
        "Edad":edad,
        "Direccion":direccion,
        "Telefono":telefono,
        
}

#for key, valor in diccionario.items():
    #print(f"{key} {valor}")

print(diccionario.get("Nombre"),"tiene",diccionario.get("Edad"),"años, vive en la",diccionario.get("Direccion"),"y su numero de telefono es",diccionario.get("Telefono"))
