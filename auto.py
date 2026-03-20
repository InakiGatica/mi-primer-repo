class Auto:
	def __init__(self, marca, color, velocidad):
	    self.marca = marca
	    self.color = color
	    self.velocidad = velocidad

	def acelerar(self):
	    print(self.marca + " esta acelerando!")

	def frenar(self):
	    print(self.marca + " esta frenando!")


class Camion(Auto):
        def __init__(self, marca, color, velocidad, carga):
	    super().__init__(marca, color, velocidad)
            self.carga = carga

        def cargar(self):
            print(self.marca + " puede cargar " + str(self.carga) + " toneladas")

auto1 = Auto("Toyota", "rojo", 180)
auto2 = Auto("Ford", "azul", 200)
camion1 = Camion(" Mercedes", "blanco", 120, 10)


print(auto1.marca)
print(auto2.color)

auto1.acelerar()
auto2.frenar()

camion1.acelerar()
camion1.cargar()
