datos = "NoMBre: juan perez, Edad: 30, Ciudad: MaDRid, Profesión: ingeniero"
datos_por_separado = datos.split(",")
print(f'{datos_por_separado[0].split(":")[0].upper()  + ":":>15}{datos_por_separado[0].split(":")[1].title()}')
print(f'{datos_por_separado[1].split(":")[0].upper() + ":":>15}{datos_por_separado[1].split(":")[1].title()}')
print(f'{datos_por_separado[2].split(":")[0].upper() + ":":>15}{datos_por_separado[2].split(":")[1].title()}')
print(f'{datos_por_separado[3].split(":")[0].upper() + ":":>15}{datos_por_separado[3].split(":")[1].title()}')