# Fundamentos de programación

# 1era Semana
## Unidad #1 Introducción a los lenguajes de programación
Las computadoras hacen exactamente lo que nosotros les
pedimos, pero debemos darles instrucciones precisas.

Aquí entran los lenguajes de programación, estos nos 
ayudan a hablar con nuestra computadora.

Existen lenguajes compilados o interpretados.

Hay varios niveles de lenguaje
Lenguaje máquina (0 o 1, código objeto):
-Este es el lenguaje que entiende la computadora sin 
pasos previos.

Bajo nivel
-En estos tipos de lenguajes debemos dar instrucciones 
más específicas.
-Necesitamos conocer más sobre el hardware.

Alto nivel
-En estos tipos de lenguajes debemos dar instrucciones 
más fáciles de leer.
-Aquí la lógica es más importante que el hardware.
-Al ser intrucciones más fáciles de entender, es más
cercano al lenguaje natural.

### Lenguajes interpretado y compilados
En los lenguajes compilados, se traduce el código fuente
completamente a un código objeto que la computadora entiende
sin necesidad de traducir.

En las ventajas de compilar tenemos:
1. El ejecutable es independiente del compilador.
2. El programa suele ejecutarse más rápido.
3. No necesita del codigo fuente.

En los lenguajes interpretados, se traduce el código fuente
en tiempo real, esto con ayuda de un interpretador. Es decir
que para ejecutar el programa se necesita además del interpretador(traductor).

En las ventajas de interpretar tenemos:
1. Se puede ejecutar en diferentes plataformas fácilmente.
2. Se pueden encontrar errores más fácilmente (ejecución en tiempo real).

### Python
Python es muy popular debido a que es fácil 
de aprender, está entre los 20 lenguajes mejor pagados
y puede ser utilizado en distintas áreas.

Áreas donde se utiliza python
Principalmente están las áreas de análisis de datos
el área de aprendizaje máquina y también de desarrollo
web.

En fundamentos de programación usaremos python para:
- Realizar tareas sencillas en la computadora.
- Leer y **entender** programas sencillos.
- Organizar los pasos para resolver un problema.
- Aprender a crear programas sencillos.

Regresando a python, python es un lenguaje de programación
de alto nivel e interpretado. Sus archivos de texto son con
la extensión .py

## Unidad #2 Python
### Tipos de datos variables y conversiones
Los tipos de datos son cómo se guarda la infomación
contenida por una varibale en python. (la computadora lo entiende)
Los tipos de datos básicos son:
- numéricos (int-enteros)
- Reales (float-decimales)
- complejos (complex)


Otros tipos:
- lógicos (bool-True and False)
- Cadenas de caracteres o strings (str-strings)

### Variables
Las variables representan un lugar en la memoria (ram)
de la pc, la podríamos ver como una caja en la que
se puede guardar tipos de datos.

"Representan espacios en la memoria de la comuputadora, 
y, además permiten almacenar datos"

Sintaxis para definir variables en python
```Python
nombre_de_la_variable = tipo_de_dato
```
También podemos definir varias variables en una sola línea:
```Python
variable1, variable2, ..., variablen = valor1, valor2, ..., valorn # Respectivamente
<=> variable1 = valor1 and variable2 = valor2 and varibalen = valorn
```


### Conversiones de tipos de datos
Para convertir de un tipo de dato a otro
se sigue la siguiente sintaxis.

```Python
int(x)
float(x)
str(x)
complex(x)
bool(x)
```

Es decir que llamamos a la función con 
el nombre del tipo de dato y el argumento
será el dato que queramos convertir.


> [!NOTE]
> Para saber que tipo de dato está contenida en una variable usamos la función **type()**

### Operadores
Los operadores nos permiten realizar operaciones sencillas
con los datos, por lo tanto, estas operaciones dependen del
tipo de dato.

Los tipos de datos son:

**Aritméticos (Matemáticos)**

|Operador      |Símbolo       |
|--------------|--------------|
| Suma             |    +     |
| Resta            |    -     |
| Multiplicación   |    *     |
| División         | /        |
| División entera  | //       |
| Módulo o residuo | %        |
| Elevar al cuadrado          |     **   |

**Relacionales (Comparativos)** --> Te devuelve booleanos

|Operador      |Símbolo       |
|--------------|--------------|
| Mayor que            |    >     |
| Menor que          |    <     |
| Mayor o igual que   |    >=     |
| Menor o igual que         | <=       |
| Igual a  | ==       |
| Diferente a | !=        |

**Lógicos (Lógica matemática)**

|Operador      |Símbolo       |
|--------------|--------------|
| Conjunción (∧)             |    and     |
| Disyunción (v)           |    or     |
| Negación (¬)   |    not     |


Cabe recalcar que el resultado se guarda en la misma variable
Se puede decir que estos operadores sirven para
actualizar la información de la variable

**Operadores de acumulación**

|Operador      |Símbolo       |
|---------------|---------------|
| Suma             |    +=     |
| Resta            |    -=     |
| Multiplicación   |    *=     |
| División         |    /=     |


# 2da Semana
# Entradas y formatos de salida
Las computadoras están en la capacidad de interactuar con
los usuarios por medio de lo que el usuario le ordene.

"Entradas" se refiere a lo que puede ingresar el
usuario.

## Input (Entrada que recibe el programa)
Es una forma de interactuar en que el usuario ingresa datos
usando el teclado de la computadora.

Nosotros le hacemos saber por medio de un mensaje al usuario
que este ya puede ingresar datos.

> [!NOTE]
> Todo tipo de dato ingresado se retorna como un string

### Ejemplo
```Python
# Input espera primero la respuesta del usuario
nombre = input('Ingrese su nombre:')
print('¡Buenos días!', nombre)

año = input('Año de nacimiento: ')
año = int(año)
edad = 2020 - año
print('Adivinaré, en el 2020 tenías', edad, 'años')
```

## Formatos de salidas
lo que el programa arroja, lo que se ve en la pantalla
por ejemplo un **print()**

Nosotros sabemos que la función print() sirve para
imprimir datos en pantalla. Pero a esto le podemos
añadir un formateo en cuanto a cómo se ven los datos en
print().

### f-strings
Los f-strings sirve para darle formato a los datos, a 
diferencia de print()

los f-strings sirven para:
- Reservar espacios en pantalla.
- Alinear a la izquierda o derecha.
- Centrar.
- Redondear los decimales de un float.

**Sintaxis**
```Python
print(f'texto{variable:caracter_de_relleno>espacio.decimales_a_redondearf}')
```
- Se muestra la variable con {}
- Se puede reservar espacio con un entero **10**
- Se puede alinear con >,<,^
- Se puede rellenar con algpun caracter **$**

#### Secuencias de escape
Las secuencias de escape es otro tipo de visualizar
datos en un print()

- Salto de linea \n
```Python
print('Línea 1\nLínea 2')
```

- Mostrar comilla simple usando \'-\"
```Python
print('Libro \'El principito\' ')
```

- Mostrar caracter \\
```Python
print('Opcion 1 \\ Opcion 2')
```

## Cadenas de carácteres o str
El tipo de datos string es inmutable, es decir, no se
puede modificar. Se consideran un tipo de dato compuesto por
caracteres.

Estos se delimitan con:
- comillas simples ('')
- comillas dobles ("")
- triples comillas (""", ''') -> estos sirven para hacer
cadenas de varias lineas

### Operadores para Strings
- Para unir o **concatenar** (+)
- Multiplicar o repetir (*) --> Por un entero
- Igualdad en cadenas (==)
- Diferencia en cadenas (!=)
- Existe una cadena dentro de otra (in)
- No existe una cadena dentro de otra (not in)

#### Ejemplo
```Python
# Concatenar o unir cadenas
nombre = 'Ana'
apellido = " Vera"
nombre_completo = nombre + apellido
print(nombre_completo)

# Multiplicar cadenas
cadena = 'Python'
multiplicado = cadena * 3
print(multiplicado)

# Búsquedas con in y not in
frase = "Varias palabras en cualquier orden"
cadena = "palabra"
resultado = cadena in frase
print(resultado) # --> True
```

## indexación y rebanadas con str
Para aclarar conceptos:
- indexar: Obtener un elemento según su posición.
- Rebanada (slicing): Obtener un grupo de elementos.

Con esto podemos, por ejemplo, obtener cada elemento de una cadena 
de caracteres.

**Sintaxis:**
- Cadena[índice]
- Cadena[inicio:fin] -> rebanada
- Cadena[inicio:fin:salto] -> rebanada

**Sobre los índices:**
- Inician en 0.
- Se pueden usar positivos y negativos.
- Rebanadas desde **inicio** hasta **fin sin incluir**. --> [inicio, fin)
- Su "salto" predeterminado es 1.

## Funciones en cadenas
Ciertamente no podemos modificar cadenas de caracteres
pero podemos manipularlas de esta forma:

Recalcando que el resultado debe ser guardado en una varible
para poder usarlo.

Antes de esto, veamos ciertas funciones básicas que están 
relacionadas con los strings:

- len(x): devuelve la cantidad de caracteres que tiene x.
- min(x): devuelve el menor caracter, consideranto los caracteres en
orden alfabetico. Lo más cercano a "a" será menor.
- max(x): devuelve el caracter mayor.

**métodos:**
- .title(): convierte en mayúscula la primera letra de cada palabra de la cadena.

- .capitalize(): convierte en mayúscula la primera letra y el resto de la cadena en minúscula.

- .lower(): convierte a minúsculas todas las letras.

- .upper(): convierte a mayúsculas todas las letras.

- .replace(caracteres_anteriores, nuevos_caracteres): reemplaza todas las ocurrencias de la cadena anterior por la cadena nueva.

- .islower(): devuelve True si y solo si todas las letras de la cadena están en minúsculas.

- .isupper(): devuelve True si y solo si todas las letras de la cadena están en mayúsculas.

- .isalpha(): devuelve True si todos los caracteres de la cadena son letras.

- .isalnum(): devuelve True si los caracteres son letras o dígitos.

- .startswith(prefijo): devuelve True si la cadena inicia con el prefijo.

- .endsWith(sufijo): devuelve True si la cadena termina con el prefijo.

- .count(subcadena): cuenta cuantas veces se repite esta subcadena dentro de la cadena.

- .index(subcadena): devuelve el índice donde empieza la subcadena.

- .split(separador): con el separador se divine la cadena y se genera una **lista** de subcadenas. **.split(separador) ES ESTRICTO CON LA SUBCADENA QUE SEPARA LAS DEMÁS CADENAS**

- **"separador".join(palabras.split())** --> Listas

# 3era Semana
# Colección de datos list
## Listas
- Las listas son un tipo de colección de datos.
- Permiten almacenar un grupo de datos en una sola variable.

## Características
- Los datos se guardan en orden.
- Las listas son mutables (Se pueden modificar)
- Los elementos se colocan entre []
- Permite distintos tipos de datos.
- Es posible crear una lista vacia con list() o []

## Cómo actuan los operadores en las listas
- "+" Unir o concaternar.
- "*" Multiplicar o repetir un elemento (multiplicar por un entero).
- del: eliminar un elemento.
- in: existe elemento en.
- not in: no existe el elemento en.
- [índice] indexación
- [inicio:fin:salto] slicing/rebanadas
- lista[elemento_a_modificar] = dato_nuevo
- lista[::-1] se lee al revés la lista

## Operaciones con listas
Existen funciones en python que pueden ser usadas para diferentes
tipos de datos.
- **len(lista)**: Devuelve cuantos elementos hay en la lista.
- **min(lista)**: Devuelve el menor valor de la lista (Si y solo si son comparables).
- **max(lista)**: Devuelve el mayor valor de la lista (Si y solo si son comparables).
- **sum(lista)**: Suma todos los elementos de la lista.
- **list(range(a, b, salto))**: Genera una secuencia de números enteros en una lista ("[a,b)").
- **sorted(lista)**: Permite ordenar los elementos de la lista (De forma ascendente).

También hay funciones **propias de listas**:
- **.count(valor)**: Cuenta cuantas veces se repite un valor dentro de la lista.
- **.index(valor)**, donde_empieza_a_buscar): Devuelve el índice donde está el valor en la lista (si hay varios elementos repetidos, devuelve la primera ocurrencia).
- **.append(valor)**: Agrega un valor al final de la lista.
- **.insert(idx, valor)**: Agrega un valor (Más no elimina el anterior) a la lista en la posición indicada.
- **.remove(valor)**: Permite eliminar el valor de la lista.
- **.pop(index)**: Quitar un elemento de la lista por su posición.
               También "pop()" elimina y retorna el último elemento de la lista.



# Módulo random
Este módulo permite generar números aleatorios
en un rango específico.

- Se usa para juegos.
- Se usa para seguirdad, ...
 
## Importar el módulo random
```Python
import random
import random as rd
# Donde rd es una alias
```

## random con números
- random(): genera un decimal entre 0 y 1
- randint(inicio, final): genera un entero entre ese rango incluido
el límite final
- uniform(inicio, final): parecido a randint pero con número decimales
- **randrange(inicio, final)**: devuelve un número entero entre el rango
establecido, además de que no incluye el final. También se puede usar
de la siguiente forma "ranrange(inicio, final, salto)"

## random con listas
- choice(lista): retorna un elemento aleatorio
- choices(lista, k=n), retorna aleatoriamente n elementos de la lista
  y pueden haber repetidos.
- sample(lista, n): selecciona n datos distintos.
- shuffle(lista): No retorna nada y desordena la lista original.


# Funciones
las funciones son pequeños bloques de código (pequeñas rutinas o programas) que son 
reutilizables. Además las funciones tienen entradas o parámetros, también tienen salidas (retorno).

Son de diferentes tipos:
- Funciones de Python.
- Funciones dentro de un módulo de Python.
- Funciones definidas denntro del mismo programa.

## Importancia de las funciones
Es muy útil para solucionar un gran problema ya que podríamos considerar un conjunto funciones que solucionen cosas pequeñas de ese problema, y con esto llegar a resolver
el problema del todo. "La solución a un problema es equivalente a solucionar cada parte de este".

## Sintaxis de las funciones
Para definir funciones seguimos la siguiente sintaxis.
- Se usa la **Palabra reservada def** para **crear/definir** una función.
- Las funciones tienen que tener un nombre único y descriptivo.
- Los parámetros son las variables de entrada, separadas por comas, con los cuales
trabajará la función.

Luego de definir a la función viene el bloque de instrucciones:
- Se trata de las instrucciones que tendrá la función.
- Obviamente se utiliza sangría para diferenciar el bloque de instrucciones de la función (2 espacios).

Después de que la función haya realizado las intrucciones, llega el momento
en el que tendrá que dar la solución o el resultado. A eso se le llama retorno.
- Se usa la **palabra reservada return** para devolver valores de variables o datos, separados por coma, los cuales son el resultado de la función. El retorno predeterminado en una función
es el tipo de dato **none**. Aclarando que con la palabra return detenemos la función y el codigo
que está abajo de return no se ejecutará.
```Python
def nombre_unico_funcion(parametro1, parametro2, ..., parametron)
  bloque de instrucciones
  return solucion1, solucion2 # solucion = variable

# Para llamar a la función
resultado = nombre_unico_funcion(variable1, variable2, ..., variablen)
```

## Alcance de las funciones
Al momento de trabajar con una función, hay que tener claro que las variables
declaradas en el bloque de instrucciones son **locales**, es decir solo existen dentro
de la función.

En cambio, desde el programa principal no se puede acceder las variables de las funciones por lo ya explicado y las variables declaradas en el programa principal son llamadas variables **globales**.

Al momento de llamar a las funciones también podemos:
```Python
def nombre_unico_funcion(parametro1, parametro2, ..., parametron)
  bloque de instrucciones
  return solucion

# Para llamar a la función
resultado = nombre_unico_funcion(parametro1=valor, parametro2=valor, ..., parametron=valor)
```
Es decir, al momento de llamar a la función con sus respectivos parámetros, no hay necesidad
de que los parámetros sean variables.
Se pueden crear variables temporales para llamar a una función con n parámetros siempre y cuando el nombres de las variables sea el nombre de dichos parámetros.


### Parámetros con valor predeterminado
Al momento de definir a la función también podemos darles valor por defecto a los parámetros:
```Python
def nombre_unico_funcion(parametro1=valor1, parametro2=valor2, ..., parametron=valorn)
  bloque de instrucciones
  return solucion

# Para llamar a la función
resultado = nombre_unico_funcion()
```

# Estructuras de control
Hasta ahora, nosotros podemos hacer programas básicos, pedir
datos al usuario, concatenar, hacer operaciones básicas, etc...

Programas que se ejecutan una sola vez, además de que no hay comportamientos
diferentes según el contexto (Se ejecutan de forma lineal).

Las estructuras de control, justamente nos permiten tener mayor control
durante la ejecución de nuestro programa. De esta forma nosotros podemos 
hacer que nuestro programa tome desiciones establecidas (rutinas) dependiendo
de la condición. Así nuestro programa es más interactivo con el usuario.

## Condicionales
Son un tipo de estructura de control donde nosotros podemos, en algún punto 
del programa, hacer que el programa evalue condiciones para luego tomar
desiciones con el fin de elegir la siguiente ruta.

Con "condiciones a evaluar" nos referimos a verificar el tipo de dato
"True" o "False".

### Si...
Para las condicionales se usa la palabra reservada **if**. **if** nos permite
evaluar una condición (la cual retorna o verdadero o falso) y solo si el  resultado
es True, ejecuta el bloque de instrucciones.

### Si no se cumplió lo anterior, haz esto...
Ahora, ¿cómo controlar el código cuando la condición establecida en nuestro **if** 
es falsa y queremos seguir evaluando nuestro código? Para este tipo de casos tenemos
la palabra reservada **elif**. **elif** permite evaluar otra condición cuando la anterior 
condición evaluada fue falsa (elif establece una nueva ruta).

### Si ninguna se cumplió, haz esto... (Caso contrario)
¿Y si al final no se cumplió ninguna condición? Entonces usamos la palabra reservada **else**.
**else** se ejecuta si ninguna de las anteriores condiciones se cumplieron. Pero en este caso
else no permite evaluar condiciones y puede usarse **solo una vez**.

Su sintaxis general es:
```python
# Programa principal
# Instrucciones
if condicion:
  # Con sangría
  Bloque de instrucciones
  IntrucciónM

elif condicion:
  # Con sangría
  Bloque de instrucciones
  IntrucciónM

else:
  # Caso contrario
  # Con sangría
  Bloque de instrucciones
  IntrucciónM
```

# Estructuras de control repetitivas
Hay diferentes tipos de estructura de control; las condicionales
que ya hemos visto pero además están las repetitivas (lazos (loops), bucles).
bucle for o ciclo for

Entre estas estructuras de control repetitivas están el lazo for y
el lazo while

## Lazo for
El lazo for permite recorrer/iterar en una secuencia 
de elementos y en ese elemento de los que recorremos podemos
ejecutar un bloque de código. De esta manera se ejecutará un mismo
bloque de código por cada iteración del lazo for.

-El lazo for permite repetir un bloque de código **un número
conocido** de veces y con esto recorrer o iterar una secuencia (listas, strings, ...).

-Un buen uso de range(n) es, justamente para for, en cuanto 
a el número de veces que se va a repetir el código. (secuencia)

-La cantidad de repeticiones está determinada por el número
de elementos de la secuencia.


Su sintaxis es:
```Python
for iterador in secuencia: # Palabras reservadas
  # "iterador" es una variable temporal
  # code
```

- Aclarando que el iterador tendrá cada valor en función al valor
actual de la iteración en la secuencia.

### Ejemplo for-each
```Python
lista = [3, 6, 12, 9, 1] # Definiendo una lista
total = 0

for elemento in lista:
  total += elemento
  print(total)

# Primera iteración elemento = 3 --> total += 3
# Segunda iteración elemento = 6 --> total += 6
# Segunda iteración elemento = 12 --> total += 12
# ...


promedio = total / len(secuencia)
print(f'El promedio es {promedio}')
```
