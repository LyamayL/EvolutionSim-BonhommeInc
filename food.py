import pygame


class Food:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = (255, 0, 0)
        self.rad = 15

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.rad)