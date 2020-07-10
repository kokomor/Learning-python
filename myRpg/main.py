import os
import sys
import time
import pygame
from pygame import *

BLACK = [0,0,0]
WHITE = [255,255,255]
BLUE = [0,0,255]
GREEN = [0,255,0]
DARKGREEN = [89,194,53]

SIZE = [640,480]

pygame.init()
screen = pygame.display.set_mode(SIZE)

CHARACTERS =  pygame.image.load("sprites/characters.png")


class GameObject(object):
	def __init__(self, atlas, tx, ty, w, h):
		#ЦВЕТ и POVERHNOST'
		self.img = pygame.image.load("sprites/"+atlas+".png").subsurface(Rect(tx*w,ty*h,w,h))
		self.x = 100
		self.y = 100
	def draw(self):
		screen.blit(self.img,[self.x,self.y])
hero = GameObject("characters", 6, 1, 32, 32)
steps= GameObject("grass" ,1, 1, 16, 16)
transform.scale2x(steps.img)

allSteps = []
stepTicks = 0
stepTicksRate = 16

pygame.key.set_repeat(1,1)
playing = True
while playing:
	screen.fill(DARKGREEN)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			#PLAYER 1 CONTROLS
			if event.key == pygame.K_w:
				hero.y-=1
			if event.key == pygame.K_a:
				hero.x-=1
			if event.key == pygame.K_s:
				hero.y+=1
			if event.key == pygame.K_d:
				hero.x+=1
			if event.key in [K_w,K_a,K_s,K_d]:
				stepTicks+=1
				if stepTicks>=stepTicksRate:
					stepTicks = 0
					newSteps = GameObject("grass",1,1,16,16)
					newSteps.x = hero.x+8
					newSteps.y = hero.y+24
					allSteps.append(newSteps)



	for step in allSteps:
		step.draw()
	hero.draw()

	pygame.display.flip()
	pygame.time.delay(20)