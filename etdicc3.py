Curso={
        #"Asignatura1":"Matematicas",
        #"Credito1":"6",
        #"Asignatura2":"Fisica",
        #"Credito2":"4",
        #"Asignatura3":"Quimica",
        #"Credito3":"5",
        "Matematicas":6,
        "Fisica":4,
        "Quimica":5,
        }

sumatoria=0
for llave,valor  in Curso.items():
    
    sumatoria+=valor
    print(f"<Asignatura> {llave}, tiene <Creditos> {valor}")


print(f"Los <Creditos> totales del Curso son: {sumatoria}") 