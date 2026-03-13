import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
  data = input().rstrip()
  tmp_list = []
  for char in data:
    tmp_list.append(int(char))
  graph.append(tmp_list)

q = deque()
q.append((0,0))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
  x,y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx >= 0 and nx < n and ny >= 0 and ny < m):
      if(graph[nx][ny] == 1):
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx,ny))

print(graph[n-1][m-1])