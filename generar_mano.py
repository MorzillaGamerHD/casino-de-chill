import random
import os

#genera los numeros q se convierten en cartas
def gencartas():
   carta = random.randrange(1,14)
   palo_carta = random.randrange(1,5)

   return carta, palo_carta

#pensar q pasa si se cierra el programa en el medio
#con las cartas en el archivo

#le da los valores del las cartas de póker
def asignar_valores_cartas(carta, palo_carta):

   conteo = carta    
   if conteo <= 10:
      conteo = carta
   else:
      conteo = 10

   figuras = {1: "A", 11: "J", 12: "Q", 13: "K"}
   palos = {1: "♠️", 2: "🍀", 3: "♦️", 4: "♥️"}

   #q significa figura[carta]
   if carta in figuras:
      carta = figuras[carta]
   #palos.get?
   palo_carta = palos.get(palo_carta, "?")



   carta_final = str(carta) + palo_carta


   return carta_final, conteo

#es para generar una carta 
def generar_carta():
   
   while True:
      carta, palo = gencartas()
      carta_f = asignar_valores_cartas(carta, palo)
      #print("1")
      #print(leer_carta(carta_f)) #unboundlocalerror por lo q me tira none

      if leer_carta(carta_f) == False:
         guardar_carta(carta_f)
         break
      
      elif leer_carta == 50:
         borrar_cartas()
         pass
      else:
         #carta, palo = gencartas()
         #print("3")
         pass


   return carta_f


def guardar_carta(carta):

   with open("cartas.json",'a', encoding="UTF-8") as archivo:
      archivo.writelines(f'{carta[0]}\n')

def leer_carta(carta):
   try:
      with open("cartas.json",'r', encoding="UTF-8") as archivo:

         lineas = archivo.readlines()
         conteo_linea = 1

         for linea in lineas:
            #print(f"{linea}")

            # necesito transformarlo en dupla para q los emojis se hagan legibles (♠, ♦, 🍀, ♥)
            carta_tupla = tuple(carta[0])
            linea_tupla = tuple(linea)

            # al hacerlos tupla el numero y el palo me quedan separados 
            # y aca los junto
            tupla_mejorada = linea_tupla[0] + linea_tupla[1]
            carta_tupla_mejorada = carta_tupla[0] + carta_tupla[1]


            # si la carta esta en el archivo devuelve True
            
            if tupla_mejorada == carta_tupla_mejorada:
               conteo_linea+=1
               break
            else:
               pass

      #vuelvo a chekear pq si no, no termina el for
      if conteo_linea != 50:
         if tupla_mejorada == carta_tupla_mejorada:
            return True
         else:
               return False
      else:
         return 50
   except FileNotFoundError:
      #esto es por si no encuentra el archivo, ya q 
      #se ejecuta primero este y esta en modo leer
      with open("cartas.json",'w', encoding="UTF-8") as archivo:
         pass
      return False
   except UnboundLocalError: #si no encuentra nada dentro del archivo, tira error
      return False

def borrar_cartas():
   ruta_del_archivo = 'cartas.json'

   # Verifica si el archivo existe antes de intentar borrarlo
   if os.path.exists(ruta_del_archivo):
      os.remove(ruta_del_archivo)
      #print(f"El archivo '{ruta_del_archivo}' ha sido eliminado exitosamente.")
   else:
      print(f"El archivo '{ruta_del_archivo}' no existe.")

