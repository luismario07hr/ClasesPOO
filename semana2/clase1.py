#uno = ["TV", "AC", "FB"]
#dos = ["Televisión", "Aire acondicionado", "Facebook"]


diccio = {"TV": "Television", "AC": "Aire Acondicionado", "FB": "Facebook"}

acronimonew = input("Par: ")
definicionnew = input("Definicion: ")

diccio[acronimonew] = definicionnew

eliminar = input(f"Ingrese el Acronimo a eliminar (TV), (AC), (FB), ({acronimonew}): ")

try:
    del diccio[eliminar]
except:
    print ("No existe una llave con ese acronimo. No se pudo eliminar")
    
diccio["TV"] = input()

print (diccio)
print(diccio.get("Mandarina"))

