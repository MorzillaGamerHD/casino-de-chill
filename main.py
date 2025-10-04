import reglas_blackjack as blackjack
import economia as eco
import time

def juego():
    print("q jeugo quers jugar?")
    respuesta = input("Blackjack? (B), Pocker (P), Ruleta(R)")
    print(respuesta)



if __name__ == "__main__":
    print("====================================")
    print("  ¡BIENVENIDO AL CASINO DEL PAPU!   ")
    print("====================================")
    print("WIP v0.2")



    time.sleep(0.7)
    eco.cargar_fichas()
    # no es necesario pq eco.apostar ya te muestra cuanto tenes
    #eco.saldo()


    while True:
        print("\n--- COMENZANDO NUEVA MANO ---")
        time.sleep(0.7)
        apuesta = eco.apostar()
        time.sleep(0.7)
        
        #este if es para q no se haga un bucle y se cierre el juego
        if apuesta == 0:
            print("¡Gracias por jugar! 👋")
            time.sleep(2)
            eco.guardar_fichas()
            break
        else:
            
            blackjack.blackjack(apuesta)
            time.sleep(1)
        
            volver_a_jugar = input("\n¿Querés jugar otra mano? (S/N): ")
            if volver_a_jugar.lower() != 's':
                eco.saldo()
                print("¡Gracias por jugar! 👋")
                time.sleep(2)
                eco.guardar_fichas()
                break
            