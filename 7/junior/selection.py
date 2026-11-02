import random
import time

def selection(arr):
    for i in range(0, len(arr) - 1):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]

def main():
    sizes = [10**2, 10**3, 10**4, 10**5, 10**6]
    for size in sizes:
        arr = [random.randint(0, 999) for _ in range(size)]
        start = time.perf_counter()
        selection(arr)
        elapsed = time.perf_counter() - start
        print(f"Размер: {size}, Время: {elapsed:.6f} с.")

main()