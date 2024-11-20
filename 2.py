
class Persona:
    def __init__(self, n, e):
        self.nombre = n
        self.edad = e

    def cumpleaños(self):
        self.edad += 1

# Crear objeto de tipo Persona
p = Persona(input("Ingrese nombre: "), int(input("Ingrese edad: ")))
p.cumpleaños()  # Primer cumpleaños
p.cumpleaños()  # Segundo cumpleaños

# Imprimir el resultado
print(f"{p.nombre} cumple {p.edad} años")
