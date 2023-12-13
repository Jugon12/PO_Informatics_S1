# Importa las librerias gráficas de matplotlib y la función array.
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib.animation import FuncAnimation

from numpy import array



# Adapta los datos del motor de cálculo para ser procesables por el motor gráfico.
def color_grid(grid, width, height): 

    # Añade todos el color de cada celda a la nueva lista.
    colors = []
    for row in grid:
        for item in row:
            colors.append(item["color"])

    # Crea la banda de patrón de colores.
    for i in range(0, 7): 
        colors[i] = i

    # Redimensiona la lista para devolver una matriz (Formato de input necesario para matplotlib)
    colors_array = array(colors)
    colors_grid = colors_array.reshape(height, width)

    return colors_grid



# Procesa todo el código del motor gráfico.
def animate(update_motor, grid, cellList, width, height):

    def update(frame): # Procesa el código de la función en cada frame

        # Procesa todo el motor de cálculo
        updatedGrid, cellNumber, newCellNumber = update_motor(grid, cellList) 

        # Adapta el resultado del motor de cálculo para ser interpretable por el motor gráfico
        display_grid = color_grid(updatedGrid, width, height) 


        # Limpia el gráfico anterior
        ax.clear()

        # Procesa los datos para generar la imagen
        img = ax.imshow(display_grid, cmap=cmap, extent=[0, width, height, 0], origin="upper", interpolation='none')

        # Establece las estadísticas en pantalla
        ax.set_title(f'Edad: {frame} ciclos',loc= "left")
        ax.set_title(f'Tamaño: {len(cellList)}',loc= "center")
        ax.set_title(f'% Crecimiento: {round((newCellNumber - cellNumber) * 100 / (cellNumber), 3)}',loc= "right")

    # Establece los colores usados en el programa. Este corresponderá con el índice usado en esta lista.
    cmap = ListedColormap(['sienna', 'deepskyblue', 'yellow', "darkgreen", "lime", "magenta", "firebrick"])

    # Establece los ejees y la figura del gráfico
    fig, ax = plt.subplots()

    #Crea la animación
    animation = FuncAnimation(fig, update, frames=2000, interval=1500, repeat=False)

    # Muestra el gráfico
    plt.show()