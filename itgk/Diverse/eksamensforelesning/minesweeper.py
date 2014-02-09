import random

def createBoard(density):
	board = []
	for r in range(rows):
		board.append([None] * cols)
	for r in range(rows):
		for c in range(cols):
			board[r][c] = (random.random() < density)
	return board

def createOpenStatus():
	status = []
	for r in range(rows):
		status.append([False] * cols)
	return status

def countSurroundingMines(board, row, col):
	count = 0
	for r in range(row - 1, row + 2):
		for c in range(col - 1, col + 2):
			if not (r == row and c == col) and c >= 0 and c < cols and r >= 0 and r < rows and board[r][c]:
				count += 1
	return count

	
def createMineCounts(board):
	counts = []
	for r in range(rows):
		counts.append([None] * cols)
	for r in range(rows):
		for c in range(cols):
			counts[r][c] = countSurroundingMines(board, r, c)
	return counts

def printBoard(status, counts):
	for r in range(rows):
		for c in range(cols):
			if status[r][c]:
				print(counts[r][c], end="")
			else:
				print(".", end="")
		print()

rows = 8
cols = 8
board = createBoard(0.2)
#print(board)
status = createOpenStatus()
#print(status)
counts = createMineCounts(board)
#print(counts)

while True:
	printBoard(status, counts)
	row = int(input("Row: "))
	col = int(input("Column: "))
	if board[row][col]:
		print("Game over!")
		break
	status[row][col] = True
