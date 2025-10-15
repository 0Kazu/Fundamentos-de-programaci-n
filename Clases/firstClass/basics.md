# Fundamentos de programación

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
contenida por una varibale en python.
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
| Residuo          |     **   |

**Relacionales (Comparativos)**

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


# Entradas y formatos de salida
Las computadoras están en la capacidad interactuar con
los usuarios por medio de lo que el usuario le ordene.

"Entradas" se refiere a lo que puede ingresar el
usuario.

## Input (Entrada que recibe el programa)
Es una forma de interactuar en que el usuario ingresa datos
usando el teclado de la computadora.

Nosotros le hacemos saber por medio de un mensaje al usuario
que este ya puede ingresar datos.

> [!NOTE]
> Todo tipo de dato ingresado es string

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
print(f'texto{variable:caracter_de_relleno>espacio.decimales_a_redondear}')
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
- Multiplicar o repetir (*)
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
print(resultado)
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
- Rebanadas desde **inicio** hasta **fin sin incluir**.
- Su "salto" predeterminado es 1.

## Operaciones con cadenas
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
- .title(): convierte en mayúscula la primera letra de 
cada palabra de la cadena.

- .capitalize(): convierte en mayúscula la primera letra y el resto
de la cadena en minúscula.

- .lower(): convierte a minúsculas todas las letras.

- .upper(): convierte a mayúsculas todas las letras.

- .replace(caracteres_anteriores, nuevos_caracteres): reemplaza todas las ocurrencias de la 
cadena anterior por la cadena nueva.

- .islower(): devuelve True si y solo si todas las letras 
de la cadena están en minúsculas.

- .isupper(): devuelve True si y solo si todas las letras
de la cadena están en mayúsculas.

- .isalpha(): devuelve True si todos los caracteres de la cadena
son letras.

- .isalnum(): devuelve True si los caracteres son letras o dígitos.

- .startswith(prefijo): devuelve True si la cadena inicia con el prefijo.

- .endsWith(sufijo): devuelve True si la cadena termina con el prefijo.

- .count(subcadena): cuenta cuantas veces se repite esta subcadena dentro de la cadena.

- .index(subcadena): devuelve el índice donde empieza la subcadena.

- .split(separador): con el separador se divine la cadena y se genera una **lista** 
de subcadenas.

# Colección de datos list
## Listas
- Las listas son un tipo de colección de datos.
- Permiten almacenar un grupo de datos en una sola variable.

### Características
- Los datos se guardan en orden.
- Las listas son mutables (Se pueden modificar)
- Los elementos se colocan entre []
- Permite distintos tipos de datos.
- Es posible crear una lista vacia con list() o []

### Cómo actuan los operadores en las listas
- "+" Unir o concaternar.
- "*" Multiplicar o repetir un elemento (multiplicar por un entero).
- del: eliminar un elemento.
- in: existe elemento en.
- not in: no existe el elemento en.
- [índice] indexación
- [inicio:fin:salto] slicing/rebanadas
- lista[elemento_a_modificar] = dato_nuevo
- lista[::-1] se lee al revés la lista


## Módulo random
Este módulo permite generar números aleatorios
en un rango específico.

- Se usa para juegos.
- Se usa para seguirdad, ...
 
### Importar el módulo random
```Python
import random
import random as rd
# Donde rd es una alias
```

### random con números
- random(): genera un decimal entre 0 y 1
- ranint(inicio, final): genera un entero entre ese rango incluido
el límite final
- uniform(inicio, final): parecido a ranint pero con número decimales
- **randrange(inicio, final)**: devuelve un número entero entre el rango
establecido, además de que no incluye el final. También se puede usar
de la siguiente forma "ranrange(inicio, final, salto)

### random con listas
- choice(lista): selecciona un elemento aleatorio
- choices(lista, k=n), selecciona aleatoriamente n elementos de la lista
  y pueden haber repetidos.
- sample(lista, n): selecciona n datos distintos.
- shuffle(lista): No retorna nada y desordena la lista original.





