import random
import time

def insertion(arr):
    res = arr
    for i in range(0, len(res)):
        x = res[i]
        j = i - 1
        while (j >= 0 and res[j] > x):
            res[j + 1] = res[j]
            j = j - 1
        res[j + 1] = x
        i += 1
    return res

def main():
    rand_array = [random.randint(1, 10000) for _ in range(10**4)]
    start_time = time.perf_counter()
    insertion(rand_array)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Время выполнения: {elapsed_time:.6f} с.")

main()