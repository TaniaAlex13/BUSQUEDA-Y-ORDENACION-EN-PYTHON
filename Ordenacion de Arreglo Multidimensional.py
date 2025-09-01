# Programa 2: Ordenación de una fila en Arreglo Multidimensional

# Matriz
matriz = [
    [10, 4, 7],   # fila 1
    [3, 8, 2],    # fila 2
    [9, 5, 6]     # fila 3
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos todas las filas
for i in range(len(matriz)):
    matriz[i] = bubble_sort(matriz[i])

print("\nMatriz con todas las filas ordenadas:")
for fila in matriz:
    print(fila)
