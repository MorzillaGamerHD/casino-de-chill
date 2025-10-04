import time
import os
from cryptography.fernet import Fernet

clave = b'4WVabWzje3Ucvbtd-uqqSSTTiyz-24Dhw6W3maYR-lQ='
fernet = Fernet(clave)

class Jugador:
    def __init__(self,Fichas):
        self.fichas = Fichas


def cargar_fichas():
    global PJ
    try:
        with open("fichas.txt",'r', encoding="UTF-8") as archivo:
            
            nigg = archivo.read()
            fichas_encryp = fernet.decrypt(nigg)
            fichas_decryp = fichas_encryp.decode()
        
        
            PJ = Jugador(int(fichas_decryp))
            if PJ.fichas == 0:
                print("como vas a perder todo, toma te regalo 100🎟️")
                PJ.fichas = 100
            else:
                print("datos cargados")
        
    except FileNotFoundError:
        #si no encuentra el archivo, le asigno y lo creo
        with open("fichas.txt",'w', encoding="UTF-8") as archivo:
            print("se ve q no tenes fichas creando archivo nuevo")
            archivo.write("100")
            PJ = Jugador(100)
    except ValueError:
        #si encuentra el archivo, pero esta vacio o tiene un valor q no debe lo cambia
        with open("fichas.txt",'w', encoding="UTF-8") as archivo:
                    print("archivo de fichas corrompido, creando archivo nuevo")
                    archivo.write("100")
                    PJ = Jugador(100)
    except:
        #si encuentra el archivo, pero esta vacio o tiene un valor q no debe lo cambia
        with open("fichas.txt",'w', encoding="UTF-8") as archivo:
                    print("archivo de fichas corrompido, creando archivo nuevo")
                    archivo.write("100")
                    PJ = Jugador(100)





def guardar_fichas():
    global PJ
    
    try:
        #binary mode doesn't take an encoding argument
        with open("fichas.txt",'wb') as archivo:
            
            #encriptado antitrampas
            fichas = PJ.fichas
            fichas_b = str(fichas).encode()
            fichas_encryp = fernet.encrypt(fichas_b)
            
            #escribo en el txt, los tickets encriptados
            archivo.write(fichas_encryp)
            print(f"se guardaron las {PJ.fichas}🎟️ fichas")
    except FileNotFoundError:
        print("error al guardar las fichas")




#se fija cuanto saldo tiene el jugador
def saldo():
    print(f"Actualmente tenés {PJ.fichas} fichas🎟️")


#esta funcion es para verificar si podemos o no hacer la apuesta
def apostar():
    
    while True:
        try:
            if int(PJ.fichas) <= 0:
                print("flaco q queres apostar?")
                print("perdiste todo, aprende a apostar")
                time.sleep(1)
                print("ahora vas a perder tambien")
                time.sleep(1)
                print("pero el system32💀")
                time.sleep(2.5)
                os.system("rundll32.exe user32.dll,LockWorkStation")
                PJ.fichas = 0
                apuesta = 0

                time.sleep(2.5)
                print("bromita jeje")
                break

            else:
                print(f"Tenés {PJ.fichas} fichas🎟️, cuanto querés apostar?")
                apuesta = int(input())

                
                if int(PJ.fichas) < apuesta:
                    print(f"Fichas insuficientes")

                elif apuesta <= 0:
                    print("La apuesta debe ser mayor a 0.")
                    
                
                else: 
                    PJ.fichas -= apuesta 
                    break

        except ValueError:
            print("Flaco te pedi un número, sos o te haces?")
        


    return apuesta

def ganar(apuesta):
    
    resultado = apuesta * 2
    
    print(f"Conseguiste {resultado}🎟️")
    PJ.fichas += int(resultado)

def perder(apuesta):
    
    print(f"Perdiste {apuesta}🎟️")

def empate(apuesta):
    PJ.fichas += apuesta
    print("Te devolvimos lo que apostaste")

def ganar21(apuesta):
    
    resultado = apuesta + (apuesta * 1.5)

    print(f"Conseguiste {resultado}🎟️")
    PJ.fichas += int(resultado)

