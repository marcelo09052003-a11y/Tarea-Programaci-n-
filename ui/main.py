from logic.game_logic import is_valid_choice, determine_winner
from utils.random_choice import get_random_choice, normalize_choice
from storage.data_store import get_history

def game_loop():
    print("🎮 Bienvenido al juego Piedra, Papel o Tijera")

    while True:
        choice = input("\nElige (piedra/papel/tijera) o escribe 'salir': ")
        choice = normalize_choice(choice)

        if not is_valid_choice(choice):
            print("⚠️ Opción inválida. Intenta otra vez.")
            continue

        if choice == "salir":
            print("\n👋 Saliendo del juego…")
            mostrar_historial()
            break

        computer = get_random_choice()
        print(f"💻 La computadora eligió: {computer}")

        resultado = determine_winner(choice, computer)
        print(f"🟢 Resultado: {resultado['message']}")

def mostrar_historial():
    historial = get_history(limit=5)

    if not historial:
        print("No hay partidas registradas.")
        return

    print("\n📋 Últimas partidas:")
    for ronda in historial:
        print(f"- {ronda['timestamp']}: Jugador={ronda['player']} / CPU={ronda['computer']} / Resultado={ronda['winner']}")

if __name__ == "__main__":
    game_loop()

# Espacio para agregar menús adicionales
