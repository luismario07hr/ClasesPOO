import random

opciones = ('ROCK', 'PAPER', 'SCISSORS', 'LIZARD', 'SPOCK')

opcion = input("Digite una opciones (Rock, Paper, Scissors, Lizard, Spock): ").upper()

opcion_computadora = random.choice(opciones)
print(opcion_computadora)

if opcion == "ROCK":
    if opcion_computadora == 'SCISSORS' or opcion_computadora == "LIZARD":
        print ("Felicidades, ganaste")
    elif opcion_computadora == opcion:
        print ("EMPATEEEEE")
    else: 
        print("Lol, perdiste")

elif opcion == "PAPER":
    if opcion_computadora == 'ROCK' or opcion_computadora == "SPOCK":
        print ("Felicidades, ganaste")
    elif opcion_computadora == opcion:
        print ("EMPATEEEEE")
    else: 
        print("Lol, perdiste")

elif opcion == "SCISSORS":
    if opcion_computadora == 'PAPER' or opcion_computadora == "LIZARD":
        print ("Felicidades, ganaste")
    elif opcion_computadora == opcion:
        print ("EMPATEEEEE")
    else: 
        print("Lol, perdiste")

elif opcion == "LIZARD":
    if opcion_computadora == 'SPOCK' or opcion_computadora == "PAPER":
        print ("Felicidades, ganaste")
    elif opcion_computadora == opcion:
        print ("EMPATEEEEE")
    else: 
        print("Lol, perdiste")

elif opcion == "SPOCK":
    if opcion_computadora == 'SCISSORS' or opcion_computadora == "ROCK":
        print ("Felicidades, ganaste")
    elif opcion_computadora == opcion:
        print ("EMPATEEEEE")
    else: 
        print("Lol, perdiste")

else:
    print ("Opcion no valida")
