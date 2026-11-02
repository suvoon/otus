import random
import time


def counting_sort(arr):
    if not arr:
        return arr
    max_val = max(arr)
    count = [0] * (max_val + 1)
    for x in arr:
        count[x] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    output = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i]] - 1] = arr[i]
        count[arr[i]] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr


def main():
    sizes = [10**2, 10**3, 10**4, 10**5, 10**6]
    for size in sizes:
        arr = [random.randint(0, 999) for _ in range(size)]
        start = time.perf_counter()
        counting_sort(arr)
        elapsed = time.perf_counter() - start
        print(f"Размер: {size}, Время: {elapsed:.6f} с.")

main()