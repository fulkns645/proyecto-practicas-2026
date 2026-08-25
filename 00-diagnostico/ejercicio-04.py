class Persona:
    def __init__(self,nombre:str,edad:int):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años")

persona1 = Persona("Juan",25)
persona2 = Persona("Pedro",48)

persona1.saludar()
persona2.saludar()