class Cuenta:
    nombre = ""
    apellido = ""
    cantidad = 0

    def __init__(self, nombre, apellido, cantidad):
        self.nombre = nombre
        self.apellido = apellido
        self.cantidad = cantidad

    def mostrar(self):
        print(self.nombre, "", self.apellido, " - ", str(self.cantidad))
    def ingresar(self):
        self.cantidad += int(input("Ingrese la cantidad que depositará en la cuenta  "))
        print("La cantidad ingresada es  ")
    def retirar(self):
        self.cantidad -= int(input("Ingrese el monto a retirar de la cuenta  "))
        print ("Monto actualizado  ")
    
cuenta1 = Cuenta("María" , "Perez", 1000)
cuenta1.mostrar()
cuenta1.ingresar()
cuenta1.mostrar()
cuenta1.retirar()
cuenta1.mostrar()