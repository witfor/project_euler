def multiples_3_5(n):
    '''Returns the sum of natrual numbers below n that are multiples of 3 and 5.'''

    return sum(x for x in range(n) if x % 3 == 0 or x % 5 ==0 )

if __name__ == "__main__":
    print(multiples_3_5(1000))
