import math
import pygame as pg


class Objphysics:
    def __init__(self, mass=5, init_position=(200, 200)):
        self.mass = mass
        self.init_position = init_position
        self.u = 0
        self.v = 0
        self.s = 0
        self.rect = pg.Rect(init_position, (10, 10))
        self.new_pos = 0

    def gravity_stimulation(self, ground_ref):
        """
        f : v = sqrt(u**2 + 2*a*s)
        :return: new_position --> the updated position of the object
        """
        self.s = ground_ref - self.init_position[1]  # Distance to the ground
        a = 10  # Acceleration due to gravity (you might want to adjust this value)
        self.v = math.sqrt(self.u**2 + 2 * a * self.s)
        self.s = self.s - self.v
        self.u = self.v

        new_position = self.init_position[1] + self.v  # Update position
        return new_position

    def reset(self):
        self.u = 0
        self.v = 0
        self.s = 0

    def render_main(self, screen):
        self.new_pos = self.gravity_stimulation(700)  # Assuming 700 is the ground reference height
        self.rect.center = (self.init_position[0], self.new_pos)
        pg.draw.circle(screen, 'red', self.rect.center, 20)

    def ground_touch(self, grnd_ref):
        if grnd_ref < self.new_pos:
            return True
        else:
            return False
