import pygame
import random


def echo(s):
    print s


def run():
    pygame.init()

    screen = pygame.display.set_mode([300,100])
    screen.fill([255,255,255])

    mainloop, x, y, color, fontsize, delta, fps =  True, 25 , 0, (32,32,32), 35, 1, 30

    Clock = pygame.time.Clock()

    while mainloop:
        tickFPS = Clock.tick(fps)
        pygame.display.set_caption("Press Esc to quit. FPS: %.2f" % (Clock.get_fps()))
        fontsize = random.randint(35, 150)
        myFont = pygame.font.SysFont("None", fontsize)
        color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        screen.fill((255,255,255))
        screen.blit(myFont.render("PYGAME!", 0, (color)), (x,y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainloop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainloop = False
        pygame.display.update()

    pygame.quit()