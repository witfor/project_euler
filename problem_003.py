def largest_prime_factor(n):
    '''Returns the largest prime factor of n recursively.'''

    if n == 1:
        return 1
    if n == 2:
        return 2
    elif n % 2 == 0:
        return max(2, largest_prime_factor(n / 2))
    for x in range(3, (int(n) + 1)**2, 2):
        if n % x == 0:
            return max(x, largest_prime_factor(n / x))
    # If no factors from 1 to (n + 1)**2, then n is prime
    return n

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
