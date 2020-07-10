import os
import sys
import time
import pygame

BLACK = [0,0,0]
WHITE = [255,255,255]
BLUE = [0,0,255]
GREEN = [0,255,0]

SIZE = [640,480]

pygame.init()
screen = pygame.display.set_mode(SIZE)

# square1 = pygame.Surface([40,40])
# square1.fill(GREEN)
# x1,y1 = 320,240

pygame.key.set_repeat(1,1)
playing = True
while playing:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type == pygame.KEYDOWN:
			# #PLAYER 1 CONTROLS
			# if event.key == pygame.K_w:
			# 	y1-=1
			# if event.key == pygame.K_a:
			# 	x1-=1
			# if event.key == pygame.K_s:
			# 	y1+=1
			# if event.key == pygame.K_d:
			# 	x1+=1
			pass


	screen.fill(BLACK)
	screen.blit(square1, [x1,y1])

	pygame.display.flip()
	pygame.time.delay(20)

