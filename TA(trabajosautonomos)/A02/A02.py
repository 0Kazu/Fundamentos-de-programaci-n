"""
### PROBLEMA 1.
1. Comparación de puntajes:

**Problema:** En una competencia, se tienen los puntajes de dos participantes. Determinar si el puntaje del primero es mayor que el del segundo.

**Ejercicio:**

- Crear dos variables `puntaje_jugador1` y `puntaje_jugador2` y asignarles los puntajes respectivos.
- Crear una expresión booleana utilizando operadores relacionales para determinar si el puntaje del primer jugador es mayor que el del segundo.
- Mostrar por consola el resultado de la comparación."""

puntaje_jugador1 = 18
puntaje_jugador2 = 20
puntaje_mayor = puntaje_jugador1 > puntaje_jugador2
print("El puntaje del primer jugado es mayor que el del segundo: ", puntaje_mayor)

"""
---

### PROBLEMA 2.
2. Cálculo de puntajes:

**Problema:**
Se tienen los puntajes de dos jugadores en tres concursos diferentes. En cada concurso, el puntaje de los jugadores se multiplica por un factor diferente (2 en el primer concurso, y 3 en el segundo). Se desea obtener los puntajes totales de ambos jugadores después de cada concurso y preguntar si ganó el jugador 1.

**Ejercicio:**
- Crear cuatro variables en total: `j1_concurso1`, `j2_concurso1`, `j1_concurso2`, `j2_concurso2`. Asignar a cada una los puntajes de los jugadores en cada concurso.
- Multiplicar los puntajes de los jugadores en cada concurso por el factor correspondiente.
- Calcular el puntaje de cada jugador después de cada concurso. El puntaje final de cada jugador se obtiene de la suma de sus puntajes en ambos concursos.
- Mostrar los puntajes de cada concurso y el puntaje final. Ejemplo:

```
Concurso 1
Jugador 1: 8 puntos
Jugador 2: 6 puntos

Concurso 2
Jugador 1: 12 puntos
Jugador 2: 15 puntos

Final
Jugador 1: 20 puntos
Jugador 2: 21 puntos
```

- Comparar los puntajes de los jugadores para determinar si ganó el jugador 1 o no.
- Mostrar el resultado de "Ganó el jugador 1:" por consola.
"""

# Primer concurso
j1_concurso1 = 4
j2_concurso1 = 3
print("Concurso 1")
print("Jugador 1: ", j1_concurso1)
print("Jugador 2: ", j2_concurso1)
print("")

# Segundo concurso
j1_concurso2 = j1_concurso1 * 2
j2_concurso2 = j2_concurso1 * 2
print("Concurso 2")
print("Jugador 1: ", j1_concurso2)
print("Jugador 2: ", j2_concurso2)
print("")

# Tercer concurso
j1_concurso3 = j1_concurso1 * 3
j2_concurso3 = j2_concurso1 * 3
print("Concurso 3")
print("Jugador 1: ", j1_concurso3)
print("Jugador 2: ", j2_concurso3)
print("")

# Puntajes finales
print("Final")
puntaje_jugador1 = j1_concurso1 + j1_concurso2 + j1_concurso3
puntaje_jugador2 = j2_concurso1 + j2_concurso2 + j2_concurso3
gano_primer_jugador = puntaje_jugador1 > puntaje_jugador2

print("Jugador 1: ", puntaje_jugador1)
print("Jugador 2: ", puntaje_jugador2)
print("")
print("Ganó el jugador 1: ", gano_primer_jugador)