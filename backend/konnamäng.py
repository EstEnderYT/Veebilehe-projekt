import pygame
import os

pygame.init()

aken = pygame.display.set_mode((600, 650))
taimer = pygame.time.Clock()
font = pygame.font.Font(os.path.join(os.path.abspath(__file__), '..', '..', 'frontend', 'RETROTECH.ttf'), 30)
mäng = True

while mäng:
    taimer.tick(30)
    aken.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mäng = False

    pygame.display.flip()

pygame.quit()