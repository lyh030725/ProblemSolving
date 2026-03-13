import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

distance = [INF]*(n+1)

graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((c,b))

q = []
heapq.heappush(q,(0, start))
distance[start] = 0

while q:
  dist, now = heapq.heappop(q)
  if(distance[now] < dist):
    continue
  
  for j in graph[now]:
    cost = j[0]+distance[now]
    if(cost < distance[j[1]]):
      distance[j[1]] = cost
      heapq.heappush(q, (cost, j[1]))

for i in range(1, n+1):
  if(distance[i] == INF):
    print("INF")
  else:
    print(distance[i])