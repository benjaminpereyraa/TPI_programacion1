import random

def iniciar_juego():
    def desordenar_palabra(palabra):
        """Desordena las letras de la palabra."""
        palabra_lista = list(palabra.replace(" ", ""))
        random.shuffle(palabra_lista)
        return ''.join(palabra_lista)

    def leer_palabras(archivo):
        """Lee las palabras desde un archivo de texto."""
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                palabras = file.read().splitlines()
            return palabras
        except FileNotFoundError:
            print(f"Error: El archivo {archivo} no se encuentra.")
            return []


    def seleccionar_nivel(nivel):
        """Selecciona el archivo según el nivel."""
        if nivel == 1:
            return 'sustantivos.txt'
        elif nivel == 2:
            return 'adjetivos.txt'
        elif nivel == 3:
            return 'verbos.txt'
        else:
            return None

    def obtener_tipo_palabras(nivel):
        """Devuelve el tipo de palabra correspondiente al nivel."""
        if nivel == 1:
            return 'SUSTANTIVOS'
        elif nivel == 2:
            return 'ADJETIVOS'
        elif nivel == 3:
            return 'VERBOS'
        else:
            return ''

    def juego():
        """Función principal que maneja la lógica del juego."""
        niveles = [1, 2, 3]
        nivel_actual = 0
        vidas = 3
        palabras_adivinadas = 0

        while nivel_actual < len(niveles):
            archivo_palabras = seleccionar_nivel(niveles[nivel_actual])
            tipo_palabras = obtener_tipo_palabras(niveles[nivel_actual])
            palabras = leer_palabras(archivo_palabras)

            if not palabras:  # Si no se pueden cargar las palabras, se termina el juego
                print("No se pudieron cargar las palabras. El juego terminará.")
                break

            palabras_usadas = set()

            while vidas > 0 and palabras_adivinadas < 20:
                palabra = random.choice(palabras)
                while palabra in palabras_usadas:
                    palabra = random.choice(palabras)
                palabras_usadas.add(palabra)

                palabra_desordenada = desordenar_palabra(palabra)
                print(f"{tipo_palabras} (ordena las letras para formar la palabra): {palabra_desordenada}")

                intento = input("Tu respuesta: ").strip().lower()
                if intento == palabra.strip().lower():
                    print("¡Correcto!")
                    palabras_adivinadas += 1
                else:
                    print(f"Incorrecto. La palabra correcta era: {palabra}. Pierdes una vida.")
                    vidas -= 1

                print(f"Vidas restantes: {vidas}")
                print(f"Palabras adivinadas: {palabras_adivinadas}/20")

            if palabras_adivinadas == 20:
                print(f"¡Felicidades! Has completado el nivel {niveles[nivel_actual]} ({tipo_palabras}).")
                nivel_actual += 1
                palabras_adivinadas = 0
                vidas = 3
            else:
                print("Has perdido todas tus vidas. El juego se reinicia.")
                nivel_actual = 0
                palabras_adivinadas = 0
                vidas = 3

        print("¡Perfecto, completaste todos los niveles!")

    juego()

# Iniciar el juego
iniciar_juego()