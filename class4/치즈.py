import sys
import copy
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

cheese_count = 0
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1:
      cheese_count += 1

q = deque()
sec = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def melt_cheese():
  global cheese_count
  copy_graph = copy.deepcopy(graph)

  for x in range(n):
    for y in range(m):
      if copy_graph[x][y] == 1:
        count = 0
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if copy_graph[nx][ny] == 0:
            count += 1
        if count >= 2:
          cheese_count -= 1
          graph[x][y] = 0
          q.append((x,y))

def find_vacuum():
  possible = []
  for x in range(2, n-2):
    for y in range(2, m-2):
      if graph[x][y] == 0:
        possible.append((x,y))

  for start in possible:
    queue = deque()
    visited = [[0]*m for _ in range(n)]
    visited[start[0]][start[1]] = 1
    queue.append((start[0],start[1]))
    
    flag = True
    while queue:
      x, y = queue.popleft()
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx == 0 or nx == n-1 or ny == 0 or ny == m-1:
          flag = False
          break
        if 0 <= nx < n and 0 <= ny < m:
          if graph[nx][ny] != 1 and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            queue.append((nx,ny))
      if not flag:
        break
    
    if flag:
      graph[start[0]][start[1]] = 2



def spread():
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if graph[nx][ny] == 2:
        graph[nx][ny] = 0
        q.append((nx,ny))


find_vacuum()
while True:
  if cheese_count == 0:
    print(sec)
    break
  # print()
  # for i in range(n):
  #   for j in range(m):
  #     print(graph[i][j], end = " ")
  #   print()
  melt_cheese()
  spread()
  sec += 1