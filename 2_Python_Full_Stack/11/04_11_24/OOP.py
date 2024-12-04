########################### OOP #################################################################################################

#### Vamos a partir definiendo el objeto sin parámetros de entrada: 

class Persona:  # Generalmente, una clase empieza con mayúscula
    # Método constructor: Encargado de inicializar los atributos de la clase que serán heredados por los objetos
    def __init__(self):  # Método encargado de inicializar los atributos de la clase
        #### Características (Atributos)
        self.tipo = "Humano"   # Define el tipo de la persona como "Humano"
        self.health = 100      # Asigna un valor inicial de salud de 100
        self.ataque = 10       # Define un valor de ataque de 10
        self.defensa = 5       # Define un valor de defensa de 5
    
    ### Acciones y funcionalidades (Métodos)
    def speak(self):
        print("I can Talk.......")  # Muestra un mensaje indicando que la persona puede hablar


# Crear un objeto de la clase Persona y usar sus métodos y atributos
kevin = Persona()
kevin.speak()            # Llama al método "speak" de la instancia kevin
print(kevin.health)      # Imprime el valor de salud de kevin
print(kevin.tipo)        # Imprime el tipo de kevin










#### Mismo ejemplo agregando otra función para interactuar entre 2 objetos:

class Persona:  # Generalmente, una clase empieza con mayúscula
    # Método constructor: Encargado de inicializar los atributos de la clase que serán heredados por los objetos
    def __init__(self):  # Método encargado de inicializar los atributos de la clase
        #### Características (Atributos)
        self.tipo = "Humano"
        self.health = 100
        self.ataque = 10
        self.defensa = 5
    
    ### Acciones y funcionalidades (Métodos)
    def speak(self):
        print("I can Talk.......")
    
    # Método que permite a una persona atacar a otra persona (enemigo)
    def atacar(self, enemigo):
        enemigo.health -= self.ataque - enemigo.defensa  # Calcula el daño infligido al enemigo basado en la defensa
        print(f'El enemigo ha recibido {self.ataque - enemigo.defensa} de daño')  # Muestra el daño recibido


# Crear dos objetos de la clase Persona
kevin = Persona()
arturo = Persona()

# Kevin ataca a Arturo y se muestra la salud de ambos
kevin.atacar(arturo)
print(f'La salud de Kevin es {kevin.health}')
print(f'La salud de Arturo es {arturo.health}')

# Arturo ataca a Kevin y se muestra la salud de ambos después del ataque
arturo.atacar(kevin)
print(f'La salud de Kevin es {kevin.health}')
print(f'La salud de Arturo es {arturo.health}')















########################## Ejemplo con variables de entrada

class Persona:
    #### Método constructor
    def __init__(self, edad, peso, estatura, nombre):  # Las variables de entrada van después del self
        #### Atributos
        self.tipo = "Humano"
        self.salud = 100
        self.defensa = 5
        self.ataque = 10
        self.edad = edad
        self.peso = peso
        self.estatura = estatura
        self.nombre = nombre
    
    ### Métodos
    def hablar(self):
        print("Hablandooooo...........")  # Mensaje que indica que la persona está hablando
    
    # Método para obtener el peso del objeto usando return
    def getpeso(self):
        return self.peso
    
    # Método para incrementar la edad (cumplir años)
    def cumple(self):
        self.edad += 1
    
    # Método para cambiar el nombre de la persona
    def cambiodenombre(self, nuevonombre):
        self.nombre = nuevonombre

    # Método para atacar a otro objeto de la clase Persona
    def atacar(self, enemigo):
        enemigo.salud -= self.ataque - enemigo.defensa  # Calcula y aplica el daño en base al ataque y defensa
        print(f'El enemigo ha recibido {self.ataque - enemigo.defensa} de daño')


# Crear una instancia de Persona con parámetros específicos
kevin = Persona(34, 87, 1.78, "Kevin")

# Mostrar algunos atributos y llamar métodos de la instancia kevin
print(kevin.tipo)
print(kevin.edad)
print(kevin.salud)

kevin.hablar()
peso_de_kevin = kevin.getpeso()
print(peso_de_kevin)

kevin.cumple()  # Incrementa la edad en 1
print(kevin.edad)

# Crear otro objeto de la clase Persona y mostrar sus datos
katari = Persona(20, 50, 1.60, "Katari")
print(f'Hola, soy {katari.nombre}, tengo {katari.edad} años, y mi salud es {katari.salud}')

# Katari ataca a Kevin y se muestra la salud de ambos después del ataque
katari.atacar(kevin)
print(f'La salud de Kevin es {kevin.salud}')
print(f'La salud de Katari es {katari.salud}')





















##################### Herencia

# Clase Estudiante que hereda de la clase Persona
class Estudiante(Persona):
    ##### Constructor
    def __init__(self, curso, edad, peso, estatura, nombre):
        super().__init__(edad, peso, estatura, nombre)  # Llama al constructor de la clase padre Persona
        #### Atributos adicionales de la clase Estudiante
        self.curso = curso
        self.conocimiento = 50  # Nivel de conocimiento inicial del estudiante
    
    ## Métodos
    # Método que incrementa el conocimiento del estudiante al aprender
    def aprender(self):
        self.conocimiento += 5 


# Crear un objeto de la clase Estudiante
Jose_biadayoli = Estudiante("Full stack Python", 25, 75, 1.80, "Jose")

# Mostrar algunos atributos de Jose_biadayoli
print(Jose_biadayoli.curso)          # Imprime el curso de Jose
print(Jose_biadayoli.salud)           # Imprime la salud de Jose, heredada de Persona
Jose_biadayoli.aprender()             # Incrementa el conocimiento de Jose al aprender
print(Jose_biadayoli.conocimiento)    # Imprime el nivel de conocimiento de Jose después de aprender
