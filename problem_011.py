def greatestProduct(list_of_lists, n):
    """Main procedure.

    Iterates through list_of_lists and returns the greatest product
    of n adjacent numbers in the same direction (up, down, left, right, or
    diagonal.)
    """
    
    greatest_product = 0
    for i in range(len(list_of_lists)):
        for j in range(len(list_of_lists[i])):
            greatest_product = max(greatest_product,
                                    horizontalProduct(list_of_lists, i, j, n),
                                    verticalProduct(list_of_lists, i, j, n),
                                    diagonalProductRight(list_of_lists, i, j, n),
                                    diagonalProductLeft(list_of_lists, i, j, n)
                                    )
    return greatest_product

def horizontalProduct(list_of_lists, x, y, n):
    answer = 1
    try:
        for i in range(4):
            answer *= list_of_lists[x][y+i]
        return answer
    except IndexError:
        return 0

def verticalProduct(list_of_lists, x, y, n):
    answer = 1
    try:
        for i in range(4):
            answer *= list_of_lists[x+i][y]
            return answer
    except IndexError:
        return 0

def diagonalProductRight(list_of_lists, x, y, n):
    answer = 1
    try:
        for i in range(4):
            answer *= list_of_lists[x+i][y+i]
        return answer
    except IndexError:
        return 0

def diagonalProductLeft(list_of_lists, x, y, n):
    answer = 1
    try:
        for i in range(4):
            answer *= list_of_lists[x+i][y-i]
        return answer
    except IndexError:
        return 0

def importData(filepath):
    "Import the grid data and cleans it into a nested list of lists."

    lines = [x.rstrip().split(' ') for x in open(filepath)]
    integer_lines = []
    for line in lines:
        new_line = []
        for i in range(len(line)):
            new_line.append(int(line[i]))
        integer_lines.append(new_line)
    return integer_lines

if __name__ == "__main__":
    print(greatestProduct(importData('problem_011_data.txt'), 4))
