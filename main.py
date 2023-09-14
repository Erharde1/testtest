
import random
def jeu_devinette():
    print("J'ai choisi un nombre au hasard entre 0 et 1000. À vous de le deviner...")
    nombre=random.randint(0,1000)
    essai = -1
    while essai != nombre:
        essai = int(input("Entrez votre essai: "))
        if essai < nombre:
            print("Mauvais choix, le nombre est plus grand.")
        elif essai > nombre:
            print("Maucais choix, le nombre est plus petit.")
    print("Bravo!")

jeu_devinette()
