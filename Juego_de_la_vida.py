import pygame
import numpy as np
import matplotlib.pyplot as plt
import  time

pygame.init()
size = width, height = 600, 600

bg = 25, 25, 25

nx_cell = 30
ny_cell = 30

nx_size = (width) / nx_cell
ny_size = (height) / ny_cell


screen = pygame.display.set_mode(size)

screen.fill(bg)

state_game = np.random.randint(0, 1, (nx_cell, ny_cell))




state_game[21, 21] = 1
state_game[22, 22] = 1
state_game[22, 23] = 1
state_game[21, 23] = 1
state_game[20, 23] = 1


# state_game[21, 19] = 1
# state_game[21, 20] = 1
# state_game[21, 21] = 1

print(state_game)
plt.matshow(state_game)
'''

plt.imshow(state_game)
ax = plt.gca()
ax.set_xticks(np.arange(0, ny_cell, 1))  # cortes del eje x
ax.set_yticks(np.arange(0, nx_cell, 1))  # cortes del eje y
ax.set_xticklabels(np.arange(0, ny_cell, 1))  # etiquetas del eje x
ax.set_yticklabels(np.arange(0, nx_cell, 1))  # etiquetas del eje y
# Minor ticks
ax.set_xticks(np.arange(-.5, ny_cell, 1), minor=True)  # lineas horizontales
ax.set_yticks(np.arange(-.5, nx_cell, 1), minor=True)  # lineas verticales

# Gridlines based on minor ticks
ax.grid(which='minor', color='w', linestyle='-', linewidth=2)
'''

# plt.show()

# Variable para pausar el juego

PausaGame = False


while True:

    new_state_game = np.copy(state_game)
    screen.fill(bg)
    time.sleep(0.1)

    # Capturar eventos del teclado y raton

    ev = pygame.event.get()

    # print(pygame.KEYDOWN)

    for event in ev:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                break

            else:
                PausaGame = not PausaGame

        mouseClick = pygame.mouse.get_pressed()
        # print(mouseClick)

        if sum(mouseClick)> 0:
            posX, posY = pygame.mouse.get_pos()
            celdaX, celdaY = int(np.floor(posX/nx_size)), int(np.floor(posY/ny_size))
            new_state_game[celdaX, celdaY] = not mouseClick[2]


    for x in range(0, nx_cell):
        for y in range(0, ny_cell):

            if not PausaGame:
                n_vecinos = state_game[(x-1) % nx_cell, (y-1) % ny_cell ] + \
                            state_game[x % nx_cell, (y - 1) % ny_cell] + \
                            state_game[(x + 1) % nx_cell, (y - 1) % ny_cell] + \
                            state_game[(x - 1) % nx_cell, y % ny_cell] + \
                            state_game[(x + 1) % nx_cell, y % ny_cell] + \
                            state_game[(x - 1) % nx_cell, (y + 1) % ny_cell] + \
                            state_game[x % nx_cell, (y + 1) % ny_cell] + \
                            state_game[(x + 1) % nx_cell, (y + 1) % ny_cell] \

                #print(n_vecinos)

                # Una célula muerta con exactamente 3 células vecinas vivas "nace" (es decir, al turno siguiente estará viva)

                if state_game[x, y] == 0 and n_vecinos == 3:
                    new_state_game[x, y] = 1
                elif state_game[x, y] == 1 and (n_vecinos < 2 or n_vecinos > 3):
                    new_state_game[x, y] = 0

            poligonos = [((x) * nx_size, (y) * nx_size),
                         ((x+1) * nx_size, (y) * nx_size),
                         ((x+1)  * nx_size, (y+1) * ny_size),
                         ((x) * nx_size, (y+1) * ny_size)]  #coordenadas de los cuadros que crean la malla

            pygame.draw.polygon(screen, (128, 128, 128), poligonos, int(abs(1-new_state_game[x,y])))

    # Se actualiza el estado del juego
    state_game = np.copy( new_state_game)
    # plt.matshow(state_game)
    # plt.show()
    pygame.display.flip()

# fin del programa