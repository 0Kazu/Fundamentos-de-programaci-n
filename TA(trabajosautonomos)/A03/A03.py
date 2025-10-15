## Parte 01:
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(f"Celsius: {celsius:>10.2f}")
print(f"Fahrenheit: {fahrenheit:>10.2f}")

## Parte 02:
nombre_completo = input("Ingrese su nombre y apellido: ").title().split()
nombre = nombre_completo[0]
apellido = nombre_completo[1]

edad = int(input("Ingrese su edad: "))
matricula = input("Ingrese su matrícula: ")

user_name = nombre[0:2] + apellido[0:2] + matricula[-2:] + str(edad + 5)

print(f"Username:{user_name:>15}")