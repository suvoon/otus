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
    rand_array = [random.randint(1, 10**7) for _ in range(10**6)]
    start_time = time.perf_counter()
    selection(rand_array)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Время выполнения: {elapsed_time:.6f} с.")

main()