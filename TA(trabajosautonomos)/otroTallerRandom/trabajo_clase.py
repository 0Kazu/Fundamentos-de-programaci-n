'''Los arreglos son:
   - Colección de datos ordenada mutable de tipo homogéneo.
   - Se necesita de una libreria para definir arreglos y utilizar sus funciones.
   - Son más eficientes y rápidos en comparación con otras colecciones de datos.
   - Se puede construir arreglos de 1, 2, ..., N dimensiones.
   
   La librería para definir los arreglos es numpy'''

# Llamar a la libreria
import numpy as np

arrCalificaciones = np.array([5.6, 9.8, 7.4, 6.3])
lista_calificaciones = [5.6, 9.8, 7.4, 6.3]
arrEstudiantes = np.array(["Andrea", "Julian", "Juan", "Diego"])
arrNotas = np.array([[7.5, 6.2, 5.4, 10.0], [8.5, 7.5, 6.2, 10.0]])

print(f"arrCalificaciones: {arrCalificaciones}")

# Output: [5.6 9.8 7.4 6.3]
# Note que no es lista porque sino: [5.6, 9.8, 7.4, 6.3]

print(f"Lista de Calificaciones: {lista_calificaciones}")
print(f"arrEstudiantes: {arrEstudiantes}")
print(f"arrNotas:\n {arrNotas}")


# Propiedades de los arreglos
print("\nPropiedades de los arreglos")
print(f"Tamaño de Calificaciones: {arrCalificaciones.size}")
print(f"Tamaño de arrNotas: {arrNotas.size}")

print(f"Dimension de Calificaciones: {arrCalificaciones.ndim}")
print(f"Dimension de Notas: {arrNotas.ndim}")

print(f"Shape de Calificaciones: {arrCalificaciones.shape}")
print(f"Shape de Notas: {arrNotas.shape}")

print(f"Tipo de dato: {arrCalificaciones.dtype}")
print(f"Tipo de dato: {arrEstudiantes.dtype}")
print(f"Tipo de dato: {arrNotas.dtype}")


