import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n = int(input())

data = []
blank = []
teacher = []
for i in range(n):
  data.append(list(map(str, input().split())))
  for j in range(n):
    if(data[i][j] == "X"):
      blank.append((i,j))
    elif(data[i][j] == "T"):
      teacher.append((i,j))

#위, 오, 아래, 왼
dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(case, data):
    copy_data = copy.deepcopy(data)
    for point in case:
      copy_data[point[0]][point[1]] = "O"
  
    for point in teacher:
      q = deque()
      for i in range(4):
        nx = point[0] + dx[i]
        ny = point[1] + dy[i]
        q.append((nx,ny,i))
      while q:
        x, y, i = q.popleft()
        if(x < n and x >= 0 and y < n and y >= 0):
          if(copy_data[x][y] == "S"):
            return False
          elif(copy_data[x][y] == "X"):
            copy_data[x][y] = "T"
            nx = x + dx[i]
            ny = y + dy[i]
            q.append((nx,ny,i))
          elif(copy_data[x][y] == "T"):
            nx = x + dx[i]
            ny = y + dy[i]
            q.append((nx,ny,i))
    return True

cases = list(combinations(blank, 3))
flag = True
for case in cases:
  flag = bfs(case, data)
  if(flag == True):
    break


if(flag == True):
  print("YES")
else:
  print("NO")


