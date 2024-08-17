diccionario_2={
    123456:{
        "nombre":"Juan",
        "apellido":"Gonzales",
        "telefono": 32156
    },
    654321:{
        "nombre":"Carlos",
        "apellido":"Muñoz",
        "telefono": 12345
    },
    111333:{
        "nombre":"Angela",
        "apellido":"Ojeda",
        "telefono": 87965
    }
}

#print(diccionario_2[654321]["nombre"]) #imprimir solo nombre de la cedula

for key, valor in diccionario_2.items():
    print(f"El numero de documento es {key} : Nombre: {valor ["nombre"]} Apellido: {valor ["apellido"]} Telefono: {valor ["telefono"]}")

