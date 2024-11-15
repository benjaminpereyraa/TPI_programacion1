import random
import os
import time
import sys

def iniciar_juego():
    # Tamaño del tablero
    ancho = 20
    altura = 10

    # Dirección de la serpiente
    dx, dy = 1, 0  # Inicia moviéndose a la derecha

    # Posición inicial de la serpiente
    snake = [(5, 5), (5, 4), (5, 3)]  # Lista de posiciones (y, x)

    # Comida inicial
    food = (random.randint(0, altura-1), random.randint(0, ancho-1))

    # Función para dibujar el tablero
    def draw_board():
        os.system('cls' if os.name == 'nt' else 'clear')  # Limpiar la consola
        for y in range(altura):
            for x in range(ancho):
                if (y, x) == snake[0]:  # Cabeza de la serpiente
                    print("O", end="")
                elif (y, x) in snake[1:]:  # Cuerpo de la serpiente
                    print("■", end="")
                elif (y, x) == food:  # Comida
                    print("@", end="")
                else:
                    print(" ", end="")
            print()

    # Función para mover la serpiente
    def move_snake():
        nonlocal dx, dy, food
        head = snake[0]
        new_head = (head[0] + dy, head[1] + dx)  # Nueva posición de la cabeza

        # Si la serpiente come la comida
        if new_head == food:
            snake.insert(0, new_head)  # Añadir la nueva cabeza
            food = (random.randint(0, altura-1), random.randint(0, ancho-1))  # Nueva comida
        else:
            snake.insert(0, new_head)  # Añadir la nueva cabeza
            snake.pop()  # Eliminar la cola de la serpiente

    # Función para comprobar si el juego ha terminado
    def game_over():
        head = snake[0]
        # Comprobar si la cabeza de la serpiente toca los bordes o se muerde a sí misma
        if head[0] < 0 or head[0] >= altura or head[1] < 0 or head[1] >= ancho or head in snake[1:]:
            return True
        return False

    # Función para manejar la entrada del usuario
    def get_input():
        nonlocal dx, dy
        key = input("Usa 'w', 'a', 's', 'd' para mover: ").lower()
        if key == "w" and dy != 1:  # Arriba
            dx, dy = 0, -1
        elif key == "a" and dx != 1:  # Izquierda
            dx, dy = -1, 0
        elif key == "s" and dy != -1:  # Abajo
            dx, dy = 0, 1
        elif key == "d" and dx != -1:  # Derecha
            dx, dy = 1, 0

    # Bucle principal del juego
    while True:
        draw_board()
        get_input()
        move_snake()
        
        if game_over():
            print("¡Game Over!")
            sys.exit()
        time.sleep(0.2)  # Esperar un momento antes de actualizar
iniciar_juego()