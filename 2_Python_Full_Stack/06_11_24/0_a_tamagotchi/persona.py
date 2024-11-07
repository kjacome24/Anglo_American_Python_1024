# persona.py

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        """Hace que la persona juegue con su Tamagotchi, incrementando su felicidad y reduciendo su salud"""
        print(f"{self.nombre} juega con {self.tamagotchi.nombre}.")
        self.tamagotchi.jugar()

    def darle_comida(self):
        """Alimenta al Tamagotchi, aumentando su felicidad y salud"""
        print(f"{self.nombre} le da de comer a {self.tamagotchi.nombre}.")
        self.tamagotchi.comer()

    def curarlo(self):
        """Cura al Tamagotchi, incrementando su salud y ajustando su felicidad"""
        print(f"{self.nombre} cura a {self.tamagotchi.nombre}.")
        self.tamagotchi.curar()
