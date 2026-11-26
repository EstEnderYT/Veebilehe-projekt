import asyncio
import pygame
from os import path

pygame.init()

aken = pygame.display.set_mode((600, 650))
taimer = pygame.time.Clock()
font = pygame.font.Font(path.join(path.dirname(path.abspath(__file__)), 'RETROTECH.ttf'), 30)

async def main():

    mäng = True

    while mäng:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mäng = False

        aken.fill('black')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mäng = False
        pygame.display.flip()

        await asyncio.sleep(0)
        taimer.tick(30)

    pygame.quit()

asyncio.run(main())