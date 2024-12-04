import random

def rock_paper_scissors():
    print("¡Piedra, Papel o Tijeras!")
    choices = ["piedra", "papel", "tijeras"]
    
    while True:
        user_choice = input("Escribe piedra, papel o tijeras (o 'salir' para terminar): ").lower()
        if user_choice == 'salir':
            print("¡Gracias por jugar!")
            break
        if user_choice not in choices:
            print("Opción no válida. Inténtalo de nuevo.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computadora elige: {computer_choice}")

        if user_choice == computer_choice:
            print("¡Es un empate!")
        elif (user_choice == "piedra" and computer_choice == "tijeras") or \
             (user_choice == "tijeras" and computer_choice == "papel") or \
             (user_choice == "papel" and computer_choice == "piedra"):
            print("¡Ganaste!")
            break
        else:
            print("Perdiste. ¡Inténtalo de nuevo!")

# Llamada a la función para iniciar el juego
rock_paper_scissors()
