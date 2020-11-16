#Author:Sinan Cem Dağtekin
#Purpose:To solve a sudoku using backtracking algorithm

#this is our board to solve.We can either take from the user or just type here.The zeroes are our blank spaces.We need to solve the zeroes.
sudoku_board=[
	[7,8,0,4,0,0,1,2,0],
	[6,0,0,0,7,5,0,0,9],
	[0,0,0,6,0,1,0,7,8],
	[0,0,7,0,4,0,2,6,0],
	[0,0,1,0,5,0,9,3,0],
	[9,0,4,0,6,0,0,0,5],
	[0,7,0,3,0,0,0,1,2],
	[1,2,0,0,0,7,4,0,0],
	[0,4,9,2,0,6,0,0,7]
]

def find_zero(board):#this function finds zeroes which are empty spaces on a sudoku board.
	for i in range(len(board)):
		for j in range(len(board[0])):
			if board[i][j]==0:
				return (i,j)
	return None

def print_board(board):#this is a print function for sudoku board which is a matrix
	for i in range(len(board)):
		if i%3==0:
			print("-----------------------")
		for j in range(len(board[0])):
			if j%3==0 and j!=0:
				print(" | ", end= "")
			if j==8:
				print(board[i][j])
			else:
				print(str(board[i][j])+" ", end="")
	print("-----------------------")

def ifValid(board,x,position):#checks the board for validation
	box1=position[1]//3
	box2=position[0]//3
	for i in range(box2*3,box2*+3):
		for j in range(box1*3,box1*3+3):
			if board[i][j]==x and (i,j)!=position:
				return False
	for i in range(len(board[0])):
		if board[position [0]][i]==x and position[1]!=i:
			return False
	for i in range(len(board)):
		if board[i][position[1]]==x and position[0]!=i:
			return False
	return True

def solver(board):
    found = find_zero(board)
    #print_board(board)#to see how to code operates step by step
    if not found:
        return True
    else:
        row, col = found

    for i in range(1,10):
        if ifValid(board, i, (row, col)):
            board[row][col] = i

            if solver(board):
                return True

            board[row][col] = 0

    return False


print_board(sudoku_board)
solver(sudoku_board)
print_board(sudoku_board)