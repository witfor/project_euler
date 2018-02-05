def smallest_num_even_divisible(a, b):
    '''Returns the smallest positive number that is evenly divisible by all numbers from a to b.

    "Evenly divisible" means divisible with no remainder.
    '''

    def prime_factors(n):
        '''Returns a list of the prime factors of n (recursively).'''
        if n == 1:
            return [1]
        if n == 2:
            return [2]
        elif n % 2 == 0:
            return [2] + prime_factors(n / 2)
        for x in range(3, int(n) + 1, 2):
            if n % x == 0:
                return [x] + prime_factors(n / x)

    #Factor numbers a through b, tabulate min factors needed in dict min_factors
    min_factors = {}
    for x in range(a, b+1):
        list = prime_factors(x)
        xdict = dict((x, list.count(x)) for x in set(list))
        for key in xdict.keys():
            if key not in min_factors or min_factors[key] < xdict[key]:
                min_factors[key] = xdict[key]

    #Calculate answer
    answer = 1
    for key in min_factors.keys():
        answer *= key**min_factors[key]
    return answer

if __name__ == '__main__':
    print(smallest_num_even_divisible(1, 20))
