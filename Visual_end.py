"""
Functionality  - handling visual end
visual control
    1. vector visual class
    2. object controls mode
    3. Animation control system
"""
import pygame as pg
import math
pg.init()


class Vector:
    """
    functions
    1. vectors visuals representation
    2. Angle transforming animations
    3. physics engine integration socket
    """
    def __init__(self, target_object, window, vector_data=(1, 0)):
        self.element_window = window
        self.target_object = target_object
        self.vector_info = vector_data  # engine output -> vector_info > dataform magnitude and directions

    def vector_visual(self):
        # vectors body creation
        op = self.target_object.rect.center
        x = op[0] + math.cos(math.radians(self.vector_info[1])) * self.vector_info[0]
        y = op[1] + math.sin(math.radians(self.vector_info[1])) * self.vector_info[0]

        # head of vector
        tip = pg.Vector2((x, y))
        v1 = (
            tip.x + math.cos(math.radians(self.vector_info[1] - 150)) * self.vector_info[0],
            tip.y + math.sin(math.radians(self.vector_info[1] - 150)) * self.vector_info[0]
        )
        v2 = (
            tip.x + math.cos(math.radians(self.vector_info[1] + 150)) * self.vector_info[0],
            tip.y + math.sin(math.radians(self.vector_info[1] + 150)) * self.vector_info[0]
        )
        pg.draw.line(self.element_window, 'white', op, (x, y), 2)
        pg.draw.polygon(self.element_window, 'red', [tip, v1, v2])

