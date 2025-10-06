"""create a function that takes in # and dash but replace dashes with digits
of mines immediately adjacent to mines"""


grid = ['-', '-', '-', '#', '#',
        '-', '#', '-', '-', '-',
        '-', '-', '#', '-', '-',
        '-', '#', '#', '-', '-',
        '-', '-', '-', '-', '-']


def count_adjacent_mines(grid):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 0), (0, 1),
                  (1, -1), (0, 0), (1, 1)]
    output_grid = [row[:] for row in grid]
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '-':
                count = 0

            for dr, dc in directions:
                r, c = rows + dr, cols + dc
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '#':
                    count += 1
                    output_grid[rows][cols] == str(count)
                    return output_grid

    output = count_adjacent_mines(grid)
    for rows in output:
        print(grid)
