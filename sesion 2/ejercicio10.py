#Cajero
def cajero_automatico():
    saldo = 1000  
    contador_depositos = 0  
    contador_retiros = 0  

    while True:
        
        print("\nOpciones disponibles:")
        print("1. Depósito")
        print("2. Retiro")
        print("3. Ver saldo")
        print("4. Salir")
        
        
        opcion = input("Elige una opción (1/2/3/4): ")
        
        if opcion == "1":  
            deposito = float(input("¿Cuánto deseas depositar? "))
            if deposito > 0:
                saldo += deposito  
                contador_depositos += 1  
                print(f"Depósito de {deposito} realizado. Saldo actual: {saldo}")
            else:
                print("El monto de depósito debe ser positivo.")
        
        elif opcion == "2":  
            retiro = float(input("¿Cuánto deseas retirar? "))
            if retiro > 0 and retiro <= saldo:
                saldo -= retiro  
                contador_retiros += 1  
                print(f"Retiro de {retiro} realizado. Saldo actual: {saldo}")
            elif retiro > saldo:
                print("No tienes suficiente saldo para realizar este retiro.")
            else:
                print("El monto de retiro debe ser positivo.")
        
        elif opcion == "3": 
            print(f"Saldo actual: {saldo}")
        
        elif opcion == "4":  
            print(f"\nGracias por usar el cajero automático.")
            print(f"Total de depósitos realizados: {contador_depositos}")
            print(f"Total de retiros realizados: {contador_retiros}")
            break
        
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
    

cajero_automatico()