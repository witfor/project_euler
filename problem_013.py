if __name__ == "__main__":
    print(str(sum([int(x.rstrip()) for x in open('problem_013_data.txt')]))[:10])
