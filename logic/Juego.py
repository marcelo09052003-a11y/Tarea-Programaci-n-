import random

print("🎮 JUEGO: Piedra, Papel o Tijera")

while True:

    # 1️⃣ Mostrar opciones
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

    jugador = input("Ingresa el número de tu elección: ")

    # 2️⃣ Validación básica
    if jugador not in ["1", "2", "3", "4"]:
        print("⚠️ Advertencia: debes elegir 1, 2, 3 o 4.")
        continue

    # 3️⃣ Salir
    if jugador == "4":
        print("\n🎮 Gracias por Jugar")
        break

    # Traducimos la elección del jugador
    opciones = {
        "1": "piedra",
        "2": "papel",
        "3": "tijera"
    }

    eleccion_jugador = opciones[jugador]
    print(f"👉 Tú elegiste: {eleccion_jugador}")

    # 4️⃣ ELECCIÓN ALEATORIA DE LA COMPUTADORA (3 OPCIONES)
    eleccion_computadora = random.choice(["piedra", "papel", "tijera"])
    print(f"💻 La computadora eligió: {eleccion_computadora}")

    # 5️⃣ Comparación de resultados según el diagrama
    if eleccion_jugador == eleccion_computadora:
        print("🔵 Resultado: EMPATE")

    elif (
        (eleccion_jugador == "piedra" and eleccion_computadora == "tijera") or
        (eleccion_jugador == "papel" and eleccion_computadora == "piedra") or
        (eleccion_jugador == "tijera" and eleccion_computadora == "papel")
    ):
        print("🟢 Resultado: ¡GANASTE!")

    else:
        print("🔴 Resultado: LA COMPUTADORA GANA")
