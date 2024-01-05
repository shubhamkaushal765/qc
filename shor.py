"""
Shor'r algorithm:
    - find period x^r = 1 mod N: r is the period, N is the number to factor.
    - Let N = pq, where p, q are prime numbers
    - Period Finding
        - pick x at random from (1, N)
        - if gcd(x, N) != 1, then p or q must be that gcd.
        - else x and N must be coprimes. Find r (the period).
        - repeat for different values of x.
    - x^r = 1 mod N => x^r - 1 = 0
    - If r is even, then it can be split into two factors, which must be some mulitples of p and q.
"""

from utils import gcd, is_prime
import random, math

def find_period(x, N):
    """Brute force period finding algorithm"""
    assert gcd(x, N) == 1, "The numbers must be coprimes."
    r = 1
    remainder = x

    # multiply remainder with x to get the next exponent and get the remainder.
    # if remainder is 1, then we have hit the cycle, as x^0 mod N is also 1.
    while remainder!=1:
        r += 1
        remainder  = (remainder * x) % N
    return r

def get_2_prime_numbers_below_n(n):
    """Get 2 prime numbers below n"""
    result = []
    for i in range(n, 0, -1):
        if is_prime(i):
            result.append(i)
        if len(result) == 2:
            break
    return result

def classical_shor(N):
    """
    Classical implementation of Shor algorithm.
    N: is the number to factor
    returns the factors of N.
    """

    print("Starting Classical Shor's algorithm...")
    print(f"To Factor, N: {N}")

    # values of x for which r is not even
    invalid_x = set()
    r = 1 # random initialization

    while r % 2 != 0:
        x = random.randint(2, N-1)
        if x in invalid_x:
            continue

        first_test = gcd(x, N)

        # if x and N have a common factor, then factors of N can be easily computed.
        if first_test != 1:
            return first_test, N // first_test
        
        r = find_period(x, N)
        if r % 2 == 1:
            invalid_x.add(x)
    print(f"Base, X: {x}, \nExponent, R: {r}")

    # find the factors of N from the x and r
    p = gcd(x**(r//2)-1, N)
    q = N // p
    print(f"The factors are: {p}, {q}.")
    print("================================================")
    return p, q


if __name__ == '__main__':
    
    inputs = get_2_prime_numbers_below_n(100)
    print(inputs)

    to_factor = inputs[0] * inputs[1]
    classical_shor(to_factor)