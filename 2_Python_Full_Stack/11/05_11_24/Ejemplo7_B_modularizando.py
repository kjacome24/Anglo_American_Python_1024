from Ejemplo7_A_modularizando import Arma  # Importa la clase Arma desde el archivo Ejemplo7_A_modularizando.py

class SuperHeroe:
    # Atributo de clase que define la sede principal de todos los superhéroes
    sede_principal = "Torre de avengers"
    
    ########## Método constructor
    def __init__(self, nombre, poder, nivel_fuerza=50):
        # Inicializa los atributos del superhéroe
        self.nombre = nombre  # Nombre del superhéroe
        self.poder = poder  # Poder principal del superhéroe
        self.nivel_fuerza = nivel_fuerza  # Nivel de fuerza inicial del superhéroe
        self.salud = 100  # Salud inicial del superhéroe
        
        # Asociación inicial con un objeto de la clase Arma
        self.arma = Arma("puños", 30)  # El superhéroe comienza con el arma "puños" que causa 30 de daño

    ######### Métodos
    def mostrar_features(self):
        # Muestra los atributos actuales del superhéroe, incluyendo el nombre del arma
        print(f'{self.nombre}, Salud: {self.salud}, poder: {self.poder}, Fuerza: {self.nivel_fuerza}, Arma: {self.arma.nombre}')
        return self  # Permite el encadenamiento de métodos

    def entrenar(self):
        # Entrena al superhéroe y aumenta su nivel de fuerza aleatoriamente
        incremento = random.randint(5, 15)  # Incremento aleatorio entre 5 y 15
        self.nivel_fuerza += incremento  # Aumenta el nivel de fuerza del superhéroe
        return self  # Permite el encadenamiento de métodos

    def pelear(self, enemigo):
        # Método para que el superhéroe ataque a un enemigo
        dano = random.randint(20, 50)  # Daño aleatorio para añadir emoción a la pelea
        enemigo.salud -= dano  # Resta el daño a la salud del enemigo
        print(f"{self.nombre} ataca a {enemigo.nombre} y le causa un daño de {dano}")
        if enemigo.salud <= 0:
            # Si la salud del enemigo llega a 0 o menos, ha sido derrotado
            enemigo.salud = 0  # Asegura que la salud no sea negativa
            print(f'{enemigo.nombre} ha sido derrotado')
        else:
            # Si el enemigo aún tiene salud, muestra su salud actual
            print(f'La salud de {enemigo.nombre} ahora es {enemigo.salud}')

    @classmethod
    def actualizar_sede_principal(cls, nueva_sede):
        # Método de clase para actualizar la sede principal de los superhéroes
        cls.sede_principal = nueva_sede  # Cambia el valor del atributo de clase `sede_principal`
        print(f'La nueva sede es {cls.sede_principal}')

    @staticmethod
    def calcular_dano(fuerza, multiplicador):
        # Método estático que calcula el daño basado en fuerza y un multiplicador
        return fuerza * multiplicador  # Retorna el daño calculado sin modificar atributos de instancia o clase


# Creación de una instancia de SuperHeroe
spiderman = SuperHeroe("Spiderman", "Telaraña", 70)

# Muestra el estado inicial de Spiderman
spiderman.mostrar_features()

# Cambia el arma de Spiderman a "Telaraña Impulsores"
spiderman.arma.nombre = "Telaraña Impulsores"
# Muestra el estado de Spiderman después de cambiar su arma
spiderman.mostrar_features()



########################### Herencia ###########################

class Villano(SuperHeroe):
    ############## Constructor
    def __init__(self, frase_malefica, nombre, poder, nivel_fuerza=50):
        # Llama al constructor de la clase padre (SuperHeroe)
        super().__init__(nombre, poder, nivel_fuerza)  # Inicializa los atributos heredados
        ##### Atributos adicionales
        self.arma = Arma("Garras", 40)  # Los villanos comienzan con el arma "Garras" con daño de 40
        self.frase_malefica = frase_malefica  # Frase malvada específica del villano

# Creación de una instancia de Villano
joker = Villano("¿Quieres sonreír toda la noche?", "Joker", "Veneno de risa", 60)

# Muestra el estado del villano Joker, heredando la funcionalidad de SuperHeroe
joker.mostrar_features()

