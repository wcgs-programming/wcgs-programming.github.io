---
title: "Pygame Ball with Levels"
layout: post
published: true
categories: showcase killian
---

> Using his Python skills and the pygame module, Killian has created a ball game with levels.
> You can download it [here](/files/showcase/Killian/pygame-ball.zip). You will need to download pygame too though which you can find in resources [here](resources/python/).

> You can see it below:

	import pygame, sys
	from pygame.locals import *
	import random
	img = pygame.image.load('key.png')
	FPS = 20
	WINDOWWIDTH = 640
	WINDOWHEIGHT = 480
	WHITE = (255, 255, 255)
	BLACK = (0, 0, 0)
	BLUE = (0, 0, 255)
	RED = (255, 0, 0)
	UP = 'up'
	DOWN = 'down'
	LEFT = 'left'
	RIGHT = 'right'
	NW = 'northwest'
	NE = 'northeast'
	SW = 'southwest'
	SE = 'southeast'
	def main():
		global FPSCLOCK, DISPLAYSURF, BASICFONT, KEYX, KEYY
		pygame.init()
		#KEYY = random.randint(0, 480)
		#KEYX = random.randint(0, 640)
		FPSCLOCK = pygame.time.Clock()
		DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
		BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
		pygame.display.set_caption('Hello World')
		showstartscreen()
		while True:
			runGame()
		
	def runGame():
		Xcoord = 300
		Ycoord = 300
		xcoord2 = 200
		ycoord2 = 200
		DIRECTION = RIGHT
		direction2 = LEFT
		SPEED = 10
		LEVEL=1
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
						DIRECTION = SW
					elif (event.key == K_d):
						DIRECTION = SE
					if (event.key == K_ESCAPE):
						 TERMINATE()
					if (event.key == K_u):
						direction2 = UP
					elif (event.key == K_j):
						direction2 = DOWN
					elif (event.key == K_k):
						direction2 = RIGHT
					elif (event.key == K_h):
						direction2 =  LEFT
			if (DIRECTION == UP):
				Ycoord-=SPEED
			elif (DIRECTION == DOWN):
				Ycoord+=SPEED
			elif (DIRECTION == LEFT):
				Xcoord-=SPEED
			elif (DIRECTION == RIGHT):
				Xcoord+=SPEED
			elif (DIRECTION == NE):
				Xcoord+=SPEED
				Ycoord+=SPEED
			elif (DIRECTION == SE):
				Xcoord+=SPEED
				Ycoord-=SPEED
			elif (DIRECTION == NW):
				Xcoord-=SPEED
				Ycoord+=SPEED
			elif (DIRECTION == SW):
				Xcoord-=SPEED
				Ycoord-=SPEED
			if (direction2 == UP):
				ycoord2-=SPEED
			elif (direction2 == DOWN):
				ycoord2+=SPEED
			elif (direction2 == LEFT):
				xcoord2-=SPEED
			elif (direction2 == RIGHT):
				xcoord2+=SPEED
				
			if(Xcoord<0):
				Xcoord=abs(Xcoord)
				DIRECTION = RIGHT
			elif(Xcoord+10>WINDOWWIDTH):
				Xcoord= WINDOWWIDTH - (Xcoord-WINDOWWIDTH)
				DIRECTION = LEFT
			if(Ycoord<0):
				Ycoord=abs(Ycoord)
				DIRECTION = DOWN
			elif(Ycoord+10>WINDOWHEIGHT):
				Ycoord= WINDOWHEIGHT - (Ycoord-WINDOWHEIGHT)
				DIRECTION = UP
			if(xcoord2<0):
				xcoord2=abs(xcoord2)
				direction2 = RIGHT
			elif(xcoord2+10>WINDOWWIDTH):
				xcoord2= WINDOWWIDTH - (xcoord2-WINDOWWIDTH)
				direction2 = LEFT
			if(ycoord2<0):
				ycoord2=abs(ycoord2)
				direction2 = DOWN
			elif(ycoord2+10>WINDOWHEIGHT):
				ycoord2= WINDOWHEIGHT - (ycoord2-WINDOWHEIGHT)
				direction2 = UP
			if(Xcoord<50 and Ycoord<32 or xcoord2<50 and ycoord2<32):
				LEVEL = LEVEL + 1
				Xcoord=300
				xcoord2=200
			if(LEVEL==1):
				DISPLAYSURF.fill(BLACK)
				DISPLAYSURF.blit(img,(0,0))
				text = BASICFONT.render('Level 1', True, RED)
				textc = text.get_rect()
				textc.topleft = (300,10)
				DISPLAYSURF.blit(text,textc)
			elif(LEVEL==2):
				DISPLAYSURF.fill(WHITE)
				DISPLAYSURF.blit(img,(0,0))
				text = BASICFONT.render('Level 2', True, BLUE)
				textc = text.get_rect()
				textc.topleft = (300,10)
				DISPLAYSURF.blit(text,textc)
			elif(LEVEL>2) and (LEVEL<=10):
				DISPLAYSURF.fill(BLACK)
				DISPLAYSURF.blit(img,(0,0))
				text = BASICFONT.render('Level %s' % LEVEL, True, BLUE)
				textc = text.get_rect()
				textc.topleft = (300,10)
				DISPLAYSURF.blit(text,textc)
			elif(LEVEL>=10):
				DISPLAYSURF.fill(BLACK)
				text = BASICFONT.render('You have won. Congratulations', True, BLUE)
				textc = text.get_rect()
				textc.topleft = (200, 10)
				DISPLAYSURF.blit(text, textc)
			pygame.draw.circle(DISPLAYSURF,RED,(Xcoord, Ycoord),20)
			pygame.draw.circle(DISPLAYSURF,BLUE,(xcoord2, ycoord2),20)
			pygame.display.update()
			FPSCLOCK.tick(FPS)
	def TERMINATE():
		pygame.quit()
		sys.exit()

	def showstartscreen():
		DISPLAYSURF.fill(BLACK)
		pygame.display.update()
		FPSCLOCK.tick(FPS)
	main()
