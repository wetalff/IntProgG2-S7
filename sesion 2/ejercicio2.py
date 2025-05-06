#Pares

def par():
    Contador = 0
    acumulador = 1
    N = 2
    M = int(input("Ingrese un numero entero positivo: "))
    
    while Contador < M:
        acumulador *= N
        Contador += 1
        N += 2
    print(f"La multiplicacion de los {M} numeros pares es de {acumulador}")
    
par()