import random
import time

def split(arr, left, right):
    pivot = arr[right]
    M = left - 1

    for j in range(left, right + 1):
        if pivot >= arr[j]:
            M += 1
            if M != j:
                arr[M], arr[j] = arr[j], arr[M]

    return M


def qsort(arr, left, right):
    if left >= right:
        return

    M = split(arr, left, right)
    qsort(arr, left, M - 1)
    qsort(arr, M + 1, right)
    return


def main():
    sizes = [10**2, 10**3, 10**4, 10**5, 10**6]
    for size in sizes:
        rand_arr = [random.randint(1, 10**6) for _ in range(size)]

        start_time = time.perf_counter()
        qsort(rand_arr, 0, len(rand_arr) - 1)
        elapsed_time = time.perf_counter() - start_time
        if elapsed_time > 120:
            print(f"Размер: {size}, Время: timeout (превышено 2 минуты)")
        else:
            print(f"Размер: {size}, Время: {elapsed_time:.6f} с.")


main()