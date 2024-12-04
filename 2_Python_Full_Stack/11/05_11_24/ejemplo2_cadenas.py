##############cadenasss

import random  # Importa la biblioteca random para generar números aleatorios

class SuperHeroe:
    def __init__(self, nombre, poder, nivel_fuerza=50):
        # Inicializa los atributos del superhéroe
        self.nombre = nombre  # Nombre del superhéroe
        self.poder = poder  # Poder principal del superhéroe
        self.nivel_fuerza = nivel_fuerza  # Nivel de fuerza inicial del superhéroe (valor por defecto es 50)
        self.salud = 100  # Salud inicial del superhéroe, establecida en 100

    def mostrar_estado(self):
        # Muestra el estado actual del superhéroe
        print(f"{self.nombre} - Salud: {self.salud}, Nivel de fuerza: {self.nivel_fuerza}, Poder: {self.poder}")
        return self  # Permite el encadenamiento de métodos

    def entrenar(self):
        # Entrena al superhéroe, incrementando su nivel de fuerza
        incremento = random.randint(5, 15)  # Genera un número aleatorio entre 5 y 15
        self.nivel_fuerza += incremento  # Incrementa el nivel de fuerza
        print(f"{self.nombre} ha entrenado y su nivel de fuerza aumentó en {incremento}. Fuerza actual: {self.nivel_fuerza}")
        return self  # Permite el encadenamiento de métodos


# Creación de una instancia del superhéroe Robin
Robin = SuperHeroe("Robin", "Acrobacias", 60)

# Muestra el estado inicial, entrena dos veces y vuelve a mostrar el estado
Robin.mostrar_estado().entrenar().entrenar().mostrar_estado()

