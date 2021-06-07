import pygame

pygame.init()
game_board = pygame.image.load("your-game-board.png")
window = pygame.display.set_mode(game_board.get_rect().size)
window.blit(game_board, (0, 0))
pygame.display.update()

def ask_question(prompt):
	user_input = input(prompt)
	while user_input.upper() not in ['YES', 'NO']:
		print("- Please answer using either yes or no. ", end = '')
		user_input = input()
	return user_input
	
def make_a_guess(object):
	print(object)
	_ = input("- Was this the correct answer?")
	exit()