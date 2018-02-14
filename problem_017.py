def count_letters(integer):
    """Returns the number of letters in the written-form of integer.

    For example, 258 is written as "two-hundred and fifty-eight",
    which has 23 letters (hyphens and spaces are not counted):
    > count_values(258)
    23

    Note: count_letters only works for integers <= 1000.
    """
    mapping = int_to_written_mapping()
    if integer <= 20:
        return mapping[integer]
    elif integer < 100:
        return mapping[integer - (integer % 10)] + mapping[integer % 10]
    elif integer < 1000:
        if integer % 100 == 0:
            return mapping[integer // 100] + mapping[100]
        # Else, need to put "and" into count: this is 3 at the end of return
        else:
            return mapping[integer // 100] + mapping[100] + count_letters(integer % 100) + 3
    elif integer == 1000:
        return mapping[1] + mapping[1000]

def int_to_written_mapping():
    """Returns a dictionary of integer lengths used to compute count_values."""
    
    word_mapping = {0: "",
                    1: "one",
                    2: "two",
                    3: "three",
                    4: "four",
                    5: "five",
                    6: "six",
                    7: "seven",
                    8: "eight",
                    9: "nine",
                    10: "ten",
                    11: "eleven",
                    12: "twelve",
                    13: "thirteen",
                    14: "fourteen",
                    15: "fifteen",
                    16: "sixteen",
                    17: "seventeen",
                    18: "eighteen",
                    19: "nineteen",
                    20: "twenty",
                    30: "thirty",
                    40: "forty",
                    50: "fifty",
                    60: "sixty",
                    70: "seventy",
                    80: "eighty",
                    90: "ninety",
                    100: "hundred",
                    1000: "thousand"
                    }
    length_mapping = {}
    for key in word_mapping.keys():
        length_mapping[key] = len(word_mapping[key])
    return length_mapping

if __name__ == "__main__":
    print(sum([count_letters(num) for num in range(1, 1001)]))
