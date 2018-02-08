def largest_palindrome(num_digits):
    '''Returns the largest palindrome made from a product of two num_digits numbers.'''

    start = int('9'*num_digits)
    largest_now = 0
    i = start
    j = start

    for i in range (start, start//10, -1):
        for j in range (start, i, -1):
            if i * j < largest_now:
                # break: all other candidates will be smaller than largest_now
                break
            if str(i * j) == str(i * j)[::-1]:
                largest_now = i * j
    return largest_now

if __name__ == "__main__":
    print(largest_palindrome(3))
