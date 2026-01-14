precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad del producto: "))
descuento = float(input("Ingrese el porcentaje de decuento en decimal: "))

total = (precio * cantidad) - (precio * cantidad)*descuento
print (total)