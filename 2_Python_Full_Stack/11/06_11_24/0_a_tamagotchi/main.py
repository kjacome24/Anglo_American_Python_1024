# main.py

from persona import Persona
from tamagotchi import Tamagotchi,TamagotchiActivo

# Crear instancia de Tamagotchi
mi_tamagotchi = Tamagotchi(nombre="Tama", color="Azul")

# Crear instancia de Persona con su Tamagotchi
persona = Persona(nombre="Kevin", apellido="Jacome", tamagotchi=mi_tamagotchi)

# Interacciones
persona.darle_comida()       # Kevin le da de comer a Tama.
persona.jugar_con_tamagotchi()  # Kevin juega con Tama.
persona.curarlo()             # Kevin cura a Tama.



################Bonus
mi_tamagotchi_activo = TamagotchiActivo(nombre="Tama Jr.", color="Rojo")
persona = Persona(nombre="Kevin", apellido="Jacome", tamagotchi=mi_tamagotchi_activo)
persona.jugar_con_tamagotchi()  # Tama Jr. juega activamente, energía baja más rápido