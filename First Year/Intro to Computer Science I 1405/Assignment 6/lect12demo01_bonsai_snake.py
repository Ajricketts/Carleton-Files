import pygame, sys, os, random

from pygame.locals import *


DIRECTION_UP    = 0
DIRECTION_DOWN  = 1
DIRECTION_LEFT  = 2
DIRECTION_RIGHT = 3

COLOUR_BACKGROUND = (0, 127, 0)
COLOUR_SNAKE      = (255, 255, 0)
COLOUR_COIN       = (255, 0, 0)
COLOUR_TEXT       = (0, 0, 0)


wide = 50
high = 50
zoom = 10

score_x = wide * zoom / 2
score_y = high * zoom / 20

center_x = wide * zoom / 2
center_y = high * zoom / 2

head_x = wide / 2
head_y = high / 2

tail_x = wide / 2
tail_y = high / 2 - 1

coin_x = random.randint(1, wide - 2)
coin_y = random.randint(1, high - 2)

direction = DIRECTION_DOWN

current_score = 0
current_bonus = 100

current_delay = 100

pygame.init()

drawing_surface = pygame.display.set_mode((wide * zoom, high * zoom), 0, 32)

pygame.display.set_caption("Bonsai Snake")

game_area = [[0 for x in range(wide)] for y in range(high)]

pygame.font.init()

current_score_font = pygame.font.Font("Px437_Phoenix_BIOS.ttf", 16)

game_over_font = pygame.font.Font("Px437_Phoenix_BIOS.ttf", 48)
game_over_message = game_over_font.render("game over", 1, COLOUR_TEXT)
game_over_rectangle = game_over_message.get_rect(center = (center_x, center_y))

player_wants_to_quit = False
game_over = False


while not player_wants_to_quit:


	# render
	
	drawing_surface.fill(COLOUR_BACKGROUND)
	
	pygame.draw.rect(drawing_surface, COLOUR_SNAKE, (head_x * zoom, head_y * zoom, zoom, zoom))
	pygame.draw.rect(drawing_surface, COLOUR_SNAKE, (tail_x * zoom, tail_y * zoom, zoom, zoom))

	pygame.draw.rect(drawing_surface, COLOUR_COIN, (coin_x * zoom, coin_y * zoom, zoom, zoom))

	current_score_message = current_score_font.render(str(current_score), 1, COLOUR_TEXT)
	current_score_rectangle = current_score_message.get_rect(center = (score_x, score_y))	
	
	drawing_surface.blit(current_score_message, current_score_rectangle)
	
	# input
	
	for event in pygame.event.get():
		if event.type == QUIT:
			player_wants_to_quit = True

			
	pressed_keys = pygame.key.get_pressed()

	if pressed_keys[pygame.K_ESCAPE] == 1:
		player_wants_to_quit = True
	elif pressed_keys[pygame.K_UP] == 1:
		direction = DIRECTION_UP
	elif pressed_keys[pygame.K_DOWN] == 1:
		direction = DIRECTION_DOWN
	elif pressed_keys[pygame.K_LEFT] == 1:
		direction = DIRECTION_LEFT
	elif pressed_keys[pygame.K_RIGHT] == 1:
		direction = DIRECTION_RIGHT
	
	
	# logic
	
	if game_over:

		drawing_surface.blit(game_over_message, game_over_rectangle)
		
	else:
		
		next_x = head_x
		next_y = head_y
		
		if direction == DIRECTION_UP:
			next_y = next_y - 1
		elif direction == DIRECTION_DOWN:
			next_y = next_y + 1
		elif direction == DIRECTION_LEFT:
			next_x = next_x - 1
		else:
			next_x = next_x + 1
		
		if next_x < 0 or next_x > wide or next_y < 0 or next_y > high or (next_x == tail_x and next_y == tail_y):
		
			game_over = True
			
		else:
		
			tail_x = head_x
			tail_y = head_y
			head_x = next_x
			head_y = next_y
			
			if (head_x == coin_x and head_y == coin_y):
				coin_x = random.randint(1, wide - 2)
				coin_y = random.randint(1, high - 2)
				current_score = current_score + current_bonus
				current_bonus = current_bonus * 2
				current_delay = int(current_delay * 0.9)

		pygame.time.delay(current_delay)
	
	pygame.display.update()