"""
FUNCTIONALITY
    Main handle of the elements of the project
1. Main event loop
2. Synchronisation of the code elements
"""

import pygame as pg
import sys
# Files importing
from Visual_end import *
from Physics_engine import *

# initialisation
pg.init()
window = pg.display.set_mode((1280, 720))
clock = pg.time.Clock()
dt = 0  # frame setup - animation
window.fill('black')


def animation_loop():
    position = pg.mouse.get_pos()
    ball = Objphysics(init_position=position)
    visual = Vector(ball, window, (10, 90))
    ground_not_touched = True
    while ground_not_touched:
        ball.new_pos = ball.gravity_stimulation(700)
        ground_not_touched = not ball.ground_touch(700)
        # window clear
        window.fill('black')
        ball.render_main(window)
        visual.vector_visual()
        pg.display.flip()
        # event handle
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        # limit frame rate
        clock.tick(60)


def control_setup():
    """
    functions
    1. objects spawning
    2. redo options
    3. details output - key
    :return: user _ control
    """
    keys = pg.key.get_pressed()
    if keys[pg.K_KP_ENTER]:
        animation_loop()
    elif keys[pg.K_SPACE]:
        print(f'Data set of object and system ')  # printing stack of info
    elif keys[pg.K_F1]:
        pass  # reset options


# MAIN LOOP - EXECUTION SYSTEM
run = True
while run:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    control_setup()  # making main user interactive
    pg.display.flip()
    dt = clock.tick(60) / 1000  # frame rate

pg.quit()
sys.exit()

