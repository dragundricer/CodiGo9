# el encapsulamiento sirve para proteger atributos y metodos para que no puedan ser alterados o llamados fuera de la misma clase
class Auto:
    def __init__(self, largo=200, ancho=130, enMarcha=False, motor=1500):
        self.largo = largo
        self.ancho = ancho
        self.__ruedas = 4  # asi se define un atributo privado
        self.enMarcha = enMarcha
        self.motor = motor

    def __str__(self):
        return str(self.__ruedas)

    def arracar(self, arrancamos):
        self.enMarcha = arrancamos
        if(self.enMarcha):
            chequeo = self.__chequeo_interno()
        if(self.enMarcha and chequeo):
            print("El coche esta en marcha sin ningun problema")
        elif (self.enMarcha and chequeo == False):
            print("El coche esta en marcha pero se requiere atencion")
        else:
            print("El coche esta parado")

    def estado(self):
        print(
            f"El auto tiene de ancho: {self.ancho}, de largo: {self.largo}, # de ruedas: {self.__ruedas}, motor: {self.motor}")

    # encapsulamos el metodo para que solo pueda ser llamado o invocado dentro de la clase
    def __chequeo_interno(self):
        self.gasolina = 5
        self.aceite = "Ok"
        self.temperatura = 10
        self.puertas = "Cerradas"
        if(self.gasolina > 20 and self.aceite == "Ok" and self.temperatura < 75 and self.puertas == "Cerradas"):
            return True
        else:
            return False

    # TODO METODO ES UNA FUNCION PERO NO TODA FUNCION ES UN METODO
    # metodo: es una funcion que se va a ejecutar UNICAMENTE dentro de una clase
    # funcion: es un conjunto de codigo que se va a ejecutar siempre que se le invoque
# instanciar una clase === ejemplarizar una clase === crear un objeto
miAutito = Auto(largo=150)
miAutito.__ruedas = 3
# miAutito.arracar(True)
# print(miAutito)
# print(miAutito.ruedas)

# EJERCICIO
# Crear una clase llamada Coordenadas y que va a tener como atributos X y Y , en su constructor debe inicializar los valores y sino recibe cualquiera de los dos su valor por defecto es 0. Tener un metodo para ver cuales han sido los valores ingresados, ejemplo
# (10,5)
# tener un metodo para ver en que cuadrante esta
#     2   |    1
#   ______|______
#         |
#     3   |    4
# Esta en el cuadrante 1
# Tener un metodo otro_vector() que tome otras coordenadas y calcule su vector resultante ((x2-x1),(y2-y1))
# PLUS: calcular la distancia entre los dos puntos => ((x2-x1)^2+(y2-y1)^2)^1/2, este debe ser un metodo privado que se ejecute cuando llamamos al metodo otro_vector()


class Coordenadas:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def cuadrante(self): # self => this (c#, java)
        if(self.x >= 0 and self.y >= 0):
            return "Cuadrante 1"
        elif (self.x > 0 and self.y < 0):
            return "Cuadrante 2"
        elif (self.x < 0 and self.y < 0):
            return "Cuadrante 3"
        elif (self.x < 0 and self.y > 0):
            return "Cuadrante 4"

    def otro_vector(self,x2,y2):
        self.x2=x2
        self.y2=y2
        print("Su vector resultante es: ({0}),({1})".format(self.x2-self.x,self.y2-self.y))
        self.__calcular_distancia()
        # pass # en c# o java seria poner {}

    def __calcular_distancia(self):
        print(f"La distancia es: {((self.x2-self.x)**2+(self.y2-self.y)**2)**(1/2)}")

    def __str__(self):
        return f"({self.x,self.y})"


cuadrante = Coordenadas(10,5)
print(cuadrante)
print(cuadrante.cuadrante())
cuadrante.otro_vector(5,2)
# No se puede acceder a este metodo porque es privado y solo se puede acceder dentro de la misma clase
# para definir un metodo o atributo privado se usa doble subguion(guion bajo) al inicio
# cuadrante.__calcular_distancia()