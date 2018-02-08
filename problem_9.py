def special_pythag_triplet(num):
    '''Returns special Pythagorean product abc.

    Returns Pythagorean product a*b*c for which:
    a**2 + b**2 == c**2;
    a + b + c == num.
    '''

    a = 1
    b = 1
    for b in range(1, num):
        if a**2 + b**2 == (num - a - b)*2:
            return a*b*(num - a - b)
        for a in range(1, b):
            if a**2 + b**2 == (num - a - b)**2:
                return a*b*(num - a - b)

if __name__ == '__main__':
    print(special_pythag_triplet(1000))
