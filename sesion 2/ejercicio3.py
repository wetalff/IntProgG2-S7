#Vocales
def vocales():
    contador_A = 0
    contador_E = 0
    contador_I = 0
    contador_O = 0
    contador_U = 0
    cadena = input("Di cualquier cosa: ").lower()
    for i in cadena:
        if i == "a":
         contador_A += 1
        elif i == "e":
             contador_E += 1
        elif i == "i":
              contador_I += 1
        elif i == "o":
             contador_O += 1
        elif i == "u":
             contador_U += 1
    print(f"Hay {contador_A} letras a en la cadena") 
    print(f"Hay {contador_E} letras e en la cadena") 
    print(f"Hay {contador_I} letras i en la cadena") 
    print(f"Hay {contador_O} letras o en la cadena") 
    print(f"Hay {contador_U} letras u en la cadena") 


vocales()