import random

def mostrar_titulo():
    print("🎮 JUEGO: Piedra, Papel o Tijera")

def mostrar_menu():
    print("\nElige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("4. Salir")

def obtener_eleccion_jugador():
    jugador = input("Ingresa el número de tu elección: ")
    if jugador not in ["1", "2", "3", "4"]:
        print("⚠️ Advertencia: debes elegir 1, 2, 3 o 4.")
        return None
    return jugador

def traducir_eleccion(jugador):
    opciones = {"1": "piedra", "2": "papel", "3": "tijera"}
    return opciones[jugador]

def obtener_eleccion_computadora():
    return random.choice(["piedra", "papel", "tijera"])

def determinar_resultado(jugador, computadora):
    if jugador == computadora:
        return "empate"
    elif (
        (jugador == "piedra" and computadora == "tijera") or
        (jugador == "papel" and computadora == "piedra") or
        (jugador == "tijera" and computadora == "papel")
    ):
        return "jugador"
    else:
        return "computadora"

def mostrar_resultado(resultado):
    if resultado == "empate":
        print("🔵 Resultado: EMPATE")
    elif resultado == "jugador":
        print("🟢 Resultado: ¡GANASTE!")
    else:
        print("🔴 Resultado: LA COMPUTADORA GANA")

def mostrar_puntajes(p_jugador, p_computadora, p_empates):
    print("\n📊 MARCADOR ACTUAL")
    print(f"Jugador: {p_jugador}")
    print(f"Computadora: {p_computadora}")
    print(f"Empates: {p_empates}")

def ejecutar_juego():
    puntos_jugador = 0
    puntos_computadora = 0
    empates = 0

    mostrar_titulo()

    while True:
        mostrar_menu()
        jugador = obtener_eleccion_jugador()

        if jugador is None:
            continue

        if jugador == "4":
            print("\n🎮 Gracias por Jugar")
            mostrar_puntajes(puntos_jugador, puntos_computadora, empates)
            break

        eleccion_jugador = traducir_eleccion(jugador)
        print(f"👉 Tú elegiste: {eleccion_jugador}")

        eleccion_computadora = obtener_eleccion_computadora()
        print(f"💻 La computadora eligió: {eleccion_computadora}")

        resultado = determinar_resultado(eleccion_jugador, eleccion_computadora)
        mostrar_resultado(resultado)

        if resultado == "jugador":
            puntos_jugador += 1
        elif resultado == "computadora":
            puntos_computadora += 1
        else:
            empates += 1

        mostrar_puntajes(puntos_jugador, puntos_computadora, empates)

ejecutar_juego()
