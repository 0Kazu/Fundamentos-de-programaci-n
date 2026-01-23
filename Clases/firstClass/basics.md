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

# 4ta semana
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

# Estructuras de control condicionales
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

# 5ta semana
# Estructuras de control repetitivas
Hay diferentes tipos de estructura de control; las condicionales
que ya hemos visto pero además están las repetitivas (lazos (loops), bucles).
bucle for o ciclo for

Entre estas estructuras de control repetitivas están el lazo for y
el lazo while

## Loop for (Lazo for)
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

## Bucle While
Mientras que en el loop for el bloque de código se repetía por cada elemento que se haya
iterado en una lista, en el bucle while el bloque código se repite si se sigue cumpliendo
cierta condición establecida.

While sólo se repite si y sólo si la condición establecida es verdadera, cuando la condición
deje de ser verdadera el bucle se detiende. De esta forma, si no se establece una condición 
válida (sea verdadera siempre) puede hacer que el bucle nunca se detenga.

Para ejecutar un bucle se usa la palabra reservada **while** seguido de la condición que
se vaya a validar.

Su sintaxis es:

```Python
while condicion:
  instruccion1...
  instruccion2...
  ...
  instruccionm...
```

Puesto que se trata de un bucle podemos usar **contadores** y **acumuladores**. 
Pero, ¿De qué se tratan los contadores y acumuladores?
- contadores: variables que se usan para contar cada iteración en el bucle ("Simplemente es en qué número de iteración estamos")
- acumuladores: variables que se usan con el fin de acumular valores en cada iteración ("Sumar valores con datos obtenidos en cada iteración")

Como se mencionó anteriormente, debemos establecer condiciones que siempre sean válidas. Esto es, no crear bucles infinitos
ya que, el hecho de tener un bucle infinito implica que nuestro programa nunca se detenga.

### Ejemplo de programa con While:
```Python
n = int(input("¿Cuántas facturas tiene? "))
facturas = [] # Contador

while len(facturas) < n:
  valor = float(input(f'Factura: $'))
  facturas.append(valor)

total = sum(facturas)
print(f'El total es: ${total}')
```


## Profundizando sobre contadores y acumuladores
### Contadores
Como se mencionó anteriormente, en un bucle es necesario guardar, 
de alguna forma, el número de iteración en la que estamos. Normalmente
los contadores son variables con tipos de datos numéricos enteros.

Al ser un contador, este inicia o en 0 o en 1. Además, es usual que incremente
su valor de 1 en 1.

### Acumuladores
Los acumuladores son variables que nos permiten almacenar valores importantes
que dependan de cierto incremento. Usualmente es de tipo entero pero podría ser
de cualquier otro tipo.

```Python
print('Ingrese sus facturas o cero para salir')
facturas = []

acumulador = 0

valor = -1

contador = 1

while valor != 0:
  valor = float(input(f'Factura {contador} $:'))
  if valor != 0:
    contador += 1
    acumulador += valor

print(f'Total: ${}')
```

# 6ta semana
# Estructuras de control anidadas
Al mezclar estructuras (anidar una condicional, un bucle, ...) podemos
resolver un problema complejo de forma más efectiva.

Para el efecto, basta con mostrar un ejemplo:

### Ejemplo con if anidado en un for
```Python
n = int(input('Ingrese un número: '))

divisores = []

for i in range(1, n + 1):  # [1, 2, 3, ..., n]
    if n % i == 0:
        divisores.append(i)
        # tenemos un if (estructura de control) anidada en un for (otra estructura de control)

if len(divisores) == 2:
    print(f'{n} es primo')
else:
    print(f'{n} NO es primo')
    print(f'Divisores: {divisores}')
```

## Ejemplo de doble lazo o doble bucle
```Python
import random as rd

primos = []

while len(primos) < 3:
    n = rd.randint(10, 100)
    print(n, end=', ')

    # Buscar divisores
    if n not in primos:
        divisores = []
        for i in range(1, n + 1):  # Buscar divisores
            if n % i == 0:
                divisores.append(i)

        if len(divisores) == 2:  # Si es primo
            primos.append(n)

print(f'\nNúmeros primos aleatorios:{primos}')
```

Por cierto "end=''" es un parámetro de la función print
el cual permite modificar la salida del print. Por ejemplo:
```Python
print(n) <=> print(n, end='\n')
```
Con "end=', '" simplemente hacemos que "no salte a otra línea"
```Python
print(n, end=', ') # salida: 0, 1, 2, (en caso de for con 3 iteraciones)
```


# 7ma semana
# Colecciones de datos 
## Diccionarios
Este es otro tipo de dato en el cuál podemos guardar aún más datos, es
parecido a las listas pero en este accedemos a los elementos mediante 
la relación clave-valor.

### Sobre los diccionarios:
- Se identifica con llaves {}
- Los elementos NO se guardan en un orden específico (a diferencia de las listas).
- Se puede crear un diccionario vacío con {} o con dict().
- Los diccionarios, como las listas, son mutables.

Su sintaxis es:
```Python
diccionario = {clave1:valor1,
              clave2:valor2,
              claven:valorn}
```

Por cierto, las claves solo pueden ser de tipo int, string o bool.
Mientras que los valores pueden ser datos cualesquiera.

Por lo tanto, nosotros podemos acceder a estos datos
mediante su clave (De esta forma accedemos a su valor)

Ahora, ¿Cómo puedo añadir valores a un diccionario?
Suponga que desea añadir un valor nuevo (diferente a los anteriores)
```Python
diccionario_vacio = dict()

# Para añadir un nuevo valor al diccionario
diccionario_vacio['clave1'] = valor1

# Para acceder a un valor del diccionario
print(diccionario_vacio['clave1']) -> retorna el valor
...
# Con esto añadimos valores nuevos a un diccionario
```

Luego, ¿Cómo puedo eliminar valores?
Hay 2 formas de eliminar valores en un diccionario:
- **del nombre_diccionario[clave]**
- **nombre_diccionario.pop(clave)** -> pop devuelve sólo el valor (no clave).

Algo importante a tomar en cuenta es que, si consultamos un valor
con una clave que no exista en el diccionario, el programa se detendrá
y retornará un error.

Para esto justamente están las funciones:
- **nombre_diccionario.get(clave, predeterminado)**, la cual:
  - Si existe la clave: retorna el valor asociado.
  - No existe la clave: retorna de valor "predeterminado".

- **nombre_diccionario.setdefault(clave, predeterminado)**, la cual: -> modifica el diccionario
  - Si existe la clave: retorna el valor asociado.
  - No existe la clave: inserta la clave con el valor de "predeterminado"
    y luego, retorna el valor "predeterminado".

### Funciones de diccionarios
- **len(diccionario)**: Retorna la cantidad de elementos del diccionario.

- **max(diccionario) or min(diccionario)**: Retorna el valor máximo o mínimo de los
  diccionarios.

- **nombre_diccionario.keys()**: Retorna una pseudo-lista con todas las claves del diccionario.

Por cierto **pseudo-lista** es parecido al tipo de dato lista, más no lo es al 100%.

- **nombre_diccionario.values()**: Retorna una pseudo-lista con todos los valores del diccionario.

- **nombre_diccionario.items()**: Retorna una pseudo-lista de pares ordenados (clave, valor).

Pero, ¿Cómo podemos recorrer diccionarios?
De la siguiente forma:
- **for clave in diccionario.keys()**: Recorrer las claves de un diccionario.

- **for valor in diccionario.values()**: Recorrer los valores de un diccionario.

- **for clave, valor in diccionario.items()**: Recorrer clave-valor. -> Forma recomendada
  para recorrer diccionarios.

# 8va semana
# Arreglos (Numpy)
Durante esta unidad estudiaremos la librería Numpy, librería que se especializa
en números, pero esta trabaja con **arreglos** de una o más dimensiones.

Aclarando que la librería no fue escrita en python por lo que, sus operaciones
están optimizadas a bajo nivel (C).

Esta librería se caracteriza porque al momento de guardar sus datos, es
lo más exacto posible (para guardar recursos en la memoria lo más posible). Con
esto tenemos una optimización y rapidez.

Esta librería trae funciones del tipo:
- Aritméticas.
- Estadísticas.
- Lógicas.
- De ordenamiento.
- Entre otras.

Pero, **¿Qué son los arreglos?**
Los arreglos son similares a las listas de python, es decir
son colecciones de datos (parecidas a los vectores) pero estos
solo pueden guardar datos de un mismo tipo (Datos homogéneos)

Sobre los tipos de datos que se pueden guardar en un arreglo
tenemos:
- Enteros: int64
- Reales o flotantes: float64
- Lógicos: Bool
- Cadenas de caracteres (>u11, <u11)

Si has estudiado álgebra lineal, el concepto de dimensión para los arreglos
se te hará familiar:
- 1 Dimensión: Vectores, lineales.
- 2 Dimensiones: Matrices (con filas y columnas).
- 3 Dimensiones, 4...

Para importar esta librería en python, hacemos lo siguiente:
```Python
import numpy as np
```

Ahora, para crear un arreglo de una dimensión (un vector), tenemos la siguiente función:
```Python
import numpy as np

lista_vector = [dato1, dato2, ..., daton]

arreglo = np.array([dato1, dato2, ..., daton])
arreglo = np.array(lista_vector)

print(arreglo)
# Output
# [dato1, dato2, ..., daton] -> vector (una dimensiones)
```
Observe que el parámetro de np.array() es una lista (nunca diccionarios). Como se menciono antes
los arreglos son datos homogéneos por lo que si en la lista hay datos heterogéneos
estos automáticamente, en el arreglo, se hacen de un mismo tipo de dato (o sólo int, o sólo string, ...)

En cuanto a la función np.array() de numpy, su sintaxis es la siguiente:
- ```Python
  arreglo = np.array(datos, tipo_de_dato)
  ```
  De donde:
  - datos: listas (no diccionarios) que contengan los datos para el arreglo.
  - tipo_de_dato: el tipo de dato que numpy convertirá a toda la lista de tal forma que sean homogéneos.

Para crear un arreglo bidimensional hacemos lo siguiente:
```Python
import numpy as np

arreglo = np.array([ [dato1, dato2, ..., daton], [dato1, dato2, ..., daton] ])
arreglo = np.array([ vector1, vector2 ])

print(arreglo)
# Output
# [ [dato1, dato2, ..., daton]
#   [dato1, dato2, ..., daton] ]
```
Es decir, por cada lista anidada dentro de una lista (la general), tendremos una dimensión más. Observe que cada lista, es decir, cada *[dato1, dato2, ..., daton]* representa un vector unidimensional. De esta forma
- Considere *[]* la lista general. Entonces:
  - [dato1, ..., daton] -> vector de 1 dimensión.
  - [ [dato1, ..., daton], [dato1, ..., daton] ] -> vector de 2 dimensiones.
  - [ [ [dato1, ..., daton], [dato1, ..., daton] ] ] -> vector de 3 dimensiones.

De esta forma, un arreglo no puede tener valores simples y vectores al mismo tiempo. Por ejemplo, el siguiente código retornaría error.
```Python
import numpy as np

arr = np.array([ [1,2], [[1,2]] ])

print(arr.ndim)
print(arr)
```

## Atributos de los arreglos (Propiedades)
Suponga que existe un arreglo arr, este contará con las
siguientes propiedades:
- arr.size:
  - Cantidad de elementos en el arreglo.
  - Retorna un entero.
  - En cuanto a una dimensión:
    ```Python
    import numpy as np

    datos = ["dato1", "dato2", "dato3", "dato4"]

    vector = np.array(datos)

    print(vector.size)

    # Output:
    # 4
    ```
  
  - En cuanto a 2 dimensiones:
    ```Python
    import numpy as np

    datos1 = ["dato1", "dato2", "dato3", "dato4"]
    datos2 = ["dato5", "dato6", "dato7", "dato8"]

    vector = np.array([datos1, datos2])

    print(vector.size)

    # Output
    # 8
    ```


- arr.ndim:
  - Cantidad de ejes del array.
  - o también, es el número de vectores que contiene el arreglo.
  - Retorna un entero.
  - En cuanto a una dimensión:
    ```Python
    import numpy as np

    datos = ["dato1", "dato2", "dato3", "dato4"]

    vector = np.array(datos)

    print(vector.ndim)

    # Output
    # 1
    ```
  - En cuanto a 2 dimensiones:
    ```Python
    import numpy as np

    datos1 = ["dato1", "dato2", "dato3", "dato4"]
    datos2 = ["dato5", "dato6", "dato7", "dato8"]

    vector = np.array([datos1, datos2])

    print(vector.ndim)

    # Output
    # 2
    ```
  
- arr.shape:
  - Retorna una tupla.
  - Número de elementos por cada vector (a cada vector le hace .size).
  - Indica cuantos elementos tiene el arreglo por cada una
  de sus dimensiones o ejes, por medio de una tupla.
  - En cuanto a una dimensión:
    ```Python
    import numpy as np

    datos = ["dato1", "dato2", "dato3", "dato4"]

    vector = np.array(datos)
    print(vector.shape)


    # Output
    # (4,)
    ```

  - En cuanto a dos dimensiones:
    ```Python
    import numpy as np

    datos1 = ["dato1", "dato2", "dato3", "dato4"]
    datos2 = ["dato1", "dato2", "dato3", "dato4"]

    vector = np.array([datos1, datos2])
    print(vector.shape)

    # Output
    # (2,4) -> similar a matriz Amn, m filas, n columnas
    ```
  

- arr.dtype:
  - Muestra el tipo de dato de los elementos del arreglo.
  - Ejemplo general:
    ```Python
    import numpy as np

    datos1 = ["dato1", "dato2", "dato3", "dato4"]
    datos2 = ["dato1", "dato2", "dato3", "dato4"]

    vector = np.array([datos1, datos2])
    print(vector.dtype)

    # Output
    # <U5
    ```

## Ejemplo general
```Python
import numpy as np

arr1D = np.array([2, 4, 1, 8, 7, 0])
arr2D = np.array( [ [3, 1, 1, 7], 
                  [1, 1, 0, 2],
                  [0, 3, 0, 2] ])

print(arr2D)

# Cantidad de elementos en los arrays
print(arr1D.size) # Output: 6
print(arr2D.size) # Output: 12

# Ejes o índices en los arrays
print(arr1D.ndim) # Output: 1
print(arr2D.ndim) # Output: 2 (solo cuenta con filas y columnas)

# Cantidad de elementos por ejes
print(arr1D.shape) # Output: (6,) -> En el primer eje tengo 6 elementos (izq a derecha)
print(arr2D.shape) # Output: (3, 4) - > De arriba hacia abajo, luego de izquierda a derecha.

# Tipos de datos en los arrays
print(arr1D.dtype) # Output: int64
print(arr2D.dtype) # Output: int64
```

## Funciones para creación de arreglos en numpy
Para definir arreglos, además de la forma tradicional, tenemos las siguientes funciones:
### Funciones que transforman datos a arreglos (Transformadoras):
- **np.array(datos, tipo_de_dato)**: Crea un arreglo a partir de una lista **datos**.
 - Tipos de datos disponibles (Van "en seco" de esa forma):
  - str
  - int
  - bool
  - float

### Funciones que generan un arreglo desde 0 (Generadoras):
#### Lineales o no
- **np.ones(arr.shape, tipo_de_dato)**: Crea un arreglo "de unos" del arr.shape indicado con el tipo_de_dato indicado.
- **np.zeros(arr.shape, tipo_de_dato)**: Crea un arreglo "lleno de ceros" del arr.shape indicado con el tipo_de_dato indicado.
- **np.full(arr.shape, valor, tipo_de_dato)**: Crea un arreglo relleno de "valor"  del tamaño arr.shape con su respectivo tipo_de_dato.

#### Sólo lineales
- **np.arange(inicio, final, salto, tipo_de_dato)**: Crea un *arreglo unidimensional* con la secuencia indicada **(el final no se incluye)**.
- **np.linspace(inicio, final, tamaño, tipo_de_dato)**: Crea una secuencia de elementos distribuidos uniformemente y del tamaño indicado. Es decir si queremos una secuencia solo con un vector de tamaño n, habrán n elemenos en el vector  **(el final sí se incluye)**.

## Acceder a los elemenos de los vectores
Ahora que ya sabemos cómo crear los vectores, procederemos a ver cómo acceder a cada elemento de éste.

### Generalización de indexación en vectores
Así como podemos acceder a los elementos en la listas, de igual forma
podemos hacerlo con los arreglos o vectores:

- Su índice empieza desde 0 (similar a una lista).
- Se pueden usar índices positivos o negativos.
- Permiten acceder a un elemento específico dentro del arreglo.
- Accedemos (y agregamos) a un valor por medio de: 
  - **arr[índice] = valor**
  - **arr[arr.size - 1] = valor_nuevo**
  - Cabe recalar que sólo se pueden modificar índices existentes.
- Es posible hacer uso del slicing.
- Es posible modificar elementos con el slicing.

### Una dimensión
En cuanto a vectores de 1 Dimensión tenemos la siguiente sintaxis:
Su sintaxis es similar a acceder a un elemento a una lista, es decir:
```Python
arreglo[índice]
```

Por ejemplo:

```Python
import numpy as np

arreglo = np.array([dato1, ..., daton])

print(arreglo[0]) # Output: dato1
```

### Dos dimensiones
En cuanto a vectores de 2 dimensiones tenemos la siguiente sintaxis:
```Python
arreglo[fila, columna]
```
Cabe recalcar que, las filas comienzan de 0. Es decir:
```Python
[1 0 0] # Fila 0
[2 3 1] # Fila 1
[3 1 0] # Fila 2
```

Por ejemplo:

```Python
import numpy as np

arreglo = np.array([ [dato1, ..., daton], [datito1, ..., datiton] ])

print(arreglo[1,n-1]) # Output: daton
print(arreglo[1]) # Output [datito1, ..., datiton]
```

## Operaciones entre vectores
Así como están definidas las operaciones entre vectores, en Numpy podemos
realizar operaciones entre arreglos:

Pero antes, note que al ser "operaciones entre vectores" estas deben cumplir la
condición de ser del mismo arr.shape (No exactamente como vectores en matemáticas)
También, estas operaciones se ejecutan elemento a elemento (No hay necesidad de bucles).

### Operaciones normales
Veamos algunos ejemplos:
- **Vectores "iguales"**
  ```Python
  import numpy as np

  parcial_1 = np.array([8, 9, 7])
  parcial_2 = np.array([9, 10, 6])

  nota_final = parcial_1 + parcial_2

  print(nota_final)
  # Resultado: [17 19 13]
  # (8+9, 9+10, 7+6)
  ```

- **Operaciones con escalares**
  ```Python
  vector = np.array([10, 20, 30])

  # Restar 5 a todos (como si fuera un vector [5, 5, 5])
  # Lo transforma al vector [5 5 5]
  resultado = vector - 5

  print(resultado)
  # Resultado: [ 5 15 25 ]
  ```

- **Matrices entre vectores**
  ```Python
  matriz = np.array([
      [1, 1, 1],  # Fila 1
      [2, 2, 2]   # Fila 2
  ])

  vector = np.array([10, 20, 30])

  # Suma: El vector se suma a la Fila 1 Y TAMBIÉN a la Fila 2
  suma = matriz + vector
  # Es decir
  # Lo transforma a la matriz [10, 20, 30]
  #                           [10, 20, 30]

  print(suma)
  # Resultado:
  # [[11 21 31]   <- (1+10, 1+20, 1+30)
  #  [12 22 32]]  <- (2+10, 2+20, 2+30)
  ```

### Operaciones lógicas
Considere los siguientes ejemplos:
  ```Python
  import numpy as np

  alumnos = np.array(["Sebas", "Samuel", "María", "Juan"])
  notas   = np.array([     10,          8,        9,      4])

  pasaron = notas >= 7  
  print(pasaron)
  # Output: [True True True False]

  # Modo máscara
  # notas_aprobadas = [10 8 9 4][[True True True False]]
  # Note que estamos indexando a notas en pasaron. Cuando i[índice] no es un 
  # índice y es un booleano, se cambia a modo máscara. De donde se creará un
  # nuevo arreglo [10 8 9]
  notas_aprobadas = notas[pasaron]
  print(notas_aprobadas)
  # Output: [10  8  9]

  nombres_pasaron = alumnos[pasaron]
  print(nombres_pasaron)
  # Output: ['Sebas' 'Samuel' 'María']

  nombres_reprobados = alumnos[~pasaron] #-> negación
  print(nombres_reprobados)
  # Output: ['Juan']
  ```

## Funciones de los arreglos
- **arr.astype(dtype)**: permite modificar el tipo de dato que almacena el arreglo arr.
- **arr.tolist()**: permite convertir el arreglo en una lista (cada dimensión sera una lista).
- **arr.prod(arr)**: permite multiplicar los elementos del arreglo entre sí.
- **numpy.round(arr,n)**: redondea los elementos de a con n decimales.
- **np.sum(arr)**: Suma los elementos del arreglo arr.
- **np.mean(arr)** and **np.average(arr)**: Promedia los elementos del arreglo arr.
- **np.max(arr)**: valor máximo de arr.
- **np.min(arr)**: valor mínimo de arr.
- **np.argmax(arr)**: El índice del mayor valor de arr.
- **np.argmin(arr)**: El índice del menor valor de arr. 
- **np.sort(arr)**: Genera un nuevo arreglo ordenado ascendentemente, con los elementos de arr.
- **arr.sort()**: Ordena internamente **(No retorna nada)** los elementos de a en forma ascendente sin retornar valor alguno.
- **np.argsort(arr)**: Devuelve un arreglo con los índices de ordenamiento para el arreglo arr.

## Numpy con random
Al importar numpy también importamos np.random el cual nos permite generar
arrays enteros al instante (matrices, vectores, ...)
```Python
import numpy as np

arr_temperaturas = np.random.randint(22, 39, size=7)
```

# 9na semana
# Introducción al procesamiento de datos (librería pandas)
Ahora que ya sabemos cómo guardar datos de forma eficiente procederemos a manipularlos para su respectivo análisis.

Es oportuno mencionar que la librería pandas prácticamente está construida sobre numpy.

Para importar esta librería:
```Python
import pandas as pd
```
Se introducirá sobre estructuras de datos en Pandas.

## Estructura de datos
Es una forma de organizar datos para ser utilizados eficientemente. Esta maravillosa
librería ofrece 2 tipos de estructuras de datos: **Series** y **Dataframes**.

### Series
Estructuras unidimensionales que pueden crearse a partir de listas o diccionarios. Cada
elemento de la serie tiene un índice asociado.

```Python
import pandas as pd
 
serie = pd.Series(data, index=index)
```

- El parámetro **data** corresponde a los datos de la serie (listas homogéneas o heterogéneas, no es como numpy).
- El parámetro **index** corresponde a los índices que se emplearán en la serie.

#### Asociar un nombre a la serie
Para asociar un nombre a esta serie podemos:
```Python
import pandas as pd
 
serie = pd.Series(data, index=index)

serie.name = 'Nombre_de_la_serie'
```
#### Ejemplo general de serie
Considere el siguiente ejemplo:
```Python
import pandas as pd

powerPlants = pd.Series([
    'Coca Codo Sinclair',
    'C.H. Molino',
    'Sopladora',
    'C.H. Minas San Francisco',
    'C.T. Ing. Gonzalo Cevallos',
    'Termogas Machala',
    'Termoeléctrica Quevedo',
    'Termoeléctrica Santa Elena',
    'C.H. Manta'
]) # Por defecto es un índice numérico

print(f"Plantas Generadoras de Electricidad:\n{powerPlants}")
# o también...
print("Plantas Generadoras de Electricidad:\n%s" % powerPlants)

# Output
"""
Plantas Generadoras de Electricidad:
0            Coca Codo Sinclair
1                   C.H. Molino
2                     Sopladora
3      C.H. Minas San Francisco
4    C.T. Ing. Gonzalo Cevallos
5              Termogas Machala
6        Termoeléctrica Quevedo
7    Termoeléctrica Santa Elena
8                    C.H. Manta
dtype: object
"""
# Note que se imprime tanto el índice como el valor asociado. Luego el tipo de arreglo
```
#### Slicing en series
En las series es posible hacer slicing. Para el efecto, considere el siguiente ejemplo:
```Python
import pandas as pd

powerPlants = pd.Series([
    'Coca Codo Sinclair',
    'C.H. Molino',
    'Sopladora',
    'C.H. Minas San Francisco',
    'C.T. Ing. Gonzalo Cevallos',
    'Termogas Machala',
    'Termoeléctrica Quevedo',
    'Termoeléctrica Santa Elena',
    'C.H. Manta'
])

print(powerPlants[0:3])
# Output
"""
Plantas Generadoras de Electricidad:
0            Coca Codo Sinclair
1                   C.H. Molino
2                     Sopladora
dtype: object
"""
```

Además podemos agregar datos de la misma forma que en diccionarios. Por medio de su índice:

```Python
import pandas as pd

powerPlants = pd.Series([
    'Coca Codo Sinclair',
    'C.H. Molino',
    'Sopladora',
    'C.H. Minas San Francisco',
    'C.T. Ing. Gonzalo Cevallos',
    'Termogas Machala',
    'Termoeléctrica Quevedo',
    'Termoeléctrica Santa Elena',
    'C.H. Manta'
])

powerPlants[powerPlants.size] = "Nueva hidroeléctrica"
print(powerPlants)
# Output
"""
Plantas Generadoras de Electricidad:
0            Coca Codo Sinclair
1                   C.H. Molino
2                     Sopladora
3      C.H. Minas San Francisco
4    C.T. Ing. Gonzalo Cevallos
5              Termogas Machala
6        Termoeléctrica Quevedo
7    Termoeléctrica Santa Elena
8                    C.H. Manta
9          Nueva hidroeléctrica
dtype: object
"""
```

En caso de querer guadar una copia con datos elimnados dentro de la serie, hacemos uso del método **drop()**.
Aunque este método no modifica a la serie original, lo que hace es crear una copia de esta pero sin el índice que hayamos solicitado eliminar.

```Python
import pandas as pd

powerPlants = pd.Series([
    'Coca Codo Sinclair',
    'C.H. Molino',
    'Sopladora',
    'C.H. Minas San Francisco',
    'C.T. Ing. Gonzalo Cevallos',
    'Termogas Machala',
    'Termoeléctrica Quevedo',
    'Termoeléctrica Santa Elena',
    'C.H. Manta',
    'Nueva hidroeléctrica'
])

índice_eliminado_serie = powerPlants.drop(7)

# Output
"""
Plantas Generadoras de Electricidad:
0            Coca Codo Sinclair
1                   C.H. Molino
2                     Sopladora
3      C.H. Minas San Francisco
4    C.T. Ing. Gonzalo Cevallos
5              Termogas Machala
6        Termoeléctrica Quevedo
8                    C.H. Manta
9          Nueva hidroeléctrica
dtype: object
"""
```

Este método también es muy útil para eliminar un grupo de elementos (índices):
```Python
import pandas as pd

powerPlants = pd.Series([
    'Coca Codo Sinclair',
    'C.H. Molino',
    'Sopladora',
    'C.H. Minas San Francisco',
    'C.T. Ing. Gonzalo Cevallos',
    'Termogas Machala',
    'Termoeléctrica Quevedo',
    'Termoeléctrica Santa Elena',
    'C.H. Manta',
    'Nueva hidroeléctrica'
])

nueva_serie = powerPlants.drop(powerPlants.index[0:2])


# Output
"""
Plantas Generadoras de Electricidad:
2                     Sopladora
3      C.H. Minas San Francisco
4    C.T. Ing. Gonzalo Cevallos
5              Termogas Machala
6        Termoeléctrica Quevedo
8                    C.H. Manta
9          Nueva hidroeléctrica
dtype: object
"""
```

Aún así, si desea eliminar elementos en la serie original y no una copia, puede:
```Python
import pandas as pd

powerPlants = pd.Series([
    'Coca Codo Sinclair',
    'C.H. Molino',
    'Sopladora',
    'C.H. Minas San Francisco',
    'C.T. Ing. Gonzalo Cevallos',
    'Termogas Machala',
    'Termoeléctrica Quevedo',
    'Termoeléctrica Santa Elena',
    'C.H. Manta',
    'Nueva hidroeléctrica'
])

del(powerPlants[8])
print(powerPlants)

# Output
"""
Plantas Generadoras de Electricidad:
0            Coca Codo Sinclair
1                   C.H. Molino
2                     Sopladora
3      C.H. Minas San Francisco
4    C.T. Ing. Gonzalo Cevallos
5              Termogas Machala
6        Termoeléctrica Quevedo
7    Termoeléctrica Santa Elena
9          Nueva hidroeléctrica
dtype: object
"""
```

Analizando la sintaxis de las Series tenemos:
```Python
import pandas as pd
 
serie = pd.Series(data, index=index)
```

Ahora bien, profundicemos acerca del parámetro index:

- index=**index**, De donde **index** es la lista que se usará como referencia
para indexar.

Esto es:
```Python
import pandas as pd

powerPlants = pd.Series(
    [
        'Coca Codo Sinclair',
        'C.H. Molino',
        'Sopladora',
        'C.H. Minas San Francisco',
        'C.T. Ing. Gonzalo Cevallos',
        'Termogas Machala',
        'Termoeléctrica Quevedo',
        'Termoeléctrica Santa Elena',
        'C.H. Manta'
    ],
    index=['CC', 'CM', 'S', 'CM', 'CT', 'TM', 'TQ', 'TS', 'CM']
)

print(f"Plantas Generadoras de Electricidad:\n{powerPlants}")

# Output:
"""
Plantas Generadoras de Electricidad:
CC    Coca Codo Sinclair
CM    C.H. Molino
S     Sopladora
CM    C.H. Minas San Francisco
CT    C.T. Ing. Gonzalo Cevallos
TM    Termogas Machala
TQ    Termoeléctrica Quevedo
TS    Termoeléctrica Santa Elena
CM    C.H. Manta
dtype: object
"""

```

Observe que si modificamos un índice que afecte a varios elementos modificamos todos aquellos elementos con el mismo índice o etiqueta. Ocurre de igual manera al eliminar datos en una serie.

### Dataframes (Unión de series) --> (nueva_columna_datos = df[nueva_columna])
Estas son estructuras de datos bidimensionales la cual es similar a una hoja de cálculo de excel. Es decir, consta de filas y columnas indexadas.

```Python
import pandas as pd
 
serie = pd.Dataframe(data, index=index)
```

De donde:
- data: usualmente es un diccionario (clave-valor).
- index: lista usada para indexar los elementos.

Por ejemplo:
```Python
import pandas as pd

datos = {
    'Estado': ['Guanajuato', 'Querétaro', 'Jalisco', 'Durango', 'Colima'],
    'Población': [5486000, 1828000, 7351000, 1633000, 723455],
    'Superficie': [30607, 11699, 78588, 123317, 5627]
}

Datos_Estados = pd.DataFrame(datos)

print(f"Población y Superficie: {Datos_Estados}")
print(f"El tamaño del dataframe: {Datos_Estados.shape}")

# Output
"""
Población y Superficie:
        Estado  Población  Superficie
0   Guanajuato    5486000        30607
1   Querétaro    1828000        11699
2     Jalisco    7351000        78588
3     Durango    1633000       123317
4      Colima     723455         5627
El tamaño del dataframe: (5, 3)
"""
```

Note que, podemos modificar su indexación:
import pandas as pd

```Python
datos = {
    'Estado': ['Guanajuato', 'Querétaro', 'Jalisco', 'Durango', 'Colima'],
    'Población': [5486000, 1828000, 7351000, 1633000, 723455],
    'Superficie': [30607, 11699, 78588, 123317, 5627]
}

Datos_Estados = pd.DataFrame(
    datos,
    index=['item 1', 'item 2', 'item 3', 'item 4', 'item 5']
)

print(f"Población y Superficie: {Datos_Estados}")

# Output
"""
Población y Superficie:
            Estado  Población  Superficie
item 1  Guanajuato    5486000        30607
item 2  Querétaro    1828000        11699
item 3    Jalisco    7351000        78588
item 4    Durango    1633000       123317
item 5     Colima     723455         5627
"""
```

Ahora bien. ¿Cómo podemos acceder a un elemento en particular en los dataFrames?. Recordando que las series al ser lineales, para usar un elemento solo era necesario su índice.

Sobre seleccionar una columna del data frame:
Sea df un dataframe cualquiera. Entonces podremos seleccionar la columna n si:
```Python
print(df.columnan)
print(df[columnan])
```

Sobre seleccionar una fila del data frame:
Sea df un dataframe cualquiera. Entonces podremos seleccionar la fila m si:
```Python
print(df.iloc[filam])
print(df.iloc[filaI, filaF])
```

También podemos dar un vistazo rápido a las primeras 5 filas de un data frame con **df.head()**. Aunque el argumento de esta función indica cuántas filas se mostrarán sin incluir el final. Esto es 
**df.head(hastaQueFilaAvanzaSinIncluir)**.

Además también tenemos **df.tail()** que nos muestra los últimos 5 elementos del dataframe. Aunque el argumento de esta función indica cuántas filas se mostrarán (del final) sin incluir el final. Esto es **df.tail(hastaQueFilaAvanzaSinIncluir)**.

Note que **.head()** y **.tail()** retornan dataframes.

#### Propiedades de los dataframes
- df.columns: retorna una lista con los nombres de la columna (cabeceras). También podemos modificar esta columna de la siguiente forma df.columns = nueva_cabecera, siendo nueva cabecera una lista.

- df.index: retorna cómo están enumeradas las listas. Por ejemplo: "RangeIndex(start=0, stop=150, step=1)"

#### Métodos de los dataframes
- df.describe(): retorna un dataframes que se compone de las siguientes cabeceras: 

  count	(Conteo): Te dice cuántos datos no nulos hay. (Si tienes 150 filas y aquí dice 148, sabes que te faltan 2 datos).

  mean (Promedio): La media aritmética de toda la vida.

  std	(Desviación Estándar):	Qué tan "dispersos" están tus datos. (Si es alta, los datos varían mucho; si es baja, son todos parecidos).

  min	(Mínimo):	El valor más pequeño encontrado.

  25%	(Primer Cuartil):	El límite donde cae el 25% más bajo de tus datos.

  50%	(Mediana): El dato justo en el medio. (A veces es más útil que el promedio si hay valores extremos).

  75% (Tercer Cuartil): El límite donde está el 75% de tus datos.

  max (Máximo):	El valor más alto encontrado.

- df['columna'].value_counts(): retorna una serie con la cantidad de veces que se repite cada dato de la columna.

- df.T: para transponer el dataframe (columna por filas y filas por columnas)

- df.sort_values["enFunciónDeQuéColumna", ascending=False]: retorna un dataframe pero ordenado de tal forma que estén los datos de la columan "enFunciónDeQuéColumna" de forma descendente.

# 10ma Semana
# Importar y exportar archivos con pandas
Ahora que ya sabemos los tipos de estructuras de datos básicos, procederemos al estudio
de cómo se puede importar archivos externos al programa que contengan datos. De esta forma podremos trabajar con ficheros que contegan información (como csv) y tratarlos como tablas en excel.

Para importar un archivo csv:
```Python
import pandas as pd
 
any_data_frame = pd.read_csv('ubicación')

# Observe la variación sin cabezera

any_data_frame = pd.read_csv('ubicación', header=None)
```

Un ejemplo de dataframes con cabecera y sin cabecera sería:
- Con cabecera:
  ```Python
  import pandas as pd

  df = pd.read_csv('/content/paises.csv')
  print(df)

  # Output:
  """
    Categoria Codigo  Habit_x_km2       Pais  Poblacion  Superficie
  0         C   ARGE         22.0  Argentina   45167000     1964375
  1         A   COLO         17.0   Colombia   48922000     2780400
  2         B   ESPA         93.0     Espana   47099000      505944
  3         B   MEXI        111.0     Mexico  127212000     1142748
  4         C   VENE         35.0  Venezuela   32423000      916445
  5       NaN    NaN          NaN     Brasil  210688000     8515770
  6       NaN    NaN          NaN      Chile   19241000       56102
  """
  ```

- Sin cabecera:
  ```Python
  import pandas as pd

  df = pd.read_csv('/content/paises.csv', header=None)
  # Con esto le decimos a pandas que todo nuestro csv son los datos
  # Si header=0 nuestras cabeceras serían los primeros datos del archivo (por defecto)
  # Si header=1 nuestras cabeceras serían los segundos datos del archivo

  print(df)

  # Output:
  """
            0       1            2          3          4           5
  0  Categoria  Codigo  Habit_x_km2       Pais  Poblacion  Superficie
  1          C    ARGE         22.0  Argentina   45167000     1964375
  2          A    COLO         17.0   Colombia   48922000     2780400
  3          B    ESPA         93.0     Espana   47099000      505944
  4          B    MEXI        111.0     Mexico  127212000     1142748
  5          C    VENE         35.0  Venezuela   32423000      916445
  6        NaN     NaN          NaN     Brasil  210688000     8515770
  7        NaN     NaN          NaN      Chile   19241000       56102
  """
  ```

Para añadir cabeceras personalizadas, lo hacemos de la siguiente forma:
```Python
import pandas as pd

df = pd.read_csv('/content/paises.csv', header=None)
print(df)

# Output:
"""
          0       1            2          3          4           5
0  Categoria  Codigo  Habit_x_km2       Pais  Poblacion  Superficie
1          C    ARGE         22.0  Argentina   45167000     1964375
2          A    COLO         17.0   Colombia   48922000     2780400
3          B    ESPA         93.0     Espana   47099000      505944
4          B    MEXI        111.0     Mexico  127212000     1142748
5          C    VENE         35.0  Venezuela   32423000      916445
6        NaN     NaN          NaN     Brasil  210688000     8515770
7        NaN     NaN          NaN      Chile   19241000       56102
"""

cabecera = ["Categoria", "Código", "Habit_x_km2", "País", "Población", "Superficie"]

df.columns = cabecera

# Output:
"""
   Categoria  Código  Habit_x_km2       País  Población  Superficie
0  Categoria  Codigo  Habit_x_km2       Pais  Poblacion  Superficie
1          C    ARGE         22.0  Argentina   45167000     1964375
2          A    COLO         17.0   Colombia   48922000     2780400
3          B    ESPA         93.0     Espana   47099000      505944
4          B    MEXI        111.0     Mexico  127212000     1142748
5          C    VENE         35.0  Venezuela   32423000      916445
6        NaN     NaN          NaN     Brasil  210688000     8515770
7        NaN     NaN          NaN      Chile   19241000       56102
"""

```
