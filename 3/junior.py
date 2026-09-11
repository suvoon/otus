def power(n, m):
    result = n
    for i in range(m - 1):
        result *= n
    return result

print(power(2, 11))

def fibonacci_recursion(n):
    if n == 1: return 1
    if n == 2: return 1
    return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)

print(fibonacci_recursion(6))

def fibonacci_iteration(n):
    n1, n2 = 1, 1
    for i in range (2, n):
        n3 = n1 + n2
        n1, n2 = n2, n3
    return n2

print(fibonacci_iteration(20))

def is_prime(n):
    count = 0
    for i in range (1, n + 1):
        if (n % i == 0):
            count += 1
    if count == 2: return True
    return False

print(is_prime(10))

def prime_count(n):
    result = 0
    for i in range(2, n):
        if (is_prime(i)):
            result += 1
    return result

print(prime_count(1000))