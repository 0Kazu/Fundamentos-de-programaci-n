## ACTIVDAD 04
## INTEGRANTE 01, INTEGRANTE 02, INTEGRANTE 03

import random as rd

lista_de_reproduccion = ["Like Him",
                         "Yellow",
                         "See You Again",
                         "Feels",
                         "You And Me",
                         "Mind Over Matter",
                         "Everything",
                         "Lonely Day",
                         "The Night We Met",
                         "The Rumbling"
                         ]

print(f'Lista de reproducción original:\n{lista_de_reproduccion}\n')

cancion_aleatoria = rd.choice(lista_de_reproduccion)
print(f'Canción aleatoria:\n{cancion_aleatoria}\n')

n_canciones = int(input("Ingrese el número de canciones a reproducir: "))
n_canciones_seleccionadas = rd.choices(lista_de_reproduccion, k=n_canciones)
print(f'Canciones aleatorias:\n{n_canciones_seleccionadas}\n')

rd.shuffle(lista_de_reproduccion)
print(f'Lista de reproducción mezclada:\n{lista_de_reproduccion}\n')

nueva_cancion = input("Ingrese el título de la canción que desea añadir a su lista de reproducción: ")
lista_de_reproduccion.append(nueva_cancion)
print(f'Lista de reproducción actualizada:\n{lista_de_reproduccion}\n')

quitar_cancion = input("Ingrese el título de la canción que desea remover de su lista de reproducción: ")
lista_de_reproduccion.remove(quitar_cancion)
print(f'Lista de reproducción actualizada:\n{lista_de_reproduccion}\n')