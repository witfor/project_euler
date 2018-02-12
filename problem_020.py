from problem_016 import sumDigits

def factorial(n):
    """Returns n!."""
    answer = 1
    for i in range(1, n+1):
        answer *= i
    return answer

if __name__ == "__main__":
    print(sumDigits(factorial(100)))
