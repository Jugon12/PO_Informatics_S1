# Reduce el valor del sol debajo de una célula cuando se crea.
def reduce_sun(grid, x, y):
    
    for y_pos in range(y, len(grid)):
        if grid[y_pos][x]["sun"] is not 0:
            grid[y_pos][x]["sun"] -= 1 
