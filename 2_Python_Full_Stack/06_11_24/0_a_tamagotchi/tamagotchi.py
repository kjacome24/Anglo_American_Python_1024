# tamagotchi.py

class Tamagotchi:
    def __init__(self, nombre, color, salud=50, felicidad=50, energia=50):
        self.nombre = nombre
        self.color = color
        self.salud = salud
        self.felicidad = felicidad
        self.energia = energia

    def jugar(self):
        """Incrementa la felicidad del Tamagotchi, pero disminuye un poco su salud"""
        self.felicidad += 10
        self.salud -= 5
        print(f"{self.nombre} está jugando. Felicidad: {self.felicidad}, Salud: {self.salud}")

    def comer(self):
        """Aumenta la salud y felicidad del Tamagotchi al comer"""
        self.felicidad += 5
        self.salud += 10
        print(f"{self.nombre} está comiendo. Felicidad: {self.felicidad}, Salud: {self.salud}")

    def curar(self):
        """Incrementa la salud del Tamagotchi y reduce un poco su felicidad al ser curado"""
        self.salud += 20
        self.felicidad -= 5
        print(f"{self.nombre} ha sido curado. Salud: {self.salud}, Felicidad: {self.felicidad}")




##############Bonus
class TamagotchiActivo(Tamagotchi):
    def jugar(self):
        """Esta subclase incrementa más la felicidad, pero consume más energía"""
        super().jugar()
        self.energia -= 10
        print(f"{self.nombre} está jugando de forma activa. Energía: {self.energia}, Felicidad: {self.felicidad}")