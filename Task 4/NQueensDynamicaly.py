def SafeCheaker(board, row, col, size):
 
    for i in range(row):
        if board[i][col] == 'Q':
            return False


    for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
        if board[i][j] == 'Q':
            return False

  
    for i, j in zip(range(row - 1, -1, -1), range(col + 1, size)):
        if board[i][j] == 'Q':
            return False

    return True

def Solution(board, row, size, solutions):
    if row == size:
        solutions.append([''.join(row) for row in board])
        return

    for col in range(size):
        if SafeCheaker(board, row, col, size):
            board[row][col] = 'Q'
            Solution(board, row + 1, size, solutions)
            board[row][col] = '.'  

def Board(board):
    for row in board:
        print('|' + '|'.join(row) + '|')
    print()

size = int(input("Enter the size: "))
board=[]
for i in range(size):
    row = []
    for j in range(size):
        row.append('.')  
    board.append(row)


    
solutions = []
Solution(board, 0, size, solutions)

if solutions:
    Board(solutions[0])
else:
    print("No solution exists.")


