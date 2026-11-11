import pygame
from os import path
from math import pi as pi
from random import uniform

pygame.init()

aknaSuurus = (600, 650) #Pac-man on originaalselt ruudukujulisel aknal, kuid kõrguse suurendamine 50 piksli võrra lisab ruumi skoori ja muu jaoks.
aken = pygame.display.set_mode(aknaSuurus)
taimer = pygame.time.Clock()
font = pygame.font.Font(path.join(path.abspath(__file__), '..', '..', 'frontend', 'RETROTECH.ttf'), 30)
mäng = True

#Leveli maatriks, kus iga number tähistab erikujulisi seinu, tühjust ja muid vajalike paane.
level1 = [
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
[5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
[3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
[3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
[3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
]
seinaVärv = 'blue'
punktiVärv = 'white'

mängijaX = 300
mängijaY = 335

def joonistaLevel(level):

    paaniW = aknaSuurus[0] // 30 #Pac-mani paanide mõõdud on originaalselt 30x32 pikslit ja täisarvuline jagamine tagab, et iga paan joonistatakse täisarvulistel koordinaatidel.
    paaniH = (aknaSuurus[1] - 50) // 32 #Lahutame akna kõrgusest 50 pikslit, et säilitada leveli ruudu kuju.

    for i in range(len(level)):
        for j in range(len(level[i])):
                
                x = j * paaniW
                y = i * paaniH
                paaniXK = x + paaniW / 2 #Paani keskpunkti X-koordinaat.
                paaniYK = y + paaniH / 2 #Paani keskpunkti Y-koordinaat.
                paaniXR = x - paaniW / 2 #X-koordinaat kaare joonistamiseks paani sees.
                paaniYR = y - paaniH / 2 #Y-koordinaat kaare joonistamiseks paani sees.
                kraad90 = pi / 2
                kraad270 = pi * 3 / 2

                if level[i][j] == 1:
                    pygame.draw.circle(aken, punktiVärv, (paaniXK, paaniYK), 4) #Joonistab antud koordinaatidele ringi.
                elif level[i][j] == 2:
                    pygame.draw.circle(aken, punktiVärv, (paaniXK, paaniYK), 10)
                elif level[i][j] == 3:
                    pygame.draw.line(aken, seinaVärv, (paaniXK, y), (paaniXK, y + paaniH), 3) #Joonistab antud koordinaatide vahele joone.
                elif level[i][j] == 4:
                    pygame.draw.line(aken, seinaVärv, (x, paaniYK), (x + paaniW, paaniYK), 3)
                elif level[i][j] == 5:
                    pygame.draw.arc(aken, seinaVärv, (paaniXR, paaniYK, paaniW, paaniH), 0,  kraad90, 3) #Joonistab kaare antud radiaanide vahemikus. Kaar jääb sellise ristküliku sisse, millele on antud koordinaadid ning kõrguse ja laiuse väärtused.
                elif level[i][j] == 6:
                    pygame.draw.arc(aken, seinaVärv, (paaniXK, paaniYK, paaniW, paaniH), kraad90,  pi, 3)
                elif level[i][j] == 7:
                    pygame.draw.arc(aken, seinaVärv, (paaniXK, paaniYR, paaniW, paaniH), pi,  kraad270, 3)
                elif level[i][j] == 8:
                    pygame.draw.arc(aken, seinaVärv, (paaniXR, paaniYR, paaniW, paaniH), kraad270,  2 * pi, 3)
                elif level[i][j] == 9:
                    pygame.draw.line(aken, punktiVärv, (x, paaniYK), (x + paaniW, paaniYK), 3)

def joonistaMängija():

    auguSuurus = 3

    pygame.draw.circle(aken, 'yellow', (mängijaX, mängijaY), 15)
        
    for i in range(1, 4):
        pygame.draw.circle(aken, 'brown', (mängijaX + i * uniform(-auguSuurus, auguSuurus), mängijaY + i * uniform(-auguSuurus, auguSuurus)), auguSuurus)


while mäng:
    taimer.tick(30)
    aken.fill('black')
    joonistaLevel(level1)
    joonistaMängija()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mäng = False

    pygame.display.flip()

pygame.quit()