## DESARROLLE EL EJERCICIO 01
## NOMBRE Y APELLIDO
nombre = input("Ingrese su nombre: ").upper()
ciudad = input("Ingrese su ciudad de origen: ")

saludo = f'Hola, {nombre}!, Bienvenido a nuestro programa desde {ciudad}.'
print(f'\n{saludo:<40}') # "Alinear el saludo a la izquierda en un ancho de 40 caracteres"






## DESARROLLE EL EJERCICIO 02
## NOMBRE Y APELLIDO
correo_ingresado = input("Ingrese su correo electrónico: ")


if '@' not in correo_ingresado:
  print("ERROR: Introduzca un correo electrónico válido")
else:
  correo = correo_ingresado.split('@')
  nombre_usuario = correo[0]
  dominio = correo[1]

  print(f'El nombre de usuario es: {nombre_usuario:<20}')
  print(f'El dominio es: {dominio:>25}')