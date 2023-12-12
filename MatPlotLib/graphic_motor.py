import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation
from grid_generator import generate_grid
from numpy import array
from cell_management import create_cell, evolute
import random

window_width, window_height = 1920, 992
square_size = 32
grid_width = int(window_width / square_size)
grid_height = int(window_height / square_size)

cellList = []
grid = generate_grid(grid_width, grid_height, square_size)
xInitPlant = random.randint(int(grid_width/3), 2 * int(grid_width/3))
create_cell(grid, xInitPlant, grid_height - 6, 25, 3, cellList)

showNoiseMap = False

def animate():
    def update(frame):
        # Update the data matrix for each frame (this is just an example update)

        cellNumber = len(cellList)
        print(cellNumber)
        for i in range(cellNumber):
            cell = cellList[i]
            evolute(grid, cell[1], cell[0], cellList)

        display_grid = color_grid(grid)

        newCellNumber = len(cellList)
        # Clear the previous plot
        ax.clear()

        # Display the updated data matrix as a colored grid
        img = ax.imshow(display_grid, cmap=cmap, extent=[0, columnas, filas, 0], origin="upper", interpolation='none')

        # Set title for each frame
        ax.set_title(f'Edad: {frame} ciclos',loc= "left")
        ax.set_title(f'Tamaño: {len(cellList)}',loc= "center")
        ax.set_title(f'Factor: {round((newCellNumber - cellNumber) / (cellNumber), 4)}',loc= "right")

    # Set the number of rows and columns
    filas = 31
    columnas = 60

    # Define a colormap with discrete values
    cmap = ListedColormap(['sienna', 'deepskyblue', 'yellow', "darkgreen", "lime", "magenta", "firebrick"])

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create the animation
    animation = FuncAnimation(fig, update, frames=2000, interval=1500, repeat=False)

    # Show the plot
    plt.show()


def color_grid(grid):

    colors = []

    for row in grid:
        for item in row:
            colors.append(item["color"])

    colors[0]=0 
    colors[1]=1
    colors[2]=2
    colors[3]=3
    colors[4]=4
    colors[5]=5
    colors[6]=6

    colors_array = array(colors)
    colors_grid = colors_array.reshape(31,60)

    return colors_grid
    
# Example: Input a 2x2 matrix with discrete values
animate()