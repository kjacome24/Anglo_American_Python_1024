################################ Atritubos de clase
class SuperHeroe:
    sede_principal = "Torre de avengers"  # Atributo de clase: sede principal de todos los superhéroes

    def __init__(self, nombre, poder, nivel_fuerza=50):
        # Inicializa los atributos de instancia del superhéroe
        self.poder = poder  # Poder del superhéroe
        self.nivel_fuerza = nivel_fuerza  # Nivel de fuerza del superhéroe
        self.salud = 100  # Salud inicial del superhéroe
        self.nombre = nombre  # Nombre del superhéroe

    def mostrar_features(self):
        # Muestra los atributos actuales del superhéroe
        print(f"{self.nombre} - Salud: {self.salud}, Nivel de fuerza: {self.nivel_fuerza}, Poder: {self.poder}")
        return self  # Permite el encadenamiento de métodos

################################ @classmethod
#### Nota: Los métodos de clase no tienen acceso a los atributos de instancia, solo a los atributos de clase (como `sede_principal`).
    @classmethod
    def actualizar_cuartel(cls, nuevo_cuartel):
        # Método de clase para actualizar el cuartel general (sede principal)
        cls.sede_principal = nuevo_cuartel  # Cambia el valor del atributo de clase `sede_principal`
        print(f"El cuartel general ha sido actualizado a {cls.sede_principal}")
        
###### @staticmethod
# Los métodos estáticos son funciones auxiliares y usan el decorador @staticmethod.
# No acceden a los atributos de instancia ni de clase, solo a los argumentos que reciben.
    @staticmethod
    def calcular_dano(fuerza, multiplicador):
        # Método estático que calcula el daño basado en fuerza y un multiplicador
        return fuerza * multiplicador  # Retorna el resultado sin modificar ningún atributo de instancia o clase







# Llamada a los métodos de clase y estáticos sin necesidad de instanciar un objeto
SuperHeroe.actualizar_cuartel("Nave de avengers")  # Cambia la sede principal a "Nave de avengers"
damage = SuperHeroe.calcular_dano(80, 1.5)  # Calcula el daño sin necesidad de una instancia
print(f"Calculated damage: {damage}")

# Llamada a los métodos de clase y estáticos con una instancia
ironman = SuperHeroe("ironman", "Tecnologia avanzada", 70)  # Crea una instancia de Ironman
print(ironman.sede_principal)  # Muestra la sede principal actual
ironman.actualizar_cuartel("Mansion de tony stark")  # Cambia la sede principal a "Mansion de tony stark"
print(ironman.sede_principal)  # Muestra la nueva sede principal

# Uso del método estático para calcular el daño multiplicado por 2, usando el nivel de fuerza actual de Ironman
poder_de_ironman_multiplicado = ironman.calcular_dano(ironman.nivel_fuerza, 2)
ironman.nivel_fuerza = poder_de_ironman_multiplicado  # Actualiza el nivel de fuerza de Ironman con el valor calculado
ironman.mostrar_features()  # Muestra los atributos de Ironman actualizados
