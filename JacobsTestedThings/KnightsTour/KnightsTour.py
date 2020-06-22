import random
#Creates the list full of 'e' to represent the board
def createGrid():
	rows, cols = (8, 8)
	arr = [["e" for i in range(cols)] for j in range(rows)] 
	return arr

#Prints out a given grid of size n
def printGrid(arr, n):
	for i in range(n): 
		for j in range(n):
			print(arr[i][j],end =' ')
		print() 

#Completes a shallow complete check, if the grid has an e, it is incomplete
def CheckComplete(arr, n):
	for i in range(n): 
		for j in range(n):
			if arr[i][j] == "e":
				return False
	return True


def solve():
	board = createGrid()
	#Starting point is at top left, so set as 0
	board[0][0] = 0
	#MovementHistory stores the location and number of possible moves left
	#for each tile it has touched
	MovementHistory = []
	KnightPosition = [0, 0]
	movementCounter = 1
	attempts = GetPossibleMovesForLocation(KnightPosition, board)

	while not CheckComplete(board, 8):
		newValues = AttemptMovement(attempts, KnightPosition, MovementHistory, movementCounter, board)
		attempts = newValues[0];
		KnightPosition = newValues[1]
		MovementHistory = newValues[2]
		movementCounter = newValues[3]
		board = newValues[4]
	return board

def AttemptMovement(attempts, KnightPosition, MovementHistory, movementCounter, board):
	# if a possible move exists for the knights current location
	if attempts:
		#Pick a move and calculate the new position
		move = attempts.pop()
		direction = MoveDirection(move)
		newPosition = GetNewPosition(KnightPosition, direction)
		#If the new position is empty
		if board[newPosition[0]][newPosition[1]] == "e":
			#Register the move and remaining possible moves in the history
			MovementHistory.append([KnightPosition, attempts])
			#Move the knight
			KnightPosition = newPosition
			board[KnightPosition[0]][KnightPosition[1]] = movementCounter
			movementCounter += 1
			attempts = GetPossibleMovesForLocation(KnightPosition, board)

	#If no moves remain, need to back track and find a possible move
	elif not attempts:
		board[KnightPosition[0]][KnightPosition[1]] = "e"
		movementCounter -= 1
		previousSpace = MovementHistory.pop()
		KnightPosition = previousSpace[0]
		attempts = previousSpace[1]

	return [attempts, KnightPosition, MovementHistory, movementCounter, board]


#Retrieves all the possible moves from a given location on the board
def GetPossibleMovesForLocation(currentLocation, board):
	possibleAttempts = []
	for i in range(8):
		move = MoveDirection(i)
		newPosition = GetNewPosition(currentLocation, move)
		if newPosition[0] < 0 or newPosition[0] > 7 or newPosition[1] < 0 or newPosition[1] > 7:
			continue
		if board[newPosition[0]][newPosition[1]] == "e":
			possibleAttempts.append(i)
	return possibleAttempts

#returns a knights move when given an integer 0-7, each representing
#one of the possible moves a knight can make
def MoveDirection(direction):
	directions = {
		0 : [2, 1],
		1 : [1, 2],
		2 : [-1, 2],
		3 : [-2, 1],
		4 : [-2, -1],
		5 : [-1, -2],
		6 : [1, -2],
		7 : [2, -1]
	}

	return directions[direction]

def GetNewPosition(currentPosition, moveDirection):
	return [currentPosition[0] + moveDirection[0], currentPosition[1] + moveDirection[1]]

grid = createGrid()

#The below line needs to be commented when testing
printGrid(solve(), 8)
