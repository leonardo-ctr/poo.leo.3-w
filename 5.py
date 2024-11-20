class Fabrica():
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio

class Moto(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))

class Carro(Fabrica):
    def cantidad(self):
        print("La cantidad de llantas: {}\nEl color es: {}\nEl precio es: {}".format(self._llantas, self._color, self._precio))
        print("OBJETO=carro")

# Instancia de la clase Moto
moto = Moto(2, "Gris", "$200")
print("OBJETO=moto")
moto.cantidad()

# Instancia de la clase Carro
carro = Carro(4, "Negro", "$600")
carro.cantidad()
