import random

#genera los numeros q se convierten en cartas
def gencartas():
   carta = random.randrange(1,14)
   palo_carta = random.randrange(1,5)

   return carta, palo_carta

#guardar en el archivo de las fichas las cartas q salen y chekear si salen 
#para no repetir 
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
   carta, palo = gencartas()
   carta_f = asignar_valores_cartas(carta, palo)

   return carta_f
