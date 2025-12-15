import random

def get_random_choice():
    return random.choice(["piedra", "papel", "tijera"])

def normalize_choice(text):
    return str(text).strip().lower()

# Espacio para agregar más utilidades
