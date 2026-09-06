def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def combinations(n, k):
    if n < 0 or k < 0 or n < k:
            return 0
    return factorial(n) // (factorial(k) * factorial(n - k))

n = 6
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

print(result)
    