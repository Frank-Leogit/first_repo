import random
value = int(input("Scegliere il range di numeri da generare: "))
guess = random.randint(0,value)
print(guess)
i = False
while (i == False):
    shot = int(input("Vediamo se indovini: "))
    if(shot == guess):
        print("Congratulazioni hai indovinato!")
        i = True
    else:
        print("Ritenta!")
