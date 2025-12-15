from utils.random_choice import normalize_choice
from storage.data_store import save_round

VALID_CHOICES = ["piedra", "papel", "tijera", "salir"]

def is_valid_choice(choice):
    return normalize_choice(choice) in VALID_CHOICES

def determine_winner(player_choice_raw, computer_choice_raw):
    player = normalize_choice(player_choice_raw)
    computer = normalize_choice(computer_choice_raw)

    if player == computer:
        result = {"winner": "empate", "message": "Empate"}
        save_round(player, computer, result["winner"])
        return result

    rules = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    }

    if rules[player] == computer:
        result = {"winner": "jugador", "message": "¡Ganaste!"}
    else:
        result = {"winner": "computadora", "message": "La computadora gana"}

    save_round(player, computer, result["winner"])
    return result

# Espacio para agregar reglas nuevas
