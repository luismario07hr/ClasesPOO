class Libro: #Creamos la primera clase, es un plano sin instrucciones.
    def __init__ (self, titulo, autor, isbn, disponible):
        self.titulo = titulo 
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
    def cambiar_disponibilidad (self): 
        if self.disponible:
            self.disponible = False
        #Un metodo. Es un metodo constructor que va a recibir parametros. Se usa self para
    
catalogo = [Libro("100 Anios de soledad0", "Gabriel Garcia Marquez, 123", "ISBN", True), Libro("200 Anios de soledad0", "Gabriel Garcia Marquez", "2234", False)]
for libro in catalogo:
    print (f"Autor: ")