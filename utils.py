def gcd(a, b):
    """Greatest common divisor of two integers"""
    x, y = max(a, b), min(a, b)
    if y == 0: return x
    x, y = y, x % y
    return gcd(x, y)

def is_prime(n):
    """Check whether a number is prime"""
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True