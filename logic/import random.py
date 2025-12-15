import random

print("🎮 Bienvenido al juego Piedra, Papel o Tijera")

while True:
    jugador = input("\nElige: piedra, papel, tijera o salir: ").lower()

    if jugador not in ["piedra", "papel", "tijera", "salir"]:
        print("⚠️ Opción inválida. Intenta de nuevo.")
        continue

    if jugador == "salir":
        print("👋 Gracias por jugar. Hasta luego!")
        break

    computadora = random.choice(["piedra", "papel", "tijera"])
    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("Resultado: Empate")
    elif (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijera" and computadora == "papel")
    ):
        print("Resultado: ¡Ganaste!")
    else:
        print("Resultado: La computadora gana")
