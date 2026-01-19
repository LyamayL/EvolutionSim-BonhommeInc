import math
import pygame
from game import Game
import time

W = 2750
H = 1600

def loop():
    global W
    global H
    pygame.init()
    screen = pygame.display.set_mode((W, H))
    g = Game(screen, W, H)
    g.loadVars()
    pygame.display.set_caption("Génération n°" + str(g.generation))
    font = pygame.font.Font(None, 36)

    SPAWN_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_EVENT, 5000)

    clock = pygame.time.Clock()
    running = True

    t1 = time.time()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == SPAWN_EVENT:
                g.appendFood()

        # fill the screen with a color to wipe away anything from last frame
        screen.fill((255, 255, 255))

        t2 = time.time()
        tot = math.floor(t2 - t1)

        texte = font.render(str(tot), True, (0, 0, 0))

        g.run()

        screen.blit(texte, (200, 180))

        pygame.display.flip()
        clock.tick(200)  # limits FPS to 60

        if tot >= 60:
            running = False


    g.endGen()
    g.showGraphs()
    pygame.quit()

nbGen = int(input('Entrez le nombre de génération a effectuer avant d\'arrêter : '))

for i in range(nbGen):
    print("Génération n°" + str(i + 1) + "/" + str(nbGen))
    loop()