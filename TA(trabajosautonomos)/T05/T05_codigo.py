## ESCRIBA SU SOLUCION

listaEmpleados = [
    [8, 9, 7, 8, 9],  # Empleado 1
    [6, 7, 8, 6, 7],  # Empleado 2
    [9, 9, 9, 10, 9], # Empleado 3
    [8, 8, 8, 8, 8]   # Empleado 4
]

numero_de_empleado = 1
for empleado in listaEmpleados:
  print(f'Evaluando Empleado {numero_de_empleado}:')

  promedio = 0
  dia_actual = 1
  for hora in empleado:
    promedio += hora
    if hora >= 8:
      print(f'Día {dia_actual}: Cumplido ({hora} horas)')
    else:
      print(f'Día {dia_actual}: No cumplido ({hora} horas)')
    dia_actual += 1

  print(f'Promedio semanal: {promedio/len(empleado):.2f}')

  if (promedio/len(empleado)) > 8:
    print("Trabajador con horas extras.\n")
  elif (promedio/len(empleado)) == 8:
    print("Trabajador estandar.\n")
  else:
    print("Trabajador bajo rendimiento.\n")
  
  numero_de_empleado += 1