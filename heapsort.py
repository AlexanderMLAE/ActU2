import time
# Algoritmos de ordenamiento

def heapify(A, n, i):
    heapify.count += 1
    max = i
    left = 2 * i + 1
    right = 2 * i + 2

    if (left < n and A[left] > A[max]):
        max = left

    if (right < n and A[right] > A[max]):
        max = right

    if (max != i):
        A[i], A[max] = A[max], A[i]
        heapify(A, n, max)
heapify.count = 0   

def heapsort(A):
    n = len(A)

    for i in range(n, -1, -1):
        heapify(A, n, i)
        

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

# Usar misma lista predefinida

arr = []
tiempos = []
operaciones = []
# ejecutar algoritmo
for i in range(10):
    # Obtener arreglo desde el archivo
    with open("file.txt", "r") as f:
        content = f.read()
        arr = list(eval(content)) 

    inicio = time.time()

    heapsort(arr)

    # tiempo y operaciones
    fin = time.time()
    ops = heapify.count
    heapify.count = 0

    tiempo = fin - inicio
    tiempos.append(tiempo)
    operaciones.append(ops)
    print(f"{i+1}: Tiempo: {tiempo}     Operaciones:  {ops}")

tiemposAvg = sum(tiempos) / 10
operacionesAvg = sum(operaciones) / 10

flops = operacionesAvg/tiemposAvg

print(f"Tiempo en promedio: {tiemposAvg} \n Promedio de operaciones: {operacionesAvg} \n FLOPS: {flops}")

with open("heapResult.txt", "w", encoding="utf-8") as f:
    f.write(str(arr))


