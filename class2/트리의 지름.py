import sys

sys.setrecursionlimit(10**6) 

def dfs(start):
  linked = node[start]
  for cost, now in linked:
    if(dist[now] == INF):
      dist[now] = dist[start] + cost
      dfs(now)

input = sys.stdin.readline
INF = int(1e9)

n = int(input())

node = [[] for _ in range(n+1)]

for i in range(1, n+1):
  data = list(map(int, input().split()))[:-1]
  num = data[0]

  for j in range(1, len(data), 2):
    node[num].append((data[j+1], data[j]))

dist = [INF]*(n+1)

dist[1] = 0
dfs(1)
max_vertex = dist.index(max(dist[1:]))

dist = [INF]*(n+1)
dist[max_vertex] = 0
dfs(max_vertex)
print(max(dist[1:]))