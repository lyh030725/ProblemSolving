import sys

input = sys.stdin.readline
board = []

for i in range(9):
  data = input().rstrip()
  tmp = []
  for char in data:
    tmp.append(int(char))
  board.append(tmp)

def fill_board(i,j):
  if i > 8:
    return
  
  candidate = [1,2,3,4,5,6,7,8,9]
  if board[i][j] != 0:
    if j == 8:
      fill_board(i+1, 0)
    else:
      fill_board(i, j+1)
    if i == 8 and j == 8:
      for r in range(9):
          for c in range(9):
            print(board[r][c], end = "")
          print()
      exit()
    return

  for r in range(i//3*3, i//3*3+3):
    for c in range(j//3*3, j//3*3+3):
      if board[r][c] != 0:
        if board[r][c] in candidate:
          candidate.remove(board[r][c])
  for k in range(9):
    if board[i][k] != 0:
      if board[i][k] in candidate:
        candidate.remove(board[i][k])
  for k in range(9):
    if board[k][j] != 0:
      if board[k][j] in candidate:
        candidate.remove(board[k][j])

  for cand in candidate:
    board[i][j] = cand
    if i == 8 and j == 8:
      for r in range(9):
          for c in range(9):
            print(board[r][c], end = "")
          print()
      exit()

    if j == 8:
      fill_board(i+1, 0)
    else:
      fill_board(i, j+1)
    board[i][j] = 0

fill_board(0,0)