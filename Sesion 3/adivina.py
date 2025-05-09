import datetime
import random
import time as t
import os

fecha = datetime.date.today
print(f'Bienvenido \n {fecha}')

def esperar(espera):
    while(espera >= 0):
        os.system("cls // clear")
        print(f"ESPERA{espera}")
        espera = -1
        t.sleep(1)
    os.system("cls//clear")
    


def adivinar(num_user, num_ran):
    t.sleep(3)
    if num_user == num_ran:
        print('ADIVINASTE¡¡')
    else:
        print('Lo siento, no adivinaste el numero 🤣')

def main():
    num_r= random.randint(1,10)
    res= "s"
    while res.lower() != 'n':
        num= input('Ingresa un numero del 1 al 10: ')
        adivinar(int(num), num_r)
        res=input('Desea seguir jugando? 4[S - N - R]: ')
        if res.lower()== 'r':
              num_r= random.randint(1,10)

main()

