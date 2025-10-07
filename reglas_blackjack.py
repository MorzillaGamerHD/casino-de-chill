from generar_mano import generar_carta as gencarta
import economia as eco
import time

# se fija si el A se toma como 1 u 11
def calcular_valor_mano(mano):
    # Suma inicial (asumiendo Ases como 11. Ojo: el conteo de tu generar_mano
    # hace que todos los Ases lleguen aquí como valor 1, por lo que este sum()
    # sumará 1 para los Ases inicialmente.
    total = sum(valor for i, valor in mano)
    
    # Cuenta cuántos Ases hay
    ases = sum(1 for carta, i in mano if carta.startswith("A"))
    
    # Itera para convertir Ases de 1 a 11 si es posible (si el total no se pasa de 21)
    # y luego de 11 a 1 si es necesario para no pasarse. 
    # **IMPORTANTE**: Tu código de generar_mano.py asigna conteo=1 para el As (carta=1),
    # por lo que al principio, total tendrá Ases como 1.
    # El bucle while DEBE estar al revés para darles el valor 11 primero.
    # Vamos a SIMPLIFICAR la función para manejar la lógica de forma más directa, 
    # ASUMIENDO que todos los Ases dan un valor INICIAL de 1:
    
    # 1. Sumar todos los valores, Ases cuentan como 1.
    total = sum(valor for i, valor in mano)
    
    # 2. Convertir Ases de 1 a 11, *siempre que el total no exceda 21*.
    ases = sum(1 for carta, i in mano if carta.startswith("A"))
    
    # Intentar que los Ases valgan 11
    for _ in range(ases):
        if total + 10 <= 21: # Si sumarle 10 (para convertir un 1 en 11) no excede 21
            total += 10 # Se le suma 10 al total (el As ya suma 1)
            
    return total


def blackjack(apuesta):
    #genera las cartas del dealer
    

    cartas_dealer = []
    cartas_dealer.append(gencarta())

    #conteo_dealer = cartas_dealer1[1] + cartas_dealer2[1]

    print(f"La carta del dealer son {[c[0] for c in cartas_dealer]}, [??]")


    #genera las cartas del jugador
    cartas_jugador = []
    cartas_jugador.append(gencarta())
    cartas_jugador.append(gencarta())

    conteo_jugador = calcular_valor_mano(cartas_jugador)

    print(f"Tus cartas son {[c[0] for c in cartas_jugador]}, en total {conteo_jugador}")



    #pedir cartas
    while True:
        pedir = input("Pedir (P) o Quedarse? (X): ")
        if pedir.lower() == 'p':
            carta = gencarta()
            cartas_jugador.append(carta)
            #aca llamo a la funcion
            conteo_jugador = calcular_valor_mano(cartas_jugador)
            time.sleep(0.5)
            print(f"Te salió {carta[0]}, ahora tenés {[c[0] for c in cartas_jugador]} en total {conteo_jugador}")
            print("")
            if conteo_jugador > 21:
                print("Te pasaste, perdiste 🤣🤣🤣🤣🤣")
                eco.perder(apuesta)
                break
        else:
            break



    if conteo_jugador <= 21:
        #regla del crupier
        #genero la carta y lo guarto en la variable carta
        carta = gencarta()
        #ahora meto los valores de "carta" en las cartas del crupier
        cartas_dealer.append(carta)
        #aca hago q el conteo dealer llame a la funcion de calcular mano dandole los valores de las cartas
        conteo_dealer = calcular_valor_mano(cartas_dealer)
        time.sleep(1.5)
        print("")
        print(f"El dealer revelo su carta {carta[0]}, ahora tiene {[c[0] for c in cartas_dealer]} en total {conteo_dealer}")

        while conteo_dealer < 17:
            print("El dealer pide una carta...")
            time.sleep(1.5)
            carta = gencarta()
            cartas_dealer.append(carta)
            conteo_dealer = calcular_valor_mano(cartas_dealer) 
            print(f"El dealer saco una carta {carta[0]}, ahora tiene {[c[0] for c in cartas_dealer]} en total {conteo_dealer}")

            if conteo_dealer == 21 and conteo_jugador < 21:
                print("El dealer te rompio el ojete 💥💥💥")
                eco.perder(apuesta)
                break 

            elif conteo_dealer > 21 and conteo_jugador != 21:
                print("El dealer se pasó 💥")
                eco.ganar(apuesta)
                break 

    #Resultado de partida
    if conteo_jugador <= 21:
        if conteo_jugador == 21 and conteo_dealer < conteo_jugador:
            print("Ganaste con 21🤑🤑")
            eco.ganar21(apuesta)
        elif conteo_dealer < conteo_jugador:
            print("Ganaste 🤑🤑")
            eco.ganar(apuesta)
        elif conteo_dealer == conteo_jugador:
            print("Empate")
            eco.empate(apuesta)
        elif conteo_dealer > conteo_jugador and conteo_dealer != 21:
            print("Perdiste petón")
            eco.perder(apuesta)




