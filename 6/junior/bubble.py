import random
import time

def bubble(arr):
    res = arr
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if (arr[j] > arr[j + 1]):
                res[j], res[j + 1] = res[j + 1], res[j]
    return res

def main():
    rand_array = [random.randint(1, 10000) for _ in range(10**4)]
    start_time = time.perf_counter()
    bubble(rand_array)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

main()