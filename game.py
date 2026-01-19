import json
import math
import os
import random

from cow import Cow
from food import Food
from person import Person
import matplotlib.pyplot as plt


class Game:

    def __init__(self, screen, w, h):
        self.generation = 0
        self.screen = screen
        self.w = w
        self.h = h
        self.persList = []
        self.foodList = []
        self.cowList = []
        self.stats = {}

    def loadVars(self):
        if os.path.getsize("game.json") == 0:

            x = random.randint(50, self.w - 50)
            y = random.randint(50, self.h - 50)
            vx = random.randint(1, 20) / 10
            vy = random.randint(1, 20) / 10
            speed = random.randint(1, 20) / 10
            vis = random.randint(50, 250)
            slfness = random.randint(0, 6)
            p1 = Person(self.screen, x, y, vx, vy, speed, vis, slfness)
            self.persList.append(p1)
            for i in range(5):
                x = random.randint(50, self.w - 50)
                y = random.randint(50, self.h - 50)
                f = Food(self.screen, x, y)
                self.foodList.append(f)
            self.stats = {

                "population": [1],
                "v_moy": [speed],
                "vision_moy": [vis],
                "selfishness": [slfness]

            }

        else:
            with open("game.json", 'r') as f:
                data = json.load(f)
                self.generation = data["generation"]
                persons = data["persons"]
                for p in persons:
                    newP = Person(self.screen, p['x'], p['y'], p['vx'], p['vy'], p['vitesse'], p['vision'], p['selfishness'])
                    self.persList.append(newP)
                f.close()

            for n in range(len(self.persList)):
                x = random.randint(50, self.w - 50)
                y = random.randint(50, self.h - 50)
                newfood = Food(self.screen, x, y)
                self.foodList.append(newfood)

            self.stats = data["stats"]


    def run(self):
        for elem in self.persList:
            if not elem.locked:
                elem.move()
            elem.check(self.foodList, self.cowList)
            elem.draw()

        for elem in self.foodList:
            elem.draw()

        for elem in self.cowList:
            elem.draw()

    def appendFood(self):
        nbPers = len(self.persList)
        for n in range(min(math.ceil(nbPers / 2), 40)):
            x = random.randint(50, self.w - 50)
            y = random.randint(50, self.h - 50)
            newfood = Food(self.screen, x, y)
            self.foodList.append(newfood)

        if nbPers >= 40:
            for i in range(min(math.ceil(nbPers / 10), 15)):
                x = random.randint(50, self.w - 50)
                y = random.randint(50, self.h - 50)
                newCow = Cow(self.screen, x, y)
                self.cowList.append(newCow)


    def endGen(self):
        newGen = []
        for p in self.persList:
            nbChild = (p.foodCounter // 3) - 1
            if nbChild >= 0:
                newGen.append(

                    {
                        "x": p.x,
                        "y": p.y,
                        "vx": p.vx,
                        "vy": p.vy,
                        "vitesse": p.vitesse,
                        "vision": p.vision,
                        "selfishness": p.selfishness
                    }

                )
                for i in range(nbChild):
                    x = random.randint(50, self.w - 50)
                    y = random.randint(50, self.h - 50)
                    vx = random.randint(1, 70) / 10
                    vy = random.randint(1, 70) / 10
                    speedChanger = random.randint(1, 100)
                    if speedChanger < 80:
                        speed = p.vitesse
                    elif 90 > speedChanger > 80:
                        speed = p.vitesse * (1 + (random.randint(1, 20) / 100))
                    else:
                        speed = p.vitesse * (1 - (random.randint(1, 20) / 100))

                    visionChanger = random.randint(1, 100)
                    if visionChanger < 80:
                        vision = p.vision
                    elif 90 > visionChanger > 80:
                        vision = p.vision * (1 + (random.randint(1, 20) / 100))
                    else:
                        vision = p.vision * (1 - (random.randint(1, 20) / 100))

                    selfishness = p.selfishness + random.randint(-1, 1)
                    if selfishness < 0:
                        selfishness = 0
                    elif selfishness > 6:
                        selfishness = 6

                    newGen.append(

                        {
                            "x": x,
                            "y": y,
                            "vx": vx,
                            "vy": vy,
                            "vitesse": speed,
                            "vision": vision,
                            "selfishness": selfishness
                        }

                    )

        speed_tot = 0
        vis_tot = 0
        self_tot = 0
        pop = len(newGen)
        for elem in newGen:
            speed_tot += elem["vitesse"]
            vis_tot += elem["vision"]
            self_tot += elem["selfishness"]

        self.stats["population"].append(pop)
        self.stats["v_moy"].append(speed_tot / pop)
        self.stats["vision_moy"].append(vis_tot / pop)
        self.stats["selfishness"].append(self_tot / pop)


        data = {

            "generation": self.generation + 1,
            "stats": self.stats,
            "persons": newGen,

        }

        with open("game.json", "w") as f:
            json.dump(data, f, indent=4)


    def showGraphs(self):
        # Evolution de la population
        names = [i for i in range(1, self.generation + 3)]
        values = self.stats["population"]
        plt.bar(names, values)
        plt.xlabel("Génération")
        plt.ylabel("Population")
        plt.savefig("result/evoPop.png")
        plt.clf()

        v_moy = [elem for elem in self.stats["v_moy"]]
        plt.plot(names, v_moy, color="orange")
        plt.xlabel("Génération")
        plt.ylabel("Vitesse Moyenne")
        plt.grid(True)
        plt.savefig("result/vitesse.png")
        plt.clf()

        vis_moy = [elem for elem in self.stats["vision_moy"]]
        plt.plot(names, vis_moy, color="blue")
        plt.grid(True)
        plt.xlabel("Génération")
        plt.ylabel("Vision Moyenne")
        plt.savefig("result/vision.png")
        plt.clf()

        vis_moy = [elem for elem in self.stats["selfishness"]]
        plt.plot(names, vis_moy, color="orange")
        plt.grid(True)
        plt.xlabel("Génération")
        plt.ylabel("Egoisme moyen (0 faible, 6 très fort)")
        plt.savefig("result/selfishness.png")
        plt.clf()

