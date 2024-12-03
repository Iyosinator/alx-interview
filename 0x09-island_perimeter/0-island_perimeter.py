def island_perimeter(grid):
    """
    Calculate the perimeter of an island in the grid.
    
    :param grid: List[List[int]] - 2D list representing the grid
    :return: int - perimeter of the island
    """
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                perimeter += 4

                if r > 0 and grid[r-1][c] == 1:
                    perimeter -= 2
                if c > 0 and grid[r][c-1] == 1:
                    perimeter -= 2

    return perimeter