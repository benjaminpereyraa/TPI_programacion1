
opcion = 5
while opcion != 0:
    print("-----------------------------")
    print("BIENVENIDOS A 4 EN 1")
    print("-----------------------------")
    print("1- TA-TE-TI")
    print("2- Buscamina")
    print("3- Snake")
    print("4- Juego de preguntas")
    print("0- Salir")
    
    opcion = int(input("Ingrese el número del juego que desees jugar o 0 para dejar de jugar: "))
    
    if opcion == 1:
        print("Iniciando TA-TE-TI...")
        from juegos.tatetii import iniciar_juego
    elif opcion == 2:
        print("Iniciando Buscamina...")
        from juegos.Buscaminas import iniciar_buscaminas
    elif opcion == 3:
        print("Iniciando Snake...")
        from juegos.snake import iniciar_juego
    elif opcion == 4:
        print("Iniciando Juego de preguntas...")
        # código para el juego de preguntas
    elif opcion == 0:
        print("Gracias por jugar")
    else:
        print("Opción no válida. Por favor, elige un número del 0 al 4.")