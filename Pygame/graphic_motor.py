def color_grid(grid):

    color_grid = []

    for row in grid:

        color_row = []
        for item in row:
            color_row.append(item["color"])
        color_grid.append(color_row) 

    return color_grid