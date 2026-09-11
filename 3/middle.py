import math

def power_n(n, m):
    if m == 0: return 1
    res_half = power_n(n, m // 2)
    if (m % 2 > 0):
        return n * res_half * res_half
    else:
        return res_half * res_half

print(power_n(2, 10))

def power_bit(n, m):
    if m == 0: return 1
    mask = 0x800000000
    while (m & mask == 0):
        mask >>= 1
    result = 1
    while (mask > 0):
        if (m & mask > 0):
            result *= result * n
        else:
            result *= result
        mask >>= 1
    return result

print(power_bit(2, 10))

def fibonacci_const(n):
    phi = (1 + math.sqrt(5.0)) / 2.0
    return (math.floor(math.pow(phi, n) / math.sqrt(5.0) + 1.0 / 2.0))

print(fibonacci_const(1000))

def is_prime_simplified(n):
    for i in range (2, n):
        if (n % i == 0):
            return False
    return True

print(is_prime_simplified(10))

def is_prime_simplified_odd(n):
    if n == 2: return True
    if (n % 2 == 0): return False
    for i in range (3, n, 2):
        if (n % i == 0):
            return False
    return True

print(is_prime_simplified_odd(11))

def is_prime_simplified_sqrt(n):
    if n == 2: return True
    if (n % 2 == 0): return False
    sqrt = math.ceil(math.sqrt(n)) + 1
    for i in range (3, sqrt, 2):
        if (n % i == 0):
            return False
    return True

print(is_prime_simplified_sqrt(12))

def prime_count(n):
    result = 0
    for i in range(2, n):
        if (is_prime_simplified_sqrt(i)):
            result += 1
    return result

print(prime_count(1000))

def eratosphen(n):
    primes = [False] * (n + 1)
    count = 0
    for i in range(2, n + 1):
        if not primes[i]:
            count += 1
            for j in range(i * i, n + 1, i):
                primes[j] = True
    return count

print(eratosphen(1000))