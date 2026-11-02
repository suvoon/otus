import random
import time

def shell(arr):
    res = arr[:]
    gap = len(res) // 2
    while (gap > 0):
        for i in range(gap, len(res)):
            j = i
            while (j >= gap):
                if (res[j - gap] <= res[j]):
                    break
                res[j - gap], res[j] = res[j], res[j - gap]
                j -= gap
        gap //= 2
    return res

def main():
    rand_array = [random.randint(1, 10000) for _ in range(10**4)]
    start_time = time.perf_counter()
    shell(rand_array)
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Время выполнения: {elapsed_time:.6f} с.")

main()