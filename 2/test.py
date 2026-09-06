import os

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combinations(n, k):
    if n < 0 or k < 0 or n < k:
            return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

def solution(n_str):
    n = int(n_str[0])

    result = 0
    for i in range (0, 9 * n + 1):
        sum_count = 0
        for j in range (0, 10):
            if (i >= j and (9 * (n-1) + j) >= i):
                x = i - j
                y = (n - 1) or 1

                total_comb = 0
        
                for k in range(y + 1):
                    n_comb = x - 10 * k + y - 1
                    if n_comb < y - 1:
                        break
                        
                    sign = 1 if k % 2 == 0 else -1
                    total_comb += sign * combinations(y, k) * combinations(n_comb, y - 1)
                
                sum_count += total_comb

        result += sum_count * sum_count

    return result

class Test:
    def __init__(self, run_func):
        self.run_func = run_func

    def run(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))

        iter_num = 0
        while True:
            file_in = os.path.join(base_dir, "Tests", f"test.{iter_num}.in")
            file_out = os.path.join(base_dir, "Tests", f"test.{iter_num}.out")
            
            if not os.path.exists(file_in) or not os.path.exists(file_out):
                return
                
            with open(file_in, "r", encoding="utf-8") as f:
                input_data = f.read().splitlines()
                
            with open(file_out, "r", encoding="utf-8") as f:
                output_data = f.read().splitlines()
                
                
            x = str(self.run_func(input_data))
            
            if x == output_data[0]:
                print(f"Тест {iter_num} OK: {x}")
            else:
                print(f"Тест {iter_num} ошибка: {x} ожидалось: {output_data[0]}")
                
            iter_num += 1

tester = Test(solution)
tester.run()