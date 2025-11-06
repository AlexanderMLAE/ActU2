
# Usar misma lista predefinida
arr = []

with open("file.txt", "r") as f:
    content = f.read()
    arr = eval(content)
    print(type(arr), arr)

# Algoritmos de ordenamiento

def heapify(A, n, i):
    max = i
    left = 2*i+1
    right = 2*i+2

    if (left < n and A[i] < A[left]):
        max = left

    if (right < n and A[max] < A[right]):
        max = right

    if (max != i):
        A[i], A[max] = A[max], A[i]
        heapify(A, n, max)

def heapsort(A):
    n = len(A)
    for i in range(n, 0, -1):
        heapify(A, n, i)

    for i in range(n-1, 0, -1):
        A[i], A[0] = A[0], A[i]

        heapify(A, i, 0)

# ejecutar algoritmo

heapsort(arr)

print ("Sorted array is")
print (arr)

try:
    with open("heapResult.txt", "x", encoding="utf-8") as f:
        f.write(str(arr))

except FileExistsError:
    print("heapResult.txt already exists, exclusive creation aborted.")