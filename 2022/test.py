
import math 

def prime_factors(n):
    primes = []
    # Print the number of two's that divide n
    while n % 2 == 0:
        primes.append(2)
        n = n // 2
    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3 , int(math.sqrt(n)) + 1 ,2):
        # while i divides n , print i and divide n
        while n % i == 0:
            primes.append(i)
            n = n // i

    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        primes.append(n)

    return set(primes)

print(prime_factors(2689604731076913576890751386907531890675813906785193076837657461378658794136578916389561))