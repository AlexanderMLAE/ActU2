import ast
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]
        izquierda = [x for x in arr if x < pivote]
        centro = [x for x in arr if x == pivote]
        derecha = [x for x in arr if x > pivote]
        return quicksort(izquierda) + centro + quicksort(derecha)

# Leer los datos reales desde file.txt
with open("file.txt", "r", encoding="utf-8") as f:
    contenido = f.read().strip()
    lista = ast.literal_eval(contenido)  # Convierte el texto a lista real

repeticiones = 10
tiempos = []

for _ in range(repeticiones):
    inicio = time.time()
    quicksort(lista)
    fin = time.time()
    tiempos.append(fin - inicio)

promedio_tiempo = sum(tiempos) / len(tiempos)
N = len(lista)
num_operaciones = N * (N - 1) / 2
FLOPS = num_operaciones / promedio_tiempo

print(f"\n Tiempo promedio: {promedio_tiempo:.6f} segundos")
print(f"FLOPS aproximado: {FLOPS:,}")

lista_ordenada = quicksort(lista)

# Guardar la lista ordenada (los mismos valores, solo reordenados)
with open("quicksortResult.txt", "w", encoding="utf-8") as f:
    f.write(str(lista_ordenada))
    print("\nLa lista ordenada se ha guardado en 'quicksortResult.txt'")
