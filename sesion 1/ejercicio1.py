#Suma N

def suman():
    acumulacion = 0
    N = int(input("Ingrese un numero entero positivo: "))
    for i in range(N+1):
        acumulacion += i
        print(f"La suma de 1 hasta N progresivamente es: {acumulacion}")


suman()
     