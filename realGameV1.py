import pygame
import random
import time
pygame.init()

gameState = {
	'blockY':0,
	'blockShow1':random.randrange(0,2),
	'blockShow2':random.randrange(0,2),
	'blockShow3':random.randrange(0,2),
	'blockShow4':random.randrange(0,2),
	'blockShow5':random.randrange(0,2)

}

gameDisplay = pygame.display.set_mode((500,400))

pygame.display.set_caption('realGame')

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
purple = (148,0,211)
purple2 = (147,112,219)

font = pygame.font.SysFont(None, 25)

def message(msg,color,x,y):
		screen_text = font.render(msg, True, color)
		gameDisplay.blit(screen_text, [x,y])

def gameFunction():
	gameExit = False

	img = pygame.image.load('Downloads/player.png')
	img = pygame.transform.scale(img, (100,100))
	imgx = 200
	imgy = 300
	
	blockY = 0
		
	time = 0

	score = 0
	
	def blockGenerate():
		print("blockgenerate")
		global gameState
		if gameState['blockY'] < 400:
			gameState['blockY'] += 50
		else:
			gameState['blockY'] = 0
			gameState['blockShow2'] = random.randrange(0,2)
			gameState['blockShow3'] = random.randrange(0,2)
			gameState['blockShow4'] = random.randrange(0,2)
			gameState['blockShow5'] = random.randrange(0,2)
			gameState['blockShow1'] = random.randrange(0,2)			
		print(gameState['blockY'])

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameExit = True

			if event.type == pygame.KEYDOWN:				
		
				if event.key == pygame.K_RIGHT:
					imgx += 100
				if event.key == pygame.K_LEFT:
					imgx -= 100

		

		gameDisplay.fill(purple)
		
		gameDisplay.blit(img, (imgx, imgy))

		message(str(score),black,10,10)
		
		if pygame.time.get_ticks() % 100 == 0: 
			print(gameState)
			blockGenerate()
			print(gameState)
		if gameState['blockShow1'] == 1:
			pygame.draw.rect(gameDisplay, purple2,[0,gameState['blockY'],100,100])
		if gameState['blockShow2'] == 1:
			pygame.draw.rect(gameDisplay, purple2,[100,gameState['blockY'],100,100])
		if gameState['blockShow3'] == 1:
			pygame.draw.rect(gameDisplay, purple2,[200,gameState['blockY'],100,100])
		if gameState['blockShow4'] == 1:
			pygame.draw.rect(gameDisplay, purple2,[300,gameState['blockY'],100,100])
		if gameState['blockShow5'] == 1:
			pygame.draw.rect(gameDisplay, purple2,[400,gameState['blockY'],100,100])
		pygame.display.update()

		if gameState['blockY'] == 300:
			if imgx == 0 and gameState['blockShow1'] == 1:
				pygame.quit()
				quit()
			if imgx == 100 and gameState['blockShow2'] == 1:
				pygame.quit()
				quit()
			if imgx == 200 and gameState['blockShow3'] == 1:
				pygame.quit()
				quit()
			if imgx == 300 and gameState['blockShow4'] == 1:
				pygame.quit()
				quit()
			if imgx == 400 and gameState['blockShow5'] == 1:
				pygame.quit()
				quit()
			if imgx > 400 or imgx < 0:
				pygame.quit()
				quit()
			else:
				score += 99
				

gameFunction()

pygame.quit()
quit()







