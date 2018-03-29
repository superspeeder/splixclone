import pygame
from pygame.locals import *

import sprites
import multiplayer
import map


MAP = map.map1
screen = pygame.display.set_mode(MAP.size)


screen.blit(MAP.surf)
player = sprites.Player.spawn()
player_g = pygame.sprite.GroupSingle(player)


while 1:
  for event in pygame.event.get():
    if event.type == QUIT:
      exit()
  
  keys_pressed = pygame.key.get_pressed()
  if keys_pressed[K_UP]:
    player.move("up")
  if keys_pressed[K_RIGHT]:
    player.move("right")
  if keys_pressed[K_DOWN]:
    player.move("down")
  if keys_pressed[K_LEFT]:
    player.move("left")
   
  screen.blit(MAP.surf)
  player_g.draw(screen)
  pygame.display.update()
