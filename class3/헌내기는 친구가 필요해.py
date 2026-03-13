import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []

for i in range(n):
  data = input().rstrip()
  tmp_list = []
  for j in range(m):
    tmp_list.append(data[j])
    if(data[j] == "I"):
      start = (i,j)
  graph.append(tmp_list)

q = deque()
q.append(start)

dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]
count = 0

while q:
  x, y = q.popleft()
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx >= 0 and nx < n and ny >= 0 and ny < m):
      if(graph[nx][ny] == "O"):
        graph[nx][ny] = "I"
        q.append((nx,ny))
      elif(graph[nx][ny] == "P"):
        count += 1
        graph[nx][ny] = "I"
        q.append((nx,ny))

if(count == 0):
  print("TT")
else:
  print(count)