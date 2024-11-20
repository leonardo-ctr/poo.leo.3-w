class Universidad():
    def __init__(self, Nombre):
        self.Nombre = Nombre

class Carrera():
    def carrera(self, especialidad):
        self.especialidad = especialidad

class Estudiante(Universidad, Carrera):
    def __init__(self, Nombre, nombre, edad):
        Universidad.__init__(self, Nombre)  # Inicializando la clase Universidad
        self.nombre = nombre
        self.edad = edad

    def datos(self):
        print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la Universidad {self.Nombre}")

# Crear una instancia de Estudiante
persona = Estudiante("Harvard", "Mike", 19)
persona.carrera("Ingeniería Mecatrónica")
persona.datos()
