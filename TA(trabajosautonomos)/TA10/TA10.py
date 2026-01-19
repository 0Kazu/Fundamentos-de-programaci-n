## ESCRIBA SU SOLUCION
comentarios = [
    "El producto es excelente y útil",
    "Muy mala calidad, se rompió rápido",
    "Buen servicio, volveré a comprar",
    "No me gustó el empaque",
    "El servicio fue pésimo y lento"
]

palabras_sensibles = ["mala", "pésimo", "horrible", "terrible"]


# Contar cuántos comentarios contienen una palabra clave
def contar_palabra_clave(lista, palabra):
    palabra = palabra.lower()
    contador = 0
    for comentario in lista:
        if palabra in comentario.lower():
            contador += 1
    return contador


# Contar cuántos comentarios tienen más de 4 palabras
def contar_comentarios_largos(lista):
    contador = 0
    for comentario in lista:
        palabras = comentario.split()
        if len(palabras) > 4:
            contador += 1
    return contador


# Quitar palabras negativas
def reemplazar_palabras_negativas(lista, palabras_sensibles):
    nueva_lista = []
    for comentario in lista:
        palabras = comentario.split()
        nuevas_palabras = []

        for palabra in palabras:
            if palabra.lower().strip(",.") in palabras_sensibles:
                nuevas_palabras.append("***")
            else:
                nuevas_palabras.append(palabra)

        nueva_lista.append(" ".join(nuevas_palabras))

    return nueva_lista

clave = "servicio"
print(f'La palabra \'{clave}\' aparece en {contar_palabra_clave(comentarios, clave)} comentario(s).')

print(f'Cantidad de comentarios con más de 4 palabras: {contar_comentarios_largos(comentarios)}\n')

print("Comentarios con palabras censuradas:")
censurados = reemplazar_palabras_negativas(comentarios, palabras_sensibles)
for c in censurados: # comentarios con/sin censura
    print(f'- {c}')