import sys
from collections import deque
input = sys.stdin.readline

n, m , k, x = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

visited = [0] * (n+1)
result = []

visited[x] = 1
q = deque([(x,0)])
while q:
  start, depth = q.popleft()
  if(depth == k):
    result.append(start)
  for y in graph[start]:
    if(visited[y] == 0):
      visited[y] = 1
      q.append((y,depth+1))

    
result.sort()

if(len(result) == 0):
  print(-1)
else:
  for answer in result:
    print(answer)
