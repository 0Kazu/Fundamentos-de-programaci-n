# Primer problema
# Escriba su solución:
cadena1 = input("Ingrese cadena1: ").lower()
cadena2 = input("Ingrese cadena2: ").lower()
resultado = f'{cadena2[:2] + cadena1[2:]} {cadena1[:2] + cadena2[2:]}'
print(resultado)



# Segundo problema
#Escriba su solución:
palabra_ingresada = input("Ingrese una palabra: ").lower()
longitud = len(palabra_ingresada)

print(f'El número total de caracteres es: {longitud} caracteres')
print(f'La cadena repetida conforme el número de caracteres que tiene es: {palabra_ingresada*longitud}')
print(f'Los tres primeros caracteres de la cadena son: {palabra_ingresada[:3]}')
print(f'Los tres últimos caracteres de la cadena son: {palabra_ingresada[-3:]}')
print(f'la palabra escrita al revés es: {palabra_ingresada[::-1]}')
print(f'La palabra escrita en mayúsculas es: {palabra_ingresada.upper()}')
print(f'La palabra sin letras a es: {palabra_ingresada.replace("a","")}')

palabra_sin_vocales = palabra_ingresada.replace("a","").replace("e","").replace("i","").replace("o","").replace("u","")
print(f'La palabra sin vocales es: {palabra_sin_vocales}')