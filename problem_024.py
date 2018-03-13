#Note: Implementation of lexicographic_permutations could be faster.
def lexicographic_permutations(input_list):
    """Returns a list of all the lexicographic permutations of the input_list.

    Function recursively finds all permutations of the input list,
    in lexicographic order.

    Example
    ----------
    > print(lexicographic_permutations([0, 1, 2]))
    [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    """

    if len(input_list) == 1:
        return input_list
    elif len(input_list) == 2:
        return [[input_list[0], input_list[1]], [input_list[1], input_list[0]]]
    else:
        output = []
        for i, item in enumerate(input_list):
            temp_list = input_list[:]
            temp_item = temp_list.pop(i)
            for temp_output in lexicographic_permutations(temp_list):
                output.append([temp_item] + temp_output)
        return output

if __name__ == "__main__":
    answer = lexicographic_permutations(list(range(10)))[999999]
    # Print answer as string.
    answer_str = ''
    for i in answer:
        answer_str += str(i)
    print(answer_str)
