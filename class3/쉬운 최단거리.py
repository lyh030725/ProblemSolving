import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))
  for j in range(m):
    if(graph[i][j] == 2):
      start = (i,j)

visited = [[0]*m for _ in range(n)]

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

def bfs(graph, start):
  q = deque()
  q.append((start, 0))

  while q:
    now, dist = q.popleft()
    x, y = now

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(nx >= 0 and nx < n and ny >= 0 and ny < m):
        if(graph[nx][ny] == 1 and visited[nx][ny] == 0):
          visited[nx][ny] = dist+1
          q.append(((nx,ny), dist+1))

bfs(graph, start)

for i in range(n):
  for j in range(m):
    if(graph[i][j] == 1 and visited[i][j] == 0):
      print("-1", end = " ")
      continue
    print(visited[i][j], end=" ")
  print()