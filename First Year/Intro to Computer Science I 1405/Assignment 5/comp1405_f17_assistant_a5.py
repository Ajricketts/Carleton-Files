import pygame

pygame.init()
original_maze_image = pygame.image.load("your-assigned-maze.png")
window = pygame.display.set_mode(original_maze_image.get_rect().size)
window.blit(original_maze_image, (0, 0))
pygame.display.update()

my_color_grey = (64, 64, 64)
my_color_black = (20, 12, 28)
my_color_white = (222, 238, 214)
	
window_dimension = 65
grid_dimension = 13
border_offset = 2

global current_x, current_y
(current_x, current_y) = (0, 0)

highlighting = pygame.Surface((grid_dimension, grid_dimension))
highlighting.set_alpha(128)
highlighting.fill((255, 0, 0)) 

def _highlight_cell():
	global current_x, current_y
	window.blit(highlighting, (current_x * grid_dimension, current_y * grid_dimension))
	pygame.display.update()
	if (pygame.key.get_pressed()[pygame.K_SPACE] == 0 ):
		pygame.time.delay(200)
	else:
		pygame.time.delay(20)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

while current_x < window_dimension:
	if original_maze_image.get_at((current_x * grid_dimension + border_offset, current_y * grid_dimension + border_offset)) != my_color_black:
		_highlight_cell()
		break
	current_x += 1
	
def move_down():
	global current_y
	current_y += 1
	_highlight_cell()
	
def move_right():
	global current_x
	current_x += 1
	_highlight_cell()
	
def move_left():
	global current_x
	current_x -= 1
	_highlight_cell()	
	
def what_number_am_i_standing_on():
	pygame.display.update()
	global current_x, current_y
	am_standing_on = original_maze_image.get_at((current_x * grid_dimension + border_offset, current_y * grid_dimension + border_offset))[2] - my_color_white[2]
	if am_standing_on in range(1,6):
		return am_standing_on
	return -1

def am_i_standing_on(digit):
	pygame.display.update()
	return digit == what_number_am_i_standing_on()