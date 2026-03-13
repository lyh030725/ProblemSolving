import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

graph = []
for i in range(n):
  data = input().rstrip()
  tmp_list = []
  for char in data:
    tmp_list.append(char)
  graph.append(tmp_list)


no_blind_count = 0
blind_count = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def no_blind(start):
  q = deque()
  q.append(start)
  visited[start[0]][start[1]] = 1
  while q:
    x,y,color = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(nx >= 0 and nx < n and ny >= 0 and ny < n):
        if(graph[nx][ny] == color and visited[nx][ny] == 0):
          q.append((nx,ny,color))
          visited[nx][ny] = 1

def blind(start):
  q = deque()
  q.append(start)
  visited[start[0]][start[1]] = 1
  while q:
    x,y,color = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(nx >= 0 and nx < n and ny >= 0 and ny < n):
        if(color in ("G", "R")):
          if(graph[nx][ny] in ("G", "R") and visited[nx][ny] == 0):
            q.append((nx,ny,color))
            visited[nx][ny] = 1
        else:
          if(graph[nx][ny] == "B" and visited[nx][ny] == 0):
            q.append((nx,ny,color))
            visited[nx][ny] = 1

visited = [[0]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if(visited[i][j] == 0):
      no_blind((i,j, graph[i][j]))
      no_blind_count += 1

visited = [[0]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if(visited[i][j] == 0):
      blind((i,j, graph[i][j]))
      blind_count += 1

print(no_blind_count, blind_count)