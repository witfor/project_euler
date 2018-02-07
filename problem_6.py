#Simple brute force

def sum_of_squares(n):
    """Returns the sum of square of first n natural numbers."""

    return sum([x ** 2 for x in range(n + 1)])

def square_of_sum(n):
    """Returns square of sum of first n natural numbers."""

    return (n * (n + 1) / 2) ** 2

def sum_square_difference(n):

    return square_of_sum(n) - sum_of_squares(n)

if __name__ == "__main__":
    print(sum_square_difference(100))
