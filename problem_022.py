def alphabetical_value(word):
    """Returns the alphabetical value of a word.

    COLIN, colin = 3 + 15 + 12 + 9 + 14 = 53
    """

    answer = 0
    for letter in word:
        if 65 <= ord(letter) <= 90:     #if uppercase letter
            answer += ord(letter) - 64
        elif 97 <= ord(letter) <= 122:  #if lowercase letter
            answer += ord(letter) - 96
    return answer

if __name__ == "__main__":
    f = open('problem_022_names.txt')
    f_content = f.read()
    name_list = f_content.replace('"', '').split(',')
    name_list.sort()
    total = 0
    for i in range(len(name_list)):
        total += (i + 1) * alphabetical_value(name_list[i])
    print(total)
