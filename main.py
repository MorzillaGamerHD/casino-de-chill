import reglas_blackjack as blackjack
import economia as eco
from generar_mano import borrar_cartas
import time

def juego() -> None:
    while True:
        print("q jeugo quers jugar?")
        respuesta: str = input("Blackjack? (B), Pocker (P), Ruleta(R)")
        match respuesta.lower():
            case 'b':
                ...
                break
            case 'p':
                ...
                break
            case 'r':
                ...
                break
            case _:
                print("respuesta invalida")
                pass

def bienvenida() -> None:
    print("====================================")
    print("  ¡BIENVENIDO AL CASINO DEL PAPU!   ")
    print("====================================")
    print("WIP v0.2.3\n")



if __name__ == "__main__":

    borrar_cartas()
    bienvenida()

    time.sleep(0.7)
    eco.cargar_fichas()
    # no es necesario pq eco.apostar ya te muestra cuanto tenes asads
    #eco.saldo()


    while True:
        print("\n--- COMENZANDO NUEVA MANO ---")
        time.sleep(0.7)
        apuesta = eco.apostar()
        time.sleep(0.7)

        #este if es para q no se haga un bucle y se cierre el juego
        #por si elejis q no quers seguir te saca directamente
        if apuesta == 0:
            print("¡Gracias por jugar! 👋")
            time.sleep(2)
            eco.guardar_fichas()
            borrar_cartas()
            break
        else:

            blackjack.blackjack(apuesta)
            borrar_cartas()
            time.sleep(1)

            volver_a_jugar: str = input("\n¿Querés jugar otra mano? (S/N): ")
            match volver_a_jugar:
                case 'z':
                    eco.hesoyam()
                case 's':
                    pass
                case _:
                    eco.saldo()
                    print("¡Gracias por jugar! 👋")
                    time.sleep(2)
                    eco.guardar_fichas()
                    break
# CTRL + K + C

