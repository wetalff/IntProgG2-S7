def contar_digitos():
    contador = [0] * 10  

    numero = input("Ingresa un número: ")

    for digito in numero:
        if digito.isdigit(): 
            contador[int(digito)] += 1

    print("Frecuencia de cada dígito:")
    for i in range(10):
        print(f"{i} = {contador[i]}")

contar_digitos()
