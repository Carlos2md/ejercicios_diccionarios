mi_diccionario={}
diccionario_2={
    "nombre":"Juan",
    "apellido":"Gonzalez",
    "telefono":456332,
    "edad":25}

#print(diccionario_2["apellido"])
#print(diccionario_2["telefono"])

#diccionario_2["nombre"]="Pedro"
#print(diccionario_2.get("nombre"))

#diccionario_2={
    #"ciudad":"Pasto"
#}
#for key, valor in diccionario_2.items():
    #print(f"la llave es {key} y el valor es {valor}")

if "ciudad" in diccionario_2:
    print("La clave ciudad esta presente")
else:
    print("la clave ciudad no esta presente")