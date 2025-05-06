#Notas

def notas():
    acumulador = 0
    contador = 0
    cant = int(input("Ingrese la cantidad de calificaciones a calcular su promedio: "))
    for _ in range(cant):
        calificacion = float(input("Dime la nota de esta clase: "))
        acumulador += calificacion
    promedio = acumulador / cant
    print("El promedio de las calificaciones es de:", promedio)
    
    
notas()
         
    