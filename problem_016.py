def sumNumberDigits(number):
    """Returns the sum of a number's digits."""

    string_number = str(number)
    answer = 0
    for digit in string_number:
        answer += int(digit)
    return answer

if __name__ == "__main__":
    print(sumNumberDigits(2**1000))
