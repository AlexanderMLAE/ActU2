# Bubble Sort
import time

def bubble_sort(arr):
    n = len(arr)
    comparaciones = 0
    intercambios = 0

    for i in range(n):
        for j in range(0, n - i - 1):
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                intercambios += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparaciones, intercambios

# Leer archivo file.txt con la lista
try:
    with open("file.txt", 'r') as archivo:
        mylist = archivo.read()
        lista_original = eval(mylist)

        cantidad_deseada = 10000
        lista_ordenada = lista_original.copy()
        lista_ordenada, _, _ = bubble_sort(lista_ordenada[:cantidad_deseada])
        
        print(f"\n El Archivo contiene {len(lista_ordenada):,} elementos:")

        tiempos, comps, intercs = [], [], []

    for i in range(10):
        lista_copia = lista_original.copy()
        
        inicio = time.time()
        lista_ordenada, comp, interc = bubble_sort(lista_copia[:cantidad_deseada])
        fin = time.time()

        tiempos.append(fin - inicio)
        comps.append(comp)
        intercs.append(interc)

        print(f"{i+1}: Tiempo de Ejecución: {tiempos[-1]:.8f} segundos")

    # Calcular promedios de Tiempo
    tiempo_promedio = sum(tiempos) / 10
    comp_promedio = sum(comps) / 10
    interc_promedio = sum(intercs) / 10

except FileNotFoundError:
    print("Error: No se encontró el archivo 'file.txt'")

#Tiempo
print(f"\nPromedio Tiempo de Computo: {tiempo_promedio:.8f} segundos")

#Operaciones
operaciones = comp_promedio + interc_promedio

print(f"\nTotal de Comparaciones: {comp_promedio:,}")
print(f"Total de Intercambios: {interc_promedio:,}")
print(f"Total de Operaciones: {operaciones:,}")

#FLOPS
Flops = operaciones / tiempo_promedio
print(f"\nFLOPS: {Flops:,.4f}")

with open("bubbleResult.txt", "w", encoding="utf-8") as f:
    f.write(str(lista_ordenada))