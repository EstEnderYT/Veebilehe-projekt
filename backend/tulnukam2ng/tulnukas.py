import pygame
import pygame-web
import random

# tulnuka klass
class Alien():
  def __init__(self):
    self.hp = 1
    self.speed = 1
    self.dodge = 1
    self.alive = True
    self.damage = 1
    self.value = 10 #points
    self.pos = [0,0] #x,y
    self.body = None #pygame pic
    self.dodgetime = pygame.time.get_ticks()
    self.movetime = pygame.time.get_ticks()

  def Move(self):
    dodgetimer = pygame.time.get_ticks() - self.dodgetime
    movetimer = pygame.time.get_ticks() - self.movetime
    if dodgetimer >= 500: #500 ms
      self.pos[0] += random.choice([self.dodge, -(self.dodge)])
      self.dodgetime = pygame.time.get_ticks()
    if movetimer >= 1250: #1250 ms
      self.pos[1] += self.speed
      self.movetime = pygame.time.get_ticks()

class Shooter(Alien): #tulistaja tulnukas
  def __init__(self):
    super.__init__()

  def shoot(self):
    print("shoot")

class Invader(Shooter): #palju punkte
  def __init__(self):
    super.__init__()

class Mothership(Alien): #mingi suur punane asi mis oli
  def __init__(self):
    super.__init__()

class Shield(): #neli kilpi ees
  def __init__(self):
    pass

class Player(): #mängija info
  def __init__(self):
    pass

while True:
  pass
  #game while loop here
  #mtea päris space invader oli kinda igav, äkki kaks versiooni, üks on tavaline,
  #teist saab ainult siin knockoffis mängida, tulnukad liiguvad suvaliselt ringi, katsu neid kätte saada
    
