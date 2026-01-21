peliculas = {"GDT": "Guerra de Titanes", "HP":"Harry Potter", "PP": "Peter Pan", "F": "Frankeinstein"}

eleccion = input("""\t\t Bienvenido a nuestro sistema de peliculas, dime cual quieres ver. 
                     (GDT: Guerra de Titanes, 
                     HP:Harry Potter, 
                     PP: Peter Pan, 
                     F: Frankeinstein
                     ESCRIBE UNICAMENTE EL ACRONIMO
                     ------------------------------------
                     """
                     )

print, peliculas[eleccion]

try:
    print (f"Reporduciendo {peliculas[eleccion]}...")
except:
    print ("Esa pelicula no existe uwu kawaii 🤣🤣🤣")
    


