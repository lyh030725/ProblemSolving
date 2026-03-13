n , m = map(int, input().split())

board = []


for i in range(n):
  board.append(list(input()))

def min_change(board):
  count1 = 0
  for i in range(1, 64, 2):
    if((i//8) % 2 == 0):
      if(board[i//8][i%8-1] == "W" and board[i//8][i%8] == "B"):
        continue
      elif(board[i//8][i%8-1] == "B" and board[i//8][i%8] == "W"):
        count1 += 2
      else:
        count1 += 1
    else:
      if(board[i//8][i%8-1] == "B" and board[i//8][i%8] == "W"):
        continue
      elif(board[i//8][i%8-1] == "W" and board[i//8][i%8] == "B"):
        count1 += 2
      else:
        count1 += 1
  
  count2 = 0
  for i in range(1, 64, 2):
    if((i//8) % 2 == 0):
      if(board[i//8][i%8-1] == "B" and board[i//8][i%8] == "W"):
        continue
      elif(board[i//8][i%8-1] == "W" and board[i//8][i%8] == "B"):
        count2 += 2
      else:
        count2 += 1
    else:
      if(board[i//8][i%8-1] == "W" and board[i//8][i%8] == "B"):
        continue
      elif(board[i//8][i%8-1] == "B" and board[i//8][i%8] == "W"):
        count2 += 2
      else:
        count2 += 1
  
  return min(count1, count2)

result = int(1e9)
for i in range(n-7):
  line = board[i:i+8]
  for j in range(m-7):
    data = []
    for l in line:
      data.append(l[j:j+8])
    result = min(result, min_change(data))

print(result)




