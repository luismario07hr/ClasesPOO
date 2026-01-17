pokemons = [["Gardevoir", 50], ["Togekiss", 40], ["Dragonite", 40], ["Venasaur",60], ["Crobat", 45], ["Gastrodon", 53]]

pokemondisponibles = 0

print ("===================================================")
for pokemon in pokemons: 
    if pokemon[1] < 50: 
        print (f"{pokemon[0]} no puede pelear en este gimnasio :(")

    else: 
        print (f"{pokemon[0]} esta listo para pelear :)")
        pokemondisponibles += 1
    print ("===================================================")
    
if pokemondisponibles >= 3: 
    print ("Estas listo para enfrentar este gimnasio. Buena suerte")
    print ("===================================================")
else: 
    print (f"{pokemondisponibles} de tus pokemon no pueden pelear. Subilos de nivel y regresa luego")