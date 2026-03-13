import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

obj = []

for i in range(n):
  a,b = map(int, input().split())
  obj.append((a,b))

for i in range(m):
  a,b = map(int, input().split())
  obj.append((a,b))

q = deque()
start = 1

q.append((start, 0))
visited = [0]*101

while q:
  now, count = q.popleft()
  visited[now] = 1
  if(now == 100):
    print(count)
    break
  for i in range(1,7):
    next = now+i
    if(next <= 100):
      obj_found = False
      for j in range(n+m):
        if(obj[j][0] == next):
            visited[next] = 1
            q.append((obj[j][1], count+1))
            obj_found = True
            break
      if(obj_found):
        continue
      if(visited[next] == 0):
        q.append((next, count+1))