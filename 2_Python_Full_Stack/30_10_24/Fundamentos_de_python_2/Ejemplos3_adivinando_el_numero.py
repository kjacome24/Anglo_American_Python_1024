import random

def adivina_el_numero():
    print("Adivina el número del 1 al 10")
    numero = random.randint(1, 10)
    intentos = 0

    while True:
        intento = int(input("Ingresa un número: "))
        intentos += 1

        if intento == numero:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos")
            break
        elif intento < numero:
            print("El número es mayor")
        else:
            print("El número es menor")

adivina_el_numero()