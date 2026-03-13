import sys
from collections import deque

input = sys.stdin.readline

m,n,h = map(int, input().split())

graph = []
tomatos = []

for k in range(h):
  tmp_list = []
  for i in range(n):
    tmp_list.append(list(map(int, input().split())))
  graph.append(tmp_list)
  for i in range(n):
    for j in range(m):
      if(graph[k][i][j] == 1):
        tomatos.append((k,i,j, 0))

dz = [0, 0, 0, 0, 1, -1]
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]


result = 0

def bfs(graph):
  global result
  while q:
    z,x,y, day = q.popleft()
    result = max(result, day)
    for i in range(6):
      nz = z + dz[i]
      nx = x + dx[i]
      ny = y + dy[i]
      if(nz >= 0 and nz < h and nx >= 0 and nx < n and ny >= 0 and ny < m):
        if(graph[nz][nx][ny] == 0):
          graph[nz][nx][ny] = 1
          q.append((nz,nx,ny, day+1))

q = deque()
for tomato in tomatos:
  q.append(tomato)

bfs(graph)

for k in range(h):
  for i in range(n):
    for j in range(m):
      if(graph[k][i][j] == 0):
        print(-1)
        exit()

print(result)