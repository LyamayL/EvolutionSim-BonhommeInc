import pygame

class Cow:

    def __init__(self, screen, x, y):
        self.screen = screen
        self.x = x
        self.y = y
        self.color = (137, 81, 41)
        self.rad = 15
        self.playersOnIt = []

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.rad)

    def eat(self):
        # Cas 1 : le partage est parfait:
        p1 = self.playersOnIt[0]
        p2 = self.playersOnIt[1]
        if p1.selfishness + p2.selfishness == 6:
            p1.foodCounter += p1.selfishness
            p2.foodCounter += p2.selfishness
        elif p1.selfishness + p2.selfishness < 6:
            p1.foodCounter += p1.selfishness
            p2.foodCounter += p2.selfishness
            reste = 6 - (p1.selfishness + p2.selfishness)
            if reste % 2 == 0:
                p1.foodCounter += reste // 2
                p2.foodCounter += reste // 2
            else:
                if p1.foodCounter >= p2.foodCounter:
                    p1.foodCounter += reste // 2 + reste % 2
                    p2.foodCounter += reste // 2
                else:
                    p2.foodCounter += reste // 2 + reste % 2
                    p1.foodCounter += reste // 2
        else:
            inter = (p1.selfishness + p2.selfishness) - 6
            reste = 6 - inter - 2 # -2 pour le cout énergétique engendré
            if reste % 2 == 0:
                p1.foodCounter += reste // 2
                p2.foodCounter += reste // 2
            else:
                if p1.foodCounter >= p2.foodCounter:
                    p1.foodCounter += reste // 2 + reste % 2
                    p2.foodCounter += reste // 2
