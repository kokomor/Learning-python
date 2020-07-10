import os
import sys
import time
from random import *
import pygame

BLACK = [0,0,0]
WHITE = [255,255,255]
BLUE = [0,0,255]
GREEN = [0,255,0]
YELLOW = [255,255,102]

SIZE = [640,480]

pygame.init()
screen = pygame.display.set_mode(SIZE)

class Player(object):
	def __init__(self, color):
		#ЦВЕТ и POVERHNOST'
		self.surf = pygame.Surface([40,40])
		self.surf.fill(color)
		self.x = 100
		self.y = 100
	def draw(self):
		screen.blit(self.surf,[self.x,self.y])

class Bullet(object):
	def __init__(self, x, y, color):
		#ЦВЕТ и POVERHNOST'
		self.surf = pygame.Surface([10,10])
		self.surf.fill(color)
		self.x = x
		self.y = y
		self.vecX = 0
		self.vecY = 0
		#НАПРАВЛЕНИЕ ВЫСТРЕЛА
		self.move = False
	def draw(self):
		if self.move:
			self.x+=self.vecX
			self.y+=self.vecY
		screen.blit(self.surf,[self.x,self.y])



player = Player(GREEN)

allbullets = []
allbullets.append(Bullet(120,120,YELLOW))

pygame.key.set_repeat(1,1)
playing = True
while playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			# #PLAYER 1 CONTROLS
			if event.key == pygame.K_w:
				player.y-=1
			if event.key == pygame.K_a:
				player.x-=1
			if event.key == pygame.K_s:
				player.y+=1
			if event.key == pygame.K_d:
				player.x+=1
			if event.key == pygame.K_RIGHT:
				bul = Bullet(player.x,player.y,YELLOW)
				bul.vecX = 1
				bul.move = True
				allbullets.append(bul)
			if event.key == pygame.K_DOWN:
				bul = Bullet(player.x,player.y,YELLOW)
				bul.vecY = 1
				bul.move = True
				allbullets.append(bul)
			if event.key == pygame.K_LEFT:
				bul = Bullet(player.x,player.y,YELLOW)
				bul.vecX = -1
				bul.move = True
				allbullets.append(bul)
			if event.key == pygame.K_UP:
				bul = Bullet(player.x,player.y,YELLOW)
				bul.vecY = -1
				bul.move = True
				allbullets.append(bul)




	screen.fill(BLACK)
	player.draw()
	for bullet in allbullets:
		bullet.draw()

	pygame.display.flip()
	pygame.time.delay(20)

