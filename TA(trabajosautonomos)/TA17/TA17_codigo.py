import numpy as np

arr_temperaturas = np.random.randint(22, 39, size=7)

lista_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

print("Datos:")
print("Días:", lista_semana)
print("Temperaturas:", arr_temperaturas)

print("\n1. Temperatura del cuarto día:")
print(f"{lista_semana[3]}: {arr_temperaturas[3]} grados")

print("\n2. Temperaturas de los primeros tres días:")
for i in range(3):
    print(f"{lista_semana[i]}: {arr_temperaturas[i]} grados")


print("\n3. Promedio de temperaturas en días pares:")
temps_pares = arr_temperaturas[::2]
promedio = np.mean(temps_pares)

print(f"Temperaturas tomadas: {temps_pares}")
print(f"Promedio: {promedio:.2f}")

print("\n4. Días con temperatura mayor a 28 grados:")

condicion = arr_temperaturas > 28

dias_filtrados = np.array(lista_semana)[condicion]
temps_filtradas = arr_temperaturas[condicion]

cantidad_dias = len(dias_filtrados)

for i in range(cantidad_dias):
    print(f"{dias_filtrados[i]}: {temps_filtradas[i]} grados")