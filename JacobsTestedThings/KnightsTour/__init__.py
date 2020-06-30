import random

def createGrid():
	rows, cols = (8, 8)
	arr = [["e" for i in range(cols)] for j in range(rows)] 
	return arr

def printGrid(arr, n):

	for i in range(n): 
		for j in range(n):
			print(arr[i][j],end =' ')
		print() 




def CheckComplete(arr, n):
	for i in range(n): 
		for j in range(n):
			if arr[i][j] == "e":
				return False
	return True




def solve():

	board = createGrid()
	board[0][0] = 0
	MovementHistory = []
	KnightPosition = [0, 0]
	movementCounter = 1

	attempts = GetPossibleMovesForLocation([0, 0])
	attemptedMoves = []

	while not CheckComplete(board, 8):
		#If the list of possible movements has exhausted for this square
		#Go back a step
		#print(attempts)
		if not attempts:
			#print("counter" + str(movementCounter))
			#Return to untouched state
			board[KnightPosition[0]][KnightPosition[1]] = "e"
			movementCounter -= 1
			reverseMove = MoveBackASpace(MovementHistory)
			#Undo the last move
			KnightPosition = [KnightPosition[0] - reverseMove[0][0], KnightPosition[1] - reverseMove[1]]
			#print(attemptedMoves[KnightPosition[0]][KnightPosition[1]])
			attempts = reverseMove[1]
			continue


		# ToDo if out of bounds, remove that possible move for the square
		direction = attempts.pop(random.randint(0, len(attempts) - 1))
		newDirection = MoveDirection(direction)
		newPosition = GetNewPosition(KnightPosition, newDirection)
		if newPosition[0] < 0 or newPosition[0] > 7 or newPosition[1] < 0 or newPosition[1] > 7:
			continue
		if (board[newPosition[0]][newPosition[1]] == "e"):
			board[newPosition[0]][newPosition[1]] = movementCounter
			MovementHistory.append([newDirection, attempts])

			#attemptedMoves.append(attempts)

			movementCounter += 1
			KnightPosition = [newPosition[0], newPosition[1]]
			attempts = GetPossibleMovesForLocation(KnightPosition)
			continue
			#printGrid(board, 8)
			#print(" ")

	return board

def GetPossibleMovesForLocation(currentLocation):
	possibleAttempts = []
	for i in range(8):
		move = MoveDirection(i)
		newPosition = GetNewPosition(currentLocation, move)
		if newPosition[0] < 0 or newPosition[0] > 7 or newPosition[1] < 0 or newPosition[1] > 7:
			continue
		else:
			possibleAttempts.append(i)
	return possibleAttempts

def MoveBackASpace(moveHistory):
	previousLocation = moveHistory.pop()
	return previousLocation

def GetNewPosition(currentPosition, moveDirection):
	return [currentPosition[0] + moveDirection[0], currentPosition[1] + moveDirection[1]]

def GetPreviousPosition(currentPosition, moveDirection):
	return [currentPosition[0] - moveDirection[0], currentPosition[1] - moveDirection[1]]

def MoveDirection(direction):
	directions = {
		0 : [2, 1],
		1 : [1, 2],
		2 : [-1, 2],1
		3 : [-2, 1],
		4 : [-2, -1],
		5 : [-1, -2],
		6 : [1, -2],
		7 : [2, -1]
	}

	return directions[direction]


grid = createGrid()

#print(grid[1][2])
#printGrid(solve(), 8)

if __name__ == '__main__':
    unittest.main()