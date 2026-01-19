#Escriba su solución (EJERCICIO 01):
def cambiar_extension(nombre_archivo, nueva_extension):
  if "." in nombre_archivo:
    lista_nombre_archivo = nombre_archivo.split(".") # ["datos", "png"]
    lista_nombre_archivo[-1] = nueva_extension # ["datos", "jpg"]
    nuevo_nombre = ".".join(lista_nombre_archivo) # Une a los elementos con puntos
    return nuevo_nombre
  else:
    return nombre_archivo # Sino retorna el nombre sin modificarlo







#Escriba su solución (EJERCICIO 02):
def ronda_juego(nombre1, nombre2):
  items_juego = ["piedra", "papel", "tijeras"]
  jugador1 = input(f'{nombre1}, elige piedra, papel o tijeras: ')
  jugador2 = input(f'{nombre2}, elige piedra, papel o tijeras: ')
  if jugador1 == jugador2:
      print("Hubo empate.")
  elif (jugador1 == "piedra" and jugador2 == "tijeras") or (jugador1 == "tijeras" and jugador2 == "papel") or (jugador1 == "papel" and jugador2 == "piedra"):
      return f"Gana {nombre1}"
  else:
      return f"Gana {nombre2}"

#Programa Principal
victorias_J1,victorias_J2 = 0,0
mensaje_final = ""

print("RONDA 1")
mensaje_ronda = ronda_juego("Diego", "Rocio")
print(mensaje_ronda + "\n")
if mensaje_ronda == "Gana Diego":
    victorias_J1 += 1
elif mensaje_ronda == "Gana Rocio":
    victorias_J2 += 1

print(f"RONDA 2")
mensaje_ronda = ronda_juego("Diego", "Rocio")
print(mensaje_ronda + "\n")
if mensaje_ronda == "Gana Diego":
    victorias_J1 += 1
elif mensaje_ronda == "Gana Rocio":
    victorias_J2 += 1

print("RONDA 3")
mensaje_ronda = ronda_juego("Diego", "Rocio")
print(mensaje_ronda + "\n")
if mensaje_ronda == "Gana Diego":
    victorias_J1 += 1
elif mensaje_ronda == "Gana Rocio":
    victorias_J2 += 1

print("RONDA 4")
mensaje_ronda = ronda_juego("Diego", "Rocio")
print(mensaje_ronda + "\n")
if mensaje_ronda == "Gana Diego":
    victorias_J1 += 1
elif mensaje_ronda == "Gana Rocio":
    victorias_J2 += 1

print("RONDA 5")
mensaje_ronda = ronda_juego("Diego", "Rocio")
print(mensaje_ronda + "\n")
if mensaje_ronda == "Gana Diego":
    victorias_J1 += 1
elif mensaje_ronda == "Gana Rocio":
    victorias_J2 += 1