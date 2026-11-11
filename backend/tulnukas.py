import pygame
from pygame.locals import *
#import pygame-web
import random

#pygame init
pygame.init()
Screen = pygame.display.set_mode((1000,700))
pygame.display.set_caption("Space Invaders")

#mängu algväärtused
Advance = 0
Points = 0
GameMode = "Base" #Base or Alternate
Sprites = pygame.sprite.Group() #kõik spraidid
Bullets = [] #kõik kuulid

# tulnuka klass
class Alien(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.hp = 1
        self.speed = 50
        self.dodge = 10
        self.alive = True
        self.damage = 1
        self.value = 10  # points

        self.image = pygame.Surface([40,40])
        #self.image.fill()
        pygame.draw.rect(self.image, (255,0,0), pygame.Rect(0,0,40,40))
        self.rect = self.image.get_rect()  # pygame pic

        self.dodgetime = pygame.time.get_ticks()
        self.movetime = pygame.time.get_ticks()
        self.direction = 1

    def AltMove(self): #possible alternate gamemode
        dodgetimer = pygame.time.get_ticks() - self.dodgetime
        movetimer = pygame.time.get_ticks() - self.movetime
        if dodgetimer >= 500:  # 500 ms
            self.rect.x += random.choice([self.dodge, -(self.dodge)])
            self.dodgetime = pygame.time.get_ticks()
        if movetimer >= 1250:  # 1250 ms
            self.rect.y += self.speed
            self.movetime = pygame.time.get_ticks()

    def BasicMove(self):
        dodgetimer = pygame.time.get_ticks() - self.dodgetime
        advancetimer = pygame.time.get_ticks() - self.movetime
        if dodgetimer >= 400:  # 0.4 s
            self.rect.x += self.dodge * self.direction
            self.dodgetime = pygame.time.get_ticks()
        if advancetimer >= 19600: # 20 s - 1 move
            self.rect.y += self.speed
            self.direction = self.direction * (-1)
            self.movetime = pygame.time.get_ticks()



class Shooter(Alien):  # tulistaja tulnukas
    def __init__(self):
        super().__init__()

    def shoot(self):
        print("shoot")


class Invader(Shooter):  # palju punkte
    def __init__(self):
        super().__init__()


class Mothership(Alien):  # mingi suur punane asi mis oli
    def __init__(self):
        super().__init__()


class Shield():  # neli kilpi ees
    def __init__(self):
        pass

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.speed = 3
        self.direction = direction
        self.image = pygame.Surface([5,20])
        pygame.draw.rect(self.image, (255,255,255), pygame.Rect(0,0,5,20))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

    def Move(self):
        self.rect.y += self.speed*self.direction
        if (self.rect.y <= -10) or (self.rect.y >= 710):
            self.kill()
    def Kill(self, aliens):
        for alien in aliens:
            if alien in Sprites:
                if self.rect.colliderect(alien.rect):
                    print("kill")
                    alien.kill()
                    self.kill()
                    break

class Player(pygame.sprite.Sprite):  # mängija info
    def __init__(self):
        super().__init__()
        self.hp = 3
        self.speed = 1
        self.reload = 300
        self.reloadtime = pygame.time.get_ticks()

        self.image = pygame.Surface([80,50])
        pygame.draw.rect(self.image, (0, 255, 0), pygame.Rect(0,0,80,50))
        self.rect = self.image.get_rect()
        self.rect.y = 620
        self.rect.x = 460

    def Move(self, direction):
        self.rect.x += self.speed * direction
        self.rect.x = max(min(910, self.rect.x), 10) # wery cool boundary thingy

    def Shoot(self):
        checkreload = pygame.time.get_ticks() - self.reloadtime
        if checkreload >= self.reload:
            bullet = Bullet(self.rect.x+40, self.rect.y, -1)
            Bullets.append(bullet)
            Sprites.add(bullet)
            self.reloadtime = pygame.time.get_ticks()

def BuildAttack(GameMode):
    aliens = []
    if GameMode == "Base":
        for i in range(5):
            for j in range(10):
                a = Alien()
                a.rect.x = 10 + (j*50)
                a.rect.y = 30 + (i*50)
                Sprites.add(a)
                aliens.append(a)
    return aliens

Aliens = BuildAttack("Base")
player = Player()
Sprites.add(player)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                player.Shoot()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.Move(-1)
    if keys[pygame.K_RIGHT]:
        player.Move(1)

    Screen.fill((0, 0, 0))

    Sprites.update()
    Sprites.draw(Screen)
    pygame.display.flip()

    for alien in Aliens:
        alien.BasicMove()
    for bullet in Bullets:
        if bullet in Sprites:
            bullet.Move()
            bullet.Kill(Aliens)

    # game while loop here
    # mtea päris space invader oli kinda igav, äkki kaks versiooni, üks on tavaline,
    # teist saab ainult siin knockoffis mängida, tulnukad liiguvad suvaliselt ringi, katsu neid kätte saada

