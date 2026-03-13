import sys
import copy
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

graph = []
tomatos = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(m):
    if(graph[i][j] == 1):
      tomatos.append((i,j))

q = deque()
for tomato in tomatos:
  q.append((tomato, 0))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0

while q:
  now, day = q.popleft()
  result = max(result, day)

  x,y = now
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx >= 0 and nx < n and ny >= 0 and ny < m):
      if(graph[nx][ny] == 0):
        graph[nx][ny] = 1
        q.append(((nx,ny),day+1))

for i in range(n):
  for j in range(m):
    if(graph[i][j] == 0):
      print(-1)
      exit()

print(result)