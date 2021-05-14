### EXAMPLE PYTHON MODULE
# Define some variables:
numberone = 1
ageofqueen = 78

# define some functions
def printhello():
    print("hello")
    
def timesfour(input):
    print(input * 4)
    
# define a class
class Piano:
    def __init__(self):
        self.type = input("What type of piano? ")
        self.height = input("What height (in feet)? ")
        self.price = input("How much did it cost? ")
        self.age = input("How old is it (in years)? ")
	
    def printdetails(self):
        print("This piano is a/an " + self.height + " foot",)
        print(self.type, "piano, " + self.age, "years old and costing\" + self.price + \" dollars.")

'''

El británico vive en la casa roja.
El sueco tiene un perro como mascota.
El danés toma té.
El noruego vive en la primera casa.
El alemán fuma Prince.
La casa verde está inmediatamente a la izquierda de la blanca.
El dueño de la casa verde bebe café.
El propietario que fuma Pall Mall cría pájaros.
El dueño de la casa amarilla fuma Dunhill.
El hombre que vive en la casa del centro bebe leche.
El vecino que fuma Blends vive al lado del que tiene un gato.
El hombre que tiene un caballo vive al lado del que fuma Dunhill.
El propietario que fuma Bluemaster toma cerveza.
El vecino que fuma Blends vive al lado del que toma agua.
El noruego vive al lado de la casa azul.

'''