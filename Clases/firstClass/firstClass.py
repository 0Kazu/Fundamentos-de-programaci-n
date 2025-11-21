lista = [3, 6, 12, 9, 1] # Definiendo una lista
total = 0

for elemento in lista:
  total += elemento
  print(total)

# Primera iteración elemento = 3 --> total += 3
# Segunda iteración elemento = 6 --> total += 6
# Segunda iteración elemento = 12 --> total += 12
# ...

promedio = total / len(lista)
print(f'El promedio es {promedio}')