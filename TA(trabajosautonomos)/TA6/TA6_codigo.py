## SOLUCION DEL EJERCICIO
import random as rd

casos = ["piedra", "papel", "tijera"]
jugador1 = rd.randint(1,3)
jugador2 = rd.randint(1,3)

eleccion_jugador1 = casos[jugador1 - 1]
eleccion_jugador2 = casos[jugador2 - 1]

print(f'Jugador 1 eligió: {eleccion_jugador1}')
print(f'Jugador 2 eligió: {eleccion_jugador2}')

if jugador1 == jugador2:
  print(f'Empate.')
elif ((eleccion_jugador1 == "piedra" and eleccion_jugador2 == "tijera") or (eleccion_jugador1 == "tijera" and eleccion_jugador2 == "papel") or (eleccion_jugador1 == "papel" and eleccion_jugador2 == "piedra")):
  print("Jugador 1 gana.")
else:
  print(f'Jugador 2 gana.')

