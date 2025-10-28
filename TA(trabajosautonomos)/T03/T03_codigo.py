"""
# Taller: Cálculo del IMC (Indice de Masa Corporal)

Este taller consiste en desarrollar un programa que calcule el Índice de Masa Corporal (IMC) de una persona y determine su clasificación. Se debe:
1. crear una función para calcular el IMC,
2. crear una función para clasificar el IMC,
3. solicitar los datos del usuario,
4. mostrar el resultado del IMC calculado y su clasificación.

### Pasos a seguir

1. Crear la función `calcular_imc(peso, altura)`:
   * Esta función debe recibir dos parámetros: el peso en kilogramos y la altura en metros.
   * Utiliza la fórmula:
     **IMC = peso / altura^2**
   * Devuelve el valor del IMC con dos decimales.
   
2. Crear la función `clasificar_imc(imc)`:
   * Esta función recibe el valor del IMC calculado.
   * Usa condicionales para devolver la clasificación correspondiente:
     * "Bajo Peso" si el IMC es menor a 18.5,
     * "Peso Normal" si es menor a 24.9,
     * "Sobrepeso" si es menor a 29.9,
     * "Obesidad" si es mayor a 29.9.
     
3. En el programa principal:
   * Solicitar al usuario su peso y altura mediante `input()`.
   * Llamar a las funciones `calcular_imc` y `clasificar_imc` y almacenar los resultados.
   * Mostrar al usuario su IMC calculado y la clasificación correspondiente.

### Ejemplo de ejecución

```python
Ingresa tu peso en kg: 70
Ingresa tu altura en metros: 1.75
Tu IMC es 22.86. Clasificación: Peso normal
"""

## DIEGO JOSÉ TELLO HIDALGO

## FUNCIONES
def calcular_imc(peso, altura):
  return float(f'{(peso / (altura ** 2)):.2f}')

def clasificar_imc(imc=0  ):
  if imc < 18.5:
    return "Bajo peso"
  elif imc < 24.9 and imc > 18.5:
    return "Peso Normal"
  elif imc < 29.9 and imc > 24.9:
    return "Sobrepeso"
  else:
    return "Obesidad"

## PROGRAMA PRINCIPAL
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)
estado_imc = clasificar_imc(imc)

print(f'Tu IMC es {imc}. Clasificación: {estado_imc}')

