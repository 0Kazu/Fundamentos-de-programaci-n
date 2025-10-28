## DESARROLLE EL TALLER
## NOMBRE Y APELLIDO
import random as rd

palabras = ["lista", "papel", "pluma", "claro", "cinco"]
print(f'Palabras: {palabras}')
print(f'Palabra secreta: _ _ _ _ _')

palabra_secreta = rd.choice(palabras)

palabra_ingresada = input("Ingrese una palabra de la lista: ")

if palabra_ingresada in palabra_secreta:
  print(f'¡Ganaste! La palabra era {palabra_secreta}.')
else:
  print(f'Incorrecto. La palabra no es {palabra_ingresada}.')

