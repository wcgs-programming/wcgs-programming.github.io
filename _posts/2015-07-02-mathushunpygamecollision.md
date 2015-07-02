---
title: "Pygame Collision with Levels"
layout: post
published: true
categories: showcase mathushun
---

> Using his Python skills and the pygame module, Mathushun has created a collsion game with over 1000 levels!
> You can download it [here](/files/showcase/Mathushun/pygame-collision.zip). You will need to download pygame too though which you can find in resources [here](/resources/python/).

> You can see it below:

	import pygame, sys
	from pygame.locals import *
	import random

	IMG = pygame.image.load('key_sprite.png')
	ICON = pygame.transform.scale(IMG,(30,30))
	FPS = 50
	WINDOWWIDTH = 640
	WINDOWHEIGHT = 480
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	BLUE = (0, 102, 204)
	GREEN = (0, 255, 0)
	RED = (204, 0, 0)
	YELLOW = (255, 255, 0)
	RED = (232,18,18)
	PURPLE = (102, 0, 102)
	UP = 'up'
	DOWN = 'down'
	LEFT = 'left'
	RIGHT = 'right'
	NW = 'northwest'
	NE = 'northeast'
	SE = 'southeast'
	SW = 'southwest'
	def main():
		global FPSCLOCK, DISPLAYSURF, BASICFONT
		pygame.init()
		FPSCLOCK = pygame.time.Clock()
		DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
		BASICFONT = pygame.font.Font(None, 25)
		pygame.display.set_icon(ICON)
		pygame.display.set_caption("Collision!")
		showstartscreen()
		while True:
			runGame()
	def runGame():
		TEXTSTRING = "LEVEL "
		BACKGROUNDCOLOR = BLUE
		TEXT1X = 300
		TEXT1Y = 10
		Xcoord = 300
		Ycoord = 300
		RANXCOORD = random.randint(50,500)
		RANYCOORD = random.randint(50,450)
		DIRECTION = RIGHT
		LEVEL = 1
		SPEED = 10
		COLLISION = 0
		TEXT2COLOUR = BLUE
		while True:
			for event in pygame.event.get():
				if event.type == QUIT:
					TERMINATE()
				elif event.type == KEYDOWN:
					if (event.key == K_UP):
						 DIRECTION = UP
					elif (event.key == K_DOWN):
						 DIRECTION = DOWN
					elif (event.key == K_LEFT):
						 DIRECTION = LEFT
					elif (event.key == K_RIGHT):
						 DIRECTION = RIGHT
					elif (event.key == K_w):
						 DIRECTION = NW
					elif (event.key == K_a):
						 DIRECTION = NE
					elif (event.key == K_s):
						 DIRECTION = SE
					elif (event.key == K_d):
						 DIRECTION = SW
					elif (event.key == K_q):
						 runGame()
					elif (event.key == K_ESCAPE):
						 TERMINATE()
			if (DIRECTION == UP):
				Ycoord-=SPEED
			elif (DIRECTION == DOWN):
				Ycoord+=SPEED
			elif (DIRECTION == LEFT):
				Xcoord-=SPEED
			elif (DIRECTION == RIGHT):    
				Xcoord+=SPEED
			elif (DIRECTION == NW):
				Ycoord-=SPEED  
				Xcoord-=SPEED
			elif (DIRECTION == NE):
				Ycoord-=SPEED  
				Xcoord+=SPEED
			elif(DIRECTION == SE):
				Ycoord+=SPEED  
				Xcoord-=SPEED
			elif (DIRECTION == SW):
				Ycoord+=SPEED  
				Xcoord+=SPEED
			if(Xcoord<0):
				Xcoord = abs(Xcoord)
				SPEED = 0
				TEXTSTRING = "COLLISION!!! YOUR SCORE WAS "
				TEXT1X = 200
				TEXT1Y = 10
				TEXT2COLOUR = YELLOW
			elif(Xcoord>WINDOWWIDTH-20):
				Xcoord = WINDOWWIDTH - (Xcoord - WINDOWWIDTH)-20
				SPEED = 0
				TEXTSTRING = "COLLISION!!! YOUR SCORE WAS "                
				TEXT1X = 200
				TEXT1Y = 10
				TEXT2COLOUR = YELLOW
			if(Ycoord<0):
				Ycoord = abs(Ycoord)
				SPEED = 0
				TEXTSTRING = "COLLISION!!! YOUR SCORE WAS "
				TEXT1X = 200
				TEXT1Y = 10
				TEXT2COLOUR = YELLOW
			elif(Ycoord>WINDOWHEIGHT-20):
				Ycoord = WINDOWHEIGHT - (Ycoord - WINDOWHEIGHT)-20
				SPEED = 0
				TEXTSTRING = "COLLISION!!! YOUR SCORE WAS "
				TEXT1X = 200
				TEXT1Y = 10
				TEXT2COLOUR = YELLOW
			if(Xcoord >= RANXCOORD and Ycoord >= RANYCOORD) and (Xcoord <= RANXCOORD+50 and Ycoord <= RANYCOORD+32):
				COLLISION = 1
			if (COLLISION == 1):
				Xcoord = 320
				Ycoord = 240
				LEVEL = LEVEL + 1
				RANXCOORD = randplacex()
				RANYCOORD = randplacey()
				COLLISION = 0
				if(LEVEL >= 10):
					BACKGROUNDCOLOR = PURPLE
					TEXT2COLOUR = PURPLE
					SPEED = 12
				if(LEVEL >= 20):
					BACKGROUNDCOLOR = GREEN
					TEXT2COLOUR = GREEN
					SPEED = 14
				if(LEVEL >= 30):
					BACKGROUNDCOLOR = RED
					TEXT2COLOUR = RED
					SPEED = 16
				if(LEVEL >= 40):
					BACKGROUNDCOLOR = BLACK
					TEXT2COLOUR = BLACK
					SPEED = 18
				if(LEVEL >= 50):
					BACKGROUNDCOLOR = WHITE
					TEXT2COLOUR = WHITE
					SPEED = 20
				if(LEVEL >= 100):
					SPEED = 30
				if(LEVEL >= 200):
					SPEED = 40
				if(LEVEL >= 300):
					SPEED = 42
				if(LEVEL >= 400):
					SPEED = 44
				if(LEVEL >= 500):
					SPEED = 46
				if(LEVEL >= 600):
					SPEED = 48
				if(LEVEL >= 700):
					SPEED = 50
				if(LEVEL >= 1000):
					SPEED = 52    
			#Level code here
			DISPLAYSURF.fill(BACKGROUNDCOLOR)
			DISPLAYSURF.blit(IMG,(RANXCOORD,RANYCOORD))
			TEXT1 = BASICFONT.render(TEXTSTRING + str(LEVEL),True,YELLOW)
			TEXT1C = TEXT1.get_rect()
			TEXT1C.topleft = (TEXT1X,TEXT1Y)
			DISPLAYSURF.blit(TEXT1,TEXT1C)
			TEXT2 = BASICFONT.render("PRESS Q TO START AGAIN!",True,TEXT2COLOUR)
			TEXT2C = TEXT2.get_rect()
			TEXT2C.topleft = (225,50)
			DISPLAYSURF.blit(TEXT2,TEXT2C)
			#Draw code here
			pygame.draw.circle(DISPLAYSURF,YELLOW,(Xcoord,Ycoord),20)
			pygame.display.update()
			pygame.display.flip()
			FPSCLOCK.tick(FPS)
			
	def TERMINATE():
		pygame.quit()
		sys.exit()
	def randplacex():
		x = random.randint(50,500)
		return x
	def randplacey():
		y= random.randint(50,450)
		return y
	def showstartscreen():
		DISPLAYSURF.fill(BLUE)
		pygame.display.update()
		pygame.display.flip()
		FPSCLOCK.tick(FPS)
	main()
