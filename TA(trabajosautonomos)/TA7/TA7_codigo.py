nombre_articulo1 = input(f'Ingrese el nombre del primer artículo: ')
precio_unitario1 = float(input(f'Ingrese el precio unitario de {nombre_articulo1}: '))
cantidad_articulo1 = int(input(f'Ingrese la cantidad de {nombre_articulo1} que desea comprar: '))
total_articulo1 = precio_unitario1*cantidad_articulo1

nombre_articulo2 = input(f'\nIngrese el nombre del segundo artículo: ')
precio_unitario2 = float(input(f'Ingrese el precio unitario de {nombre_articulo2}: '))
cantidad_articulo2 = int(input(f'Ingrese la cantidad de {nombre_articulo2} que desea comprar: '))
total_articulo2 = precio_unitario2*cantidad_articulo2

nombre_articulo3 = input(f'\nIngrese el nombre del tercer artículo: ')
precio_unitario3 = float(input(f'Ingrese el precio unitario de {nombre_articulo3}: '))
cantidad_articulo3 = int(input(f'Ingrese la cantidad de {nombre_articulo3} que desea comprar: '))
total_articulo3 = precio_unitario3*cantidad_articulo3

total_articulos = total_articulo1 + total_articulo2 + total_articulo3

descuento = total_articulos > 100
descuento_aplicado = total_articulos * (int(descuento) * 0.10)

impuesto = (total_articulos - descuento_aplicado) * 0.18

total_general = (total_articulos + impuesto) - descuento_aplicado

resumen = "Resumen de la compra"
print(f'\n{resumen:-^47}')
titulos_tabla = ["Artículo", "Cantidad", "Precio", "Unitario Total"]

print(f'{titulos_tabla[0]:<14} {titulos_tabla[1]:<9} {titulos_tabla[2]:<7} {titulos_tabla[3]}')
print(f'{nombre_articulo1:<14} {cantidad_articulo1:<9} {precio_unitario1:^{len(titulos_tabla[2])}} {total_articulo1:>{len(titulos_tabla[3])}}')
print(f'{nombre_articulo2:<14} {cantidad_articulo2:<9} {precio_unitario2:^{len(titulos_tabla[2])}} {total_articulo2:>{len(titulos_tabla[3])}}')
print(f'{nombre_articulo3:<14} {cantidad_articulo3:<9} {precio_unitario3:^{len(titulos_tabla[2])}} {total_articulo3:>{len(titulos_tabla[3])}}')

print(f'\nSubtotal: ${total_articulos}')
print(f'Descuento (10%): -${descuento_aplicado:.2f}')
print(f'Impuesto (18%): +${impuesto:.2f}')
print(f'Total a pagar ${total_general:.2f}')