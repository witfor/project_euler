from problem_012 import factors

def sum_amicable_numbers_under(n):
    """Returns the sum of all amicable numbers under n.

    Let d(n) be defined as the sum of proper divisors of n
    (numbers less than n which divide evenly into n).

    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and
    each of a and b are called amicable numbers.
    """

    list = []
    count = 0
    for num in range(1, n):
        if num not in list:
            sd = sum(factors(num)[:-1])
            if num == sum(factors(sd)[:-1]) and num != sd:
                list.append(num)
                list.append(sd)
                count += sd + num
    return count

if __name__ == "__main__":
    print(sum_amicable_numbers_under(10000))
