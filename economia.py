from cryptography.fernet import Fernet

ARCHIVO_FICHAS = "fichas.json"
CLAVE_FERNET = b'4WVabWzje3Ucvbtd-uqqSSTTiyz-24Dhw6W3maYR-lQ='


fernet = Fernet(CLAVE_FERNET) 


class Jugador:
    def __init__(self,Fichas): 
        self.fichas = Fichas
        #self.cartas = 10


def cargar_fichas() -> None:
    global PJ
    try:
        with open(ARCHIVO_FICHAS,'r', encoding="UTF-8") as archivo:
            
            #nigg = archivo.read()
            fichas_encryp = fernet.decrypt(archivo.read())
            fichas_desencriptado = fichas_encryp.decode()
        
        
            PJ = Jugador(int(fichas_desencriptado))
            if PJ.fichas == 0:
                print("como vas a perder todo, toma te regalo 100🎟️")
                PJ.fichas = 100
            else:
                print("datos cargados")
        
    except FileNotFoundError:
        #si no encuentra el archivo, le asigno y lo creo
        with open(ARCHIVO_FICHAS,'w', encoding="UTF-8") as archivo:
            print("se ve q no tenes fichas creando archivo nuevo...")
            archivo.write("100")
            
            #se pone asi pq si no, no se inicializa que es PJ
            #   NameError: name 'PJ' is not defined
            PJ = Jugador(100)
    except ValueError:
        #si encuentra el archivo, pero esta vacio o tiene un valor q no debe lo cambia
        with open(ARCHIVO_FICHAS,'w', encoding="UTF-8") as archivo:
                    print("archivo de fichas corrompido, creando archivo nuevo...")
                    archivo.write("100")
                    PJ = Jugador(100)
    except:
        #si encuentra el archivo, pero esta vacio o tiene un valor q no debe lo cambia
        with open(ARCHIVO_FICHAS,'w', encoding="UTF-8") as archivo:
                    print("archivo de fichas corrompido, creando archivo nuevo...")
                    archivo.write("100")
                    PJ = Jugador(100)

def guardar_fichas() -> None:
    global PJ
    
    try:
        #binary mode doesn't take an encoding argument
        with open(ARCHIVO_FICHAS,'wb') as archivo:
            
            #encriptado antitrampas
            fichas = PJ.fichas
            fichas_b = str(fichas).encode()
            fichas_encryp = fernet.encrypt(fichas_b)
            
            #escribo en el txt, los tickets encriptados
            archivo.write(fichas_encryp)
            print(f"Se guardaron las {PJ.fichas}🎟️  fichas")
    except FileNotFoundError:
        print("error al guardar las fichas")

#se fija cuanto saldo tiene el jugador
def saldo() -> None: print(f"Actualmente tenés {PJ.fichas} fichas🎟️")

#esta funcion es para verificar si podemos o no hacer la apuesta
# y descuenta las fichas apostadas
def apostar() -> int:

    def es_int(apuesta):
        try:
            apuesta = int(apuesta)
            return True
        except ValueError:
            return False


    if PJ.fichas == 0:
                print("no tenes fichas pa")
                #devuelve 0 para q se cierre el programa en main
                apuesta = 0
                return apuesta


    while True:
        print(f"Tenés {PJ.fichas} fichas🎟️, cuanto querés apostar?")
        print("(a) Para apostar todo ")

        apuesta = input()


        if es_int(apuesta) == True:
            apuesta = int(apuesta)
            # como chekear si es un int o un str?
            if apuesta > PJ.fichas:
                print("Fichas insuficientes")

            

            if apuesta <= 0:
                print("La apuesta debe ser mayor a 0.")

            else:
                PJ.fichas -= apuesta 
                return apuesta
        else:
            if apuesta.lower() == 'a':
                apuesta = PJ.fichas
                PJ.fichas -= apuesta
                return apuesta
            print("Flaco te pedi un número, o aposta todo (a)")


def ganar(apuesta: int) -> None:
    
    resultado = apuesta * 2
    
    print(f"Conseguiste {resultado}🎟️")
    PJ.fichas += resultado

def perder(apuesta: int) -> None:
    
    print(f"Perdiste {apuesta}🎟️")

def empate(apuesta: int) -> None:
    PJ.fichas += apuesta
    print("Te devolvimos lo que apostaste")

def ganar21(apuesta: int) -> None:
    
    resultado = apuesta + (apuesta * 1.5)
    #lo reconvierto a int pq puede tirar float
    resultado = int(resultado)

    print(f"Conseguiste {resultado}🎟️")
    PJ.fichas += resultado

def hesoyam() -> None:
    PJ.fichas += 10000
    saldo()

