nombre_completo = input("Ingrese su nombre completo: ")
# Obtener su primer nombre
primer_nombre = nombre_completo.split(' ')[0].upper()

edad = int(input(f"{primer_nombre}, ingrese su edad: "))

salario_mensual = float(input("Ahora, ingrese su salario mensual: "))
alario_anual = salario_mensual * 12
print("\npresentando datos...")
print("Nombre de la persona:", primer_nombre)
print("Edad de la persona:", edad)
print("Salario mensual de la persona:", salario_mensual)
print("Salario anual de la persona:", alario_anual)