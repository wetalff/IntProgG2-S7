# Mayor y Menor

def Mayor_Menor():
    Num = int(input("Dime la cantidad de numeros que quieres ingresar: "))
    
    Nums = int(input("Dime el numero: "))
    
    Mayor = Nums
    
    Menor = Nums
    
    for _ in range(Num - 1):
        Nums = int(input("Dime el numero: "))
        if Nums > Mayor:
         Mayor = Nums
        elif Nums < Menor:
            Menor = Nums
    print("De los numeros que me dijiste el mayor es: ", Mayor)
    print("De los numeros que me dijiste el menor es: ", Menor)
        
        
        
        
        
Mayor_Menor()
     
        