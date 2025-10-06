grid = [[0 for _ in range(4)] for _ in range(2)]
grid[0][1] = 7
for row in grid:
    print(row)


def create_grid(rows, cols, value):
    return [[value for _ in range(cols)] for _ in range(rows)]


grid = create_grid(2, 4, -1)
for row in grid:
    print(row)


def replace_in_grid(grid, row, col, new_value):
    grid[row][col] = new_value
    return grid


my_grid = create_grid(4, 4, 0)
new_grid = replace_in_grid(my_grid, 2, 3, 100)
for row in new_grid:
    print(row)
    print()


def build_and_replace(rows, cols, replacement):
    grid = [[0 for _ in range(cols)]for _ in range(rows)]
    grid[1][1] = replacement
    return grid


new_grid = build_and_replace(3, 3, "X")

for row in new_grid:
    print(row)
    print()
