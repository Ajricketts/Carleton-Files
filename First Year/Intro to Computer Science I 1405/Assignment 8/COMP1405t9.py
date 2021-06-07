def buildGameGrid(size):
	gameGrid = []	
	for i in range(size):
		row = []
		for j in range(size):
			row.append(0)
		gameGrid.append(row)	

	return gameGrid
			


def printGameGrid(gameGrid):
	for i in gameGrid:
		print(i)

def checkTilePosition(gameGrid, pos):
	Zx = pos[0]
	y = pos[1]
				
	if gameGrid[y][x] == 0:
		free_space = True
	else:
		free_space = False 
	print(free_space)

def checkLeftTiles(gameGrid, playerNum, pos):

def checkRightTiles(gameGrid, playerNum, pos):
	x = pos[0]	
	y = pos[1]
	tiles_to_flip = []
	checkTilePosition(gameGrid, pos)
	for i in gameGrid[y][x]:	
		if not(free_space):
			if gameGrid[y][x] == playerNum:
				break
			elif gameGrid[y][x] != playerNum:
				tiles_to_flip.append(gameGrid[y][x])
		if free_space:
			break
	return tiles_to_flip
def checkTopTiles(gameGrid, playerNum, pos):

def checkBottomTiles(gameGrid, playerNum, pos):

def flipTilePosition(gameGrid, playerNum, pos):
	checkRightTile(gameGrid,playerNum, pos)
	checkLeftTile(gameGrid,playerNum, pos)
	checkDownTile(gameGrid,playerNum, pos)
	checkUpTile(gameGrid,playerNum, pos)	
	count = 0
	for i in tiles_to_flip:
		tiles_to_flip[count] = 1
		count += 1	
def main():
	# Initialize some Constants
	player1 = 1; player2 = 2; size = 9
	currentPlayer = player1
	# Building our 'Go' Board
	goBoard = buildGameGrid(size)
	printGameGrid(goBoard)
	numMovesPlayed = 0
	# Keep looping until no more possible moves
	while numMovesPlayed < size**2:
		# Get player X's input and format it into a list of 2 ints
		chosenMove = input("Player {}: What move will you make? ".format(currentPlayer)).strip(' ').strip('(').strip(')').split(',')
		chosenMove[0] = int(chosenMove[0]); chosenMove[1] = int(chosenMove[1])
		# Keep asking player until they give a valid position - once valid, flipTilePosition is called and used
		while not flipTilePosition(goBoard, currentPlayer, chosenMove):
			print("Sorry, that tile is unavailable - please select another.")
			chosenMove = input("Player {}: What move will you make? ".format(currentPlayer)).strip(' ').strip('(').strip(')').split(',')
			chosenMove[0] = int(chosenMove[0]); chosenMove[1] = int(chosenMove[1])
		# Flip Player and print game state
		if currentPlayer == player1:
			currentPlayer = player2
		else:
			currentPlayer = player1
		printGameGrid(goBoard)
		numMovesPlayed += 1

if __name__ == "__main__":
	main()
