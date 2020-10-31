import pygame
from random import randint
from copy import deepcopy

RES = WIDTH, HEIGHT = 1920, 1080
TITLE = 20
W, H = WIDTH // TITLE, HEIGHT // TITLE
FPS = 10

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()

next_field = [[0 for i in range(W)] for j in range(H)]
current_field = [[randint(0,1) for i in range(W)] for j in range(H)]

def chech_cell(current_field, x, y):
	count = 0
	for j in range(y - 1, y + 2):
		for i in range(x - 1, x + 2):
			if current_field[j][i]:
				count += 1
	if current_field[y][x]:
		count -= 1
		if count == 2 or count == 3:
			return 1
		return 0
	else:
		if count == 3:
			return 1
		return 0



while True:
	surface.fill(pygame.Color("black"))
	for even in pygame.event.get():
		if even.type == pygame.QUIT:
			exit()

	[pygame.draw.line(surface, pygame.Color('dimgray'), (x, 0), (x, HEIGHT)) for x in range(0, WIDTH, TITLE)]
	[pygame.draw.line(surface, pygame.Color('dimgray'), (0, y), (WIDTH, y)) for y in range(0, HEIGHT, TITLE)]

	for x in range(1, W - 1):
		for y in range(1, H - 1):
			if current_field[y][x]:
				pygame.draw.rect(surface, pygame.Color('forestgreen'), (x * TITLE + 2, y * TITLE + 2, TITLE - 2, TITLE -2))
			next_field[y][x] = chech_cell(current_field, x, y)

	current_field = deepcopy(next_field)		

	pygame.display.flip()
	clock.tick(FPS)