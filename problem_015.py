def lattice_paths(n, m):
    """Returns number of lattice paths in n * m grid.

    Parameters
    ----------
    n: number of rows
    m: number of columns

    Output
    ----------
    Number of paths from top left corner to bottom right corner along
    edges in n * m grid.

    Example
    ----------
    > lattice_paths(2, 2)
    6

    Notes
    ----------
    Solution achieved with dynamic programming.
    """

    list = [1] + [0 for i in range(m)]
    for x in range(n + 1):
        for y in range(1, m + 1):
            list[y] += list[y - 1]
    return list[-1]

if __name__ == "__main__":
    print(lattice_paths(20, 20))
