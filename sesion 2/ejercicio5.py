#Factorial

def facts():
    acum = 1
    i = 1
    num = int(input("Dime un numero entero positivo: "))
    while i <= num:
        acum *= i
        i += 1
    print(f"El factorial de {num} es {acum}")
    
    
facts()   
        


