#Frase

def frase():
    Contador = 0
    word = ""
    Frase = input("Ingrese una oracion o frase: ")
    for i in Frase:
        if i != " ":
            word += i
        else:
            if word != "":
                Contador += 1
                word = ""
                
    if word != "":
        Contador += 1
        
    print(f"La frase contiene {Contador} palabras")
    
            
        
        
frase()
