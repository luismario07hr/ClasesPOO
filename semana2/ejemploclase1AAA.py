menus = {"Desauno": ["Huevo", "Cafe", "Pan"],
         "Almuerzo": ["Costilla", "Pollo", "Carne"],
         "Cena": ["Pupusas", "Frijoles", "Sandwich"]}

for tiempo, comidas in menus.items(): 
    print (tiempo)
    print ("---------------------------")
    for comida in comidas: 
        print (comida)

for tiempo, platos in menus.items(): 
    print (tiempo, ": ", ", " .join(platos))
