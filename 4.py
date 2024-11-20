class Persona():
    def __init__(self, nom, ape):
        self.nombre = nom
        self.apellido = ape

    def nombre_completo(self):
        print(self.nombre + " " + self.apellido)  # Usar comillas dobles estándar

class Estudiante(Persona):
    def __init__(self, nom, ape, carr):
        super().__init__(nom, ape)
        self.carrera = carr

    def mostrar_carrera(self):
        print(self.carrera)

# Crear instancia de Estudiante
estudiante1 = Estudiante("Juan", "Pérez", "Ingeniería")
estudiante1.nombre_completo()  # Mostrar nombre completo
estudiante1.mostrar_carrera()  # Mostrar carrera
