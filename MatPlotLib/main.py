# Importa el motor gráfico y el motor de cálculo
from calc_motor import start_motor, update_motor
from graphic_motor import animate

#Establece las variables del tamaño de la cuadrícula para que se ajuste en pantalla completa a 1920x992 píxeles.
window_width, window_height = 1920, 992
square_size = 32
grid_width = int(window_width / square_size)
grid_height = int(window_height / square_size)

# Inicializa el motor de cálculo para que se ajuste a las dimensiones deseadas.
grid, cellList = start_motor (grid_width, grid_height)

# Anima mediante el motor gráfico las actualizaciones obtenidas del motor de cálculo con los parámetros de pantalla establecidos.
animate(update_motor, grid, cellList, grid_width, grid_height)

