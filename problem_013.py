if __name__ == "__main__":
    filepath = 'problem_013_data.txt'
    print(str(sum([int(x.rstrip()) for x in open(filepath)]))[:10])
