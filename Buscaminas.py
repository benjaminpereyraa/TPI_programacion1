def iniciar_buscaminas():
    import random

    # Tamaño del tablero y número de minas
    filas = 5
    columnas = 5
    num_minas = 3

    # Crear el tablero vacío
    tablero = [[' ' for _ in range(columnas)] for _ in range(filas)]
    descubiertas = [[False for _ in range(columnas)] for _ in range(filas)]

    # Colocar minas en posiciones aleatorias
    minas_colocadas = 0
    while minas_colocadas < num_minas:
        fila_mina = random.randint(0, filas - 1)
        columna_mina = random.randint(0, columnas - 1)
        if tablero[fila_mina][columna_mina] != 'M':
            tablero[fila_mina][columna_mina] = 'M'
            minas_colocadas += 1

    # Función para contar minas alrededor de una celda
    def contar_minas_alrededor(fila, columna):
        conteo = 0
        for i in range(fila - 1, fila + 2):
            for j in range(columna - 1, columna + 2):
                if 0 <= i < filas and 0 <= j < columnas and tablero[i][j] == 'M':
                    conteo += 1
        return conteo

    # Función para mostrar el tablero al jugador
    def mostrar_tablero():
        for i in range(filas):
            for j in range(columnas):
                if descubiertas[i][j]:
                    print(tablero[i][j], end=' ')
                else:
                    print('*', end=' ')
            print()

    # Bucle principal del juego
    while True:
        mostrar_tablero()

        # Pedir al usuario las coordenadas
        fila = int(input("Ingrese un número de fila del 0 al 4: "))
        columna = int(input("Ingrese un número de columna del  0 al 4: "))
        
        # Validar las coordenadas ingresadas
        if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
            print("Coordenadas fuera del rango. Inténtelo de nuevo.")
            continue

        # Verificar si la celda ya fue descubierta
        if descubiertas[fila][columna]:
            print("¡Ya has descubierto esta celda!")
            print(       "Elige otra.")
            continue

        # Verificar si el usuario ha descubierto una mina
        if tablero[fila][columna] == 'M':
            print( "   ¡¡¡Boom!!!" )
            print("¡Encontraste una mina!")
            print("  Juego terminado.")
            break

        # Contar minas alrededor y mostrar el número
        minas_cercanas = contar_minas_alrededor(fila, columna)
        tablero[fila][columna] = str(minas_cercanas)
        descubiertas[fila][columna] = True
        
        print("Celda segura. ¡Sigue jugando!")

iniciar_buscaminas()