class SuperHeroe:
    def __init__(self, nombre, poder, nivel_fuerza=50):
        # Inicializa los atributos del superhéroe
        self.nombre = nombre  # Nombre del superhéroe
        self.poder = poder  # Poder principal del superhéroe
        self.nivel_fuerza = nivel_fuerza  # Nivel de fuerza inicial del superhéroe (valor por defecto es 50)
        self.salud = 100  # Salud inicial del superhéroe, establecida en 100
        print(f"{self.nombre} ha ingresado al equipo")  # Mensaje que se muestra al crear una nueva instancia del superhéroe

    def mostrar_estado(self):
        # Muestra el estado actual del superhéroe
        print(f"{self.nombre} - Salud: {self.salud}, Nivel de fuerza: {self.nivel_fuerza}, Poder: {self.poder}")


# Creación de dos superhéroes
capitan_america = SuperHeroe("Capitan America", "Super fuerza", 90)  # Crea una instancia de Capitan America con nivel de fuerza 90
ironman = SuperHeroe("Ironman", "Tecnología avanzada", 85)  # Crea una instancia de Ironman con nivel de fuerza 85

# Muestra el estado de cada superhéroe
capitan_america.mostrar_estado()
ironman.mostrar_estado()

