# Initial Solution
from problem_007 import is_prime
def simple_sum_primes_below(n):
    '''Returns the sum of all primes below n.'''
    sum = 0
    if n > 1:
        sum = 2
    for num in range(1, n, 2):
        if is_prime(num):
            sum += num
    return sum

# Solution Implementing Sieve of Eratosthenes
def sum_primes_below(n):
    '''Returns the sum of all primes below n (using sieve of Eratosthenes).'''
    if n == 1 or n == 2:
        return 0
    sum = 2
    sieve = {}
    for num in range(3, n, 2):
        sieve[num] = True
    sieve[2] = True
    midpoint = int(n**0.5)
    if midpoint % 2 == 0:
        midpoint += 1

    for num in range(3, midpoint, 2):
        if sieve[num] == True:
            sum += num
        for num in range(num**2, n, 2*num):
            sieve[num] = False

    for num in range(midpoint, n, 2):
        if sieve[num] == True:
            sum += num
    return sum

if __name__ == '__main__':
    print(sum_primes_below(2000000))
