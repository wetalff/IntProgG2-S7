"""Leer una palabra diferente a fin y convertirla a mayuscula"""

palabra = input("Dime una palabra: ")
for _ in range(1000000):
    print(f"{palabra.capitalize()} tiene {len(palabra)} letras")
    palabra = input("Dime una palabra: ")
    if palabra == "fin":
      print("Adios")
    break
