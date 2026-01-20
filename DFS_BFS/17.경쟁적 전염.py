import sys
input = sys.stdin.readline
from collections import deque

n , k = map(int , input().split())

tube = []
for _ in range(n):
  line = list(map(int, input().split()))
  tube.append(line)

s, x, y = map(int, input().split())

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

q = deque([])

for virus in range(1, k+1):
  for i in range(n):
    for j in range(n):
      if(tube[i][j] == virus):
        q.append((virus,i,j))
        continue

for _ in range(s):
  temp = []
  while q:
    virus, px, py = q.popleft()
    for i in range(4):
      nx = px + dx[i]
      ny = py + dy[i]
      if(nx >= 0 and nx < n and ny >=0 and ny < n):
        if(tube[nx][ny] == 0):
          tube[nx][ny] = virus
          temp.append((virus, nx, ny))
  q = deque(temp)


print(tube[x-1][y-1])