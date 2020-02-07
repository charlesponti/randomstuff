grid = [
    [True, True, True, True],
    [True, False, True, True],
    [True, True, False, True],
    [False, True, True, True],
]


def valid_square(grid, row, col):
    return grid[row][col]


def is_at_end(grid, row, col):
    return row >= (len(grid) - 1) and col >= (len(grid[row]) - 1)


def count_paths(grid: list, row: int, col: int):
    if is_at_end(grid, row, col):
        return 1

    if not valid_square(grid, row, col):
        return 0

    return count_paths(grid, row + 1, col) + count_paths(grid, row, col + 1)


print(count_paths(grid, 0, 0))
