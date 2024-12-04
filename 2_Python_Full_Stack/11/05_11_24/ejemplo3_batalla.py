################ Batalla de superhéroes ################

import random  # Importa la biblioteca random para generar números aleatorios

class SuperHeroe:
    def __init__(self, nombre, poder, nivel_fuerza=50):
        # Inicializa los atributos del superhéroe
        self.nombre = nombre  # Nombre del superhéroe
        self.poder = poder  # Poder principal del superhéroe
        self.nivel_fuerza = nivel_fuerza  # Nivel de fuerza inicial del superhéroe (valor por defecto es 50)
        self.salud = 100  # Salud inicial del superhéroe, establecida en 100
        print(f"{self.nombre} ha ingresado al equipo con el poder de {self.poder} y fuerza de nivel {self.nivel_fuerza}.")  # Mensaje que se muestra al crear un nuevo superhéroe

    def mostrar_estado(self):
        # Muestra el estado actual del superhéroe (salud, fuerza, poder)
        print(f"{self.nombre} - Salud: {self.salud}, Nivel de fuerza: {self.nivel_fuerza}, Poder: {self.poder}")

    def pelear(self, otro_heroe):
        # Método para atacar a otro superhéroe
        dano = random.randint(20, 50)  # Daño aleatorio entre 20 y 50 para añadir emoción
        otro_heroe.salud -= dano  # Resta el daño a la salud del otro superhéroe
        print(f"{self.nombre} ataca a {otro_heroe.nombre} y le causa {dano} de daño.")  # Muestra el ataque y el daño causado
        if otro_heroe.salud <= 0:
            # Si la salud del otro superhéroe llega a 0 o menos, ha sido derrotado
            otro_heroe.salud = 0  # Asegura que la salud no sea negativa
            print(f"{otro_heroe.nombre} ha sido derrotado.")
        else:
            # Si el otro superhéroe aún tiene salud, muestra su salud actual
            print(f"La salud de {otro_heroe.nombre} ahora es {otro_heroe.salud}.")

# Creando dos instancias de superhéroes
capitan_america = SuperHeroe("capitan_america", "Super Fuerza", 70)  # Superhéroe con poder "Super Fuerza" y fuerza de nivel 70
ironman = SuperHeroe("Ironman", "Tecnología avanzada", 80)  # Superhéroe con poder "Tecnología avanzada" y fuerza de nivel 80

# Bucle de batalla donde ambos superhéroes se atacan hasta que uno sea derrotado
while True:
    # capitan_america ataca a Ironman
    capitan_america.pelear(ironman)
    if ironman.salud == 0:  # Si Ironman es derrotado, termina el bucle
        break
    # Ironman ataca a capitan_america
    ironman.pelear(capitan_america)
    if capitan_america.salud == 0:  # Si capitan_america es derrotado, termina el bucle
        break






