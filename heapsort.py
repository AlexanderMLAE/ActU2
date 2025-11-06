import time
inicio = time.time()
# Algoritmos de ordenamiento

def heapify(A, n, i):
    heapify.count += 1
    max = i
    left = 2 * i + 1
    right = 2 * i + 2

    if (left < n and A[i] < A[left]):
        max = left

    if (right < n and A[max] < A[right]):
        max = right

    if (max != i):
        A[i], A[max] = A[max], A[i]
        heapify(A, n, max)
heapify.count = 0   

def heapsort(A):
    n = len(A)

    for i in range(n, 0, -1):
        heapify(A, n, i)
        

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        heapify(A, i, 0)

# Usar misma lista predefinida
arr = []

with open("file.txt", "r") as f:
    content = f.read()
    arr = eval(content)
    print(type(arr), arr)


# ejecutar algoritmo

heapsort(arr)

print ("Sorted array is")
print (arr)

with open("heapResult.txt", "w", encoding="utf-8") as f:
    f.write(str(arr))

# tiempo

fin = time.time()

operaciones = heapify.count

tiempo = fin - inicio
flops = operaciones/tiempo
print("Tiempo: ", tiempo, "\n Operaciones: ", operaciones, "\n FLOPS: ", flops)
