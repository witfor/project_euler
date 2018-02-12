def sumDigits(number):
    """Returns the sum of a number's digits."""

    return sum([int(x) for x in str(number)])

if __name__ == "__main__":
    print(sumDigits(2**1000))
