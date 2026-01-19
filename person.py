import pygame.draw
import math

from cow import Cow
from food import Food


class Person:

    def __init__(self, screen, x, y, vx, vy, vitesse, vision, selfishness):
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.vitesse = vitesse
        self.selfishness = selfishness
        self.color = (0, int(255 * (1 - self.selfishness / 6)), 0)
        self.rad = 20
        self.vision = vision
        self.foodCounter = 0
        self.targeting = False
        self.foodTarg = None
        self.locked = False


    def draw(self):
        #pygame.draw.circle(self.screen, (0, 0, 255), (self.x, self.y), self.vision, width=5)
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.rad)

    def move(self):
        if self.x <= 20 or self.x >= self.screen.get_width() - 20:
            self.vx = -self.vx
        if self.y <= 20 or self.y >= self.screen.get_height() - 20:
            self.vy = -self.vy

        self.x += self.vx * self.vitesse
        self.y += self.vy * self.vitesse


    def check(self, foodList, cowList):

        if self.foodTarg not in foodList:
            self.targeting = False

        if not self.targeting:
            # On charge tous les éléments dans le champ de vision
            inVision = [elem for elem in (foodList + cowList) if self.get_dist(elem.x, elem.y) < self.vision]

            if len(inVision) != 0:

                # On applique la fonction f qui retourne la distance entre le perso et chaque nourriture de inVision et on compare le min non pas par rapport à ce qu'il y a dans la liste mais par rapport aux resultats de la fonction et renvoie un élément de la liste
                food_min = min(inVision, key=lambda f: self.get_dist(f.x, f.y))
                pygame.draw.line(self.screen, (145, 212, 193), (self.x, self.y), (food_min.x, food_min.y))
                self.targeting = True
                dx = food_min.x - self.x
                dy = food_min.y - self.y
                dist = math.sqrt(dx ** 2 + dy ** 2)
                if dist != 0:
                    self.vx = (dx / dist) * self.vitesse
                    self.vy = (dy / dist) * self.vitesse
                else:
                    self.vx = dx * self.vitesse
                    self.vy = dy * self.vitesse



        for elem in (foodList + cowList):
            if self.get_dist(elem.x, elem.y) < self.rad:
                if isinstance(elem, Food):
                    foodList.remove(elem)
                    self.foodCounter += 1
                    self.targeting = False
                elif isinstance(elem, Cow):
                    if len(elem.playersOnIt) < 2 and self not in elem.playersOnIt:
                        elem.playersOnIt.append(self)
                        self.locked = True
                    elif len(elem.playersOnIt) == 2:
                        for player in elem.playersOnIt:
                            player.foodCounter += 1
                            player.locked = False
                        elem.eat()
                        cowList.remove(elem)




    def get_dist(self, x2, y2):
        return math.sqrt((self.x - x2)**2 + (self.y - y2)**2)