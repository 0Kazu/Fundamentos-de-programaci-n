# -*- coding: utf-8 -*-
"""
# Actividad: Crear funciones y condicionales

# Parte 1

Crea una función que actúe como una calculadora simple. La función debe recibir dos números y una operación matemática (suma, resta, multiplicación o división) y devolver el resultado.

**Pasos para resolver:**

1. Define una función calculadora que reciba tres parámetros: dos números y una cadena de texto que indica la operación.
2. Dentro de la función, usa condicionales (if, elif, else) para verificar qué operación debe realizarse.
3. Si la operación es:
  * "suma", devuelve la suma de los dos números.
  * "resta", devuelve la resta de los dos números.
  * "multiplicación", devuelve el producto de los dos números.
  * "división", devuelve la división de los dos números.
4. Retorna con un f-string el resultado.

Ejemplo de Ejecución:

```python
Que operacion quiere realizar: suma
Primer numero: 2
Segundo numero: 3
El resultado de la suma es 5
"""

def calculadora(a=0, b=0, operacion=""):
	operaciones = ["suma", "resta", "multiplicación", "división", "multiplicacion", "division"]
	operacion = operacion.lower()

	if operacion in operaciones:
		if operacion == operaciones[0]:
			return f'El resultado de la suma es {a + b}'
		elif operacion == operaciones[1]:
			return f'El resultado de la resta es {a - b}'
		elif operacion == operaciones[2] or operacion == operaciones[4]:
			return f'El resultado de la multiplicación es {a * b}'
		elif operacion == operaciones[3] or operacion == operaciones[5]:
			if b == 0:
				return "ERROR: División por 0."
			else:
				return f'El resultado de la multiplicación es {a / b}'
	else:
		return "Ingrese una operación válida."
	
operacion = input("Qué operación quiere realizar: ")
primer_numero = float(input("Primer número: "))
segundo_numero = float(input("Segundo número: "))

print(calculadora(primer_numero, segundo_numero, operacion))

"""## Parte 2:

Este ejercicio consiste en desarrollar un programa que calcule los cuadrados de una lista de números. Se debe:
1. crear una función que reciba una lista de números,
2. devolver una nueva lista con los cuadrados de esos números.

### Pasos a seguir

1. Crear la función `calcular_cuadrados(lista_numeros)`:
   * Esta función debe recibir un parámetro: una lista de números.
   * Debe calcular el cuadrado de cada número en la lista y devolver una nueva lista con los resultados.

### Ejemplo de ejecución

```python
numeros = [1, 2, 3, 4]
resultado = calcular_cuadrados(numeros)
print(resultado)  # Salida esperada: [1, 4, 9, 16]

"""

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