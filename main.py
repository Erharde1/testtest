#boucle while

import random

def jeux_devinette():
    nombre=random.randit(start,end)
    essai= none
    while essai != nombre:
        essai=int(input(f"J'ai choisi un nombre au hasard entre 0 et 1000. À vous de le deviner... \nEntrez votre essai: "))
        if essai < nombre:
            print("Mauvais choix, le nombre est plus grand.")
        elif essai > nombre:
            print("Maucais choix, le nombre est plus petit.")
    print("Bravo! Vous avez deviné le chiffre.")

jeux_devinette(0,1000)