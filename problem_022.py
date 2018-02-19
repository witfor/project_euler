def alphabetical_value(word):
    """Returns the alphabetical value of a word.

    COLIN, colin = 3 + 15 + 12 + 9 + 14 = 53
    """

    return sum([ord(letter.lower()) - 96 for letter in word])

if __name__ == "__main__":
    with open('problem_022_names.txt') as f:
        f_content = f.read()
    name_list = f_content.replace('"', '').split(',')
    name_list.sort()
    print(sum([(i + 1) * alphabetical_value(name) for i, name in enumerate(name_list)]))
