# Sin for, es necesario hacer uso de la recursividad.

def calcular_cuadrados(lista_numeros):
	if lista_numeros == []:
		return []
	else:
		primer_numero = lista_numeros[0]
		cuadrado_primer_numero = primer_numero**2

		lista_restante = lista_numeros[1:]
		lista_resultante = calcular_cuadrados(lista_restante) # Recursividad

		return [cuadrado_primer_numero] + lista_resultante
	
numeros = [2, 6, 8]
print(calcular_cuadrados(numeros))