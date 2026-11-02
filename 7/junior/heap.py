import random
import time

def heapify(arr, root, size):
    p = root
    l = 2 * p + 1
    r = 2 * p + 2
    if (l < size and arr[l] > arr[p]):
        p = l
    if (r < size and arr[r] > arr[p]):
        p = r
    if (p == root):
        return
    arr[root], arr[p] = arr[p], arr[root]
    return heapify(arr, p, size)

def heap(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        heapify(arr, i, len(arr))

    for i in range(len(arr) - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)

def main():
    sizes = [10**2, 10**3, 10**4, 10**5, 10**6]
    for size in sizes:
        arr = [random.randint(0, 999) for _ in range(size)]
        start = time.perf_counter()
        heap(arr)
        elapsed = time.perf_counter() - start
        print(f"Размер: {size}, Время: {elapsed:.6f} с.")

main()
