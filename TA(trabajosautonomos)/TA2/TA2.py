"""
# Actividad 01:

### Récord de corredor de maratón.

**Problema:**
Un corredor de maratón registró su tiempo al inicio y al finalizar una carrera en minutos como cadenas. Se desea determinar cuántos minutos transcurrieron entre ambos tiempos y luego verificar si mejoró su récord previo.

**Ejercicio:**
- Crear tres variables: `tiempo_inicio`, `tiempo_fin` y `record_previo`. Asignar a a las variables los tiempos en minutos pero almacenados como  cadenas.
- Convertir las cadenas a enteros.
- Calcular la diferencia de minutos entre `tiempo_fin` y `tiempo_inicio`.
- Verificar si la diferencia de minutos es menor que `record_previo`.
- Mostrar por consola la cantidad de minutos transcurridos entre el inicio y el final de la carrera y si el corredor mejoró su récord previo.
"""

tiempo_inicio = '25'
tiempo_fin = '48'
record_previo = "24"

diferencia_tiempo = int(tiempo_fin) - int(tiempo_inicio)

mejoro_record = diferencia_tiempo < int(record_previo)
# ya que el record es el menor tiempo en hacer algo

print("Su carrera duró", diferencia_tiempo, "minutos.")
print("Su record anterior fue:", record_previo)
print("El corredor superó su record:", mejoro_record)

"""# Actividad 02:

### Sumar dígitos de una cadena.

**Problema:**
Se desea sumar los dígitos de un número de 3 cifras que está almacenado como una cadena. Se pide realizar esta operación solo utilizando operadores aritméticos.

**Ejercicio:**
- Crear una variable `numero` y asignarle un número de tres cifras como una cadena. Ejemplo: `numero = '538'`
- Convertir el número en entero para los siguientes pasos.
- Utilizar el operador de división entera (`//`) para obtener el cociente de dividir `numero` por 100. Esto dará el dígito de las centenas.
- Luego, utilizar el operador de residuo (`%`) para obtener el residuo de dividir `numero` por 100. Después, utilizar el operador de división entera nuevamente para dividir este resultado por 10. Esto dará el dígito de las decenas.
- Utilizar el operador de residuo (`%`) nuevamente para obtener el residuo de dividir `numero` por 10. Esto dará el dígito de las unidades.
- Sumar los tres dígitos obtenidos en los pasos anteriores.
- Mostrar por consola la suma de los dígitos.


"""

numero_cadena = "538"
numero_entero = int(numero_cadena)

# Dígitos para el número
centenas = str(numero_entero // 100)
decenas = str((numero_entero % 100) // 10)
unidades = str((numero_entero % 100) % 1)

# Formando el nuevo número
nuevo_numero = centenas + decenas + unidades
print("El número formado es", nuevo_numero)