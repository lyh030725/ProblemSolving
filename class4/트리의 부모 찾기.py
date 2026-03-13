import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for i in range(n-1):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

q = deque()
parent = [1]*(n+1)

for i in graph[1]:
  q.append(i)
  parent[i] = 1

visited = [0]*(n+1)
visited[1] = 1
while q:
  now = q.popleft()
  visited[now] = 1

  for i in graph[now]:
    if(visited[i] == 0):
      parent[i] = now
      q.append(i)

for i in range(2, n+1):
  print(parent[i])