#Suma pares e impares
def suma():
    acum1 = 0
    acum2 = 0
    Num = int(input("Dime un numero: "))
    if Num % 2 == 0:
            acum1 += Num
    elif Num % 2 != 0:
            acum2 += Num
    while Num != 0:
        Num = int(input("Dime un numero: "))
        if Num % 2 == 0:
            acum1 += Num
        elif Num % 2 != 0:
            acum2 += Num
        
        
    print("Suma de los pares: ", acum1)
    print("Suma de los impares: ", acum2)
        
       
        
        
        
               
suma()
