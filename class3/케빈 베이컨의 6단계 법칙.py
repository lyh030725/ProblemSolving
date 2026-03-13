import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

min_value = int(1e9)
result = 0

for i in range(n, 0, -1):
  q = deque()
  visited = [-1]*(n+1)
  visited[i] = 0
  q.append(i)
  while q:
    now = q.popleft()
    for j in graph[now]:
      if(visited[j] == -1):
        q.append(j)
        visited[j] = visited[now] + 1
  
  count = 0
  for k in range(1, n+1):
    count += visited[k]
  
  min_value = min(min_value, count)
  if(min_value == count):
    result = i

print(result)