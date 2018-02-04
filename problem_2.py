
if __name__ == "__main__":
    # Initial Fibonacci values
    a = 1
    b = 2
    sum_even_valued_terms = b

    while a + b < 4000000:
        if (a + b) % 2 == 0:
            sum_even_valued_terms += a + b
        a, b = b, a + b
    print(sum_even_valued_terms)
