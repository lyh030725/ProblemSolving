import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
  tmp_list = []
  data = input().rstrip()
  for char in data:
    tmp_list.append(int(char))
  graph.append(tmp_list)

visited = [[0]*n for _ in range(n)]

dx = [-1, 1, 0 , 0]
dy = [0, 0 ,-1, 1]

def bfs(start):
  global count

  q = deque()
  q.append(start)
  visited[start[0]][start[1]] = 1

  while q:
    now = q.popleft()
    for i in range(4):
      nx = now[0] + dx[i]
      ny = now[1] + dy[i]
      if(nx >= 0 and nx < n and ny >= 0 and ny < n):
        if(graph[nx][ny] == 1 and visited[nx][ny] == 0):
          q.append((nx,ny))
          visited[nx][ny] = 1
          count += 1

group = []
for i in range(n):
  for j in range(n):
    if(graph[i][j] == 1 and visited[i][j] == 0):
      count = 1
      bfs((i,j))
      group.append(count)

print(len(group))
group.sort()
for num in group:
  print(num)