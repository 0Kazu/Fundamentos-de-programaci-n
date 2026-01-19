#Escriba su solución:
def filtrar_palabras(lista_palabras):
    palabras_filtradas = []
    for palabra in lista_palabras:
        if len(palabra) >= 2 and palabra[0] == palabra[-1]:
            palabras_filtradas.append(palabra)

    # Ya teniendo la lista modificada
    return palabras_filtradas

lista = ["La", "Hola", "Diego", "ala", "Ese", "pared", "ocioso", "c", ""]

print(filtrar_palabras(lista))