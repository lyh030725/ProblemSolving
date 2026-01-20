import sys
import copy
from itertools import combinations
input = sys.stdin.readline

n, m = map(int , input().split())

data = []

for i in range(n):
  line = list(map(int , input().split()))
  data.append(line)
blank = []
virus = []

for i in range(n):
  for j in range(m):
    if(data[i][j] == 0):
      blank.append((i,j))
    elif(data[i][j] == 2):
      virus.append((i,j))

cases = combinations(blank, 3)
answer = 0

def spread(data, virus):
  row = virus[0]
  col = virus[1]
  if(row < 0 or col < 0 or row >= n or col >= m):
    return
  #left
  if(col > 0 and data[row][col-1] == 0):
    data[row][col-1] = 2
    spread(data, (row, col-1))
  #right
  if(col < m-1 and data[row][col+1] == 0):
    data[row][col+1] = 2
    spread(data, (row, col+1))
  #up
  if(row > 0 and data[row-1][col] == 0):
    data[row-1][col] = 2
    spread(data, (row-1 , col))
  #down
  if(row < n-1 and data[row+1][col] == 0):
    data[row+1][col] = 2
    spread(data, (row+1, col))
  return data

for case in cases:
  copy_data = copy.deepcopy(data)
  count = 0
  for wall in case:
    copy_data[wall[0]][wall[1]] = 1
  for virus_point in virus:
    copy_data = spread(copy_data, virus_point)
  for i in range(n):
    for j in range(m):
      if(copy_data[i][j] == 0):
        count += 1
  answer = max(answer, count)

print(answer)