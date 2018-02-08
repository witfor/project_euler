# Original Solution
from problem_003 import largest_prime_factor
def slow_nth_prime(n):
    '''Returns the nth prime number.'''
    if n == 1:
        return 2
    x = 1
    xth_prime = 2
    guess = 3

    while x < n:
        if largest_prime_factor(guess) == guess:
            xth_prime = guess
            x += 1
        guess += 2
    return xth_prime

# Implemention of Faster Solution with is_prime(n) Function
def nth_prime(n):
    '''Returns the nth prime number using is_prime.'''

    if n == 1:
        return 2
    else:
        num_primes = 1
        x = 1
        while num_primes < n:
            x += 2
            if is_prime(x):
                num_primes += 1
        return x

def is_prime(n):
    '''Returns True if n is prime, False otherwise.'''

    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = int(n**0.5)
        f = 5
        while f <= r:
            if n % f == 0:
                return False
            elif n % (f + 2) == 0:
                return False
            f += 6
        return True

if __name__ == '__main__':
    print(nth_prime(10001))
