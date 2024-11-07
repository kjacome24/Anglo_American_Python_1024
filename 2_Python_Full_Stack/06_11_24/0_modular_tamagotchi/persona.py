from tamagotchi import Tamagotchi
from tamagotchi2.tamagotchi2 import Tamagotchi2
from tamagotchi2.tamagotchi3.tamagotchi3 import Tamagotchi3

class Persona:
    def __init__(self,nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = Tamagotchi("Ruby", "Pink")
        self.tamagotchi2 = Tamagotchi2("Bunny","Silver")
        self.tamagotchi3 = Tamagotchi3("Bon", "Red")

x = Persona("Kevin","Jacome")

print(x.tamagotchi.nombre)
print(x.tamagotchi2.nombre)
print(x.tamagotchi3.color)