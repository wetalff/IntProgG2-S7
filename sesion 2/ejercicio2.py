#Pares

def par():
 contador = 0
 valor = 2
 producto = 1
 Num = int(input("Ingrese un número entero positivo: "))
 while contador < Num:
      producto *= valor
      contador += 1
      valor += 2 
    
 print("El producto de los primeros", Num, "números pares es:", producto)


par()