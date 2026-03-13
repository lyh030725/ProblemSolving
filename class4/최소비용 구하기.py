import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b,cost = map(int, input().split())
  graph[a].append((cost,b))

x,y = map(int, input().split())

distance = [INF]*(n+1)
distance[x] = 0
q = []
for item in graph[x]:
  cost, b = item
  distance[b] = min(distance[b], cost)
  heapq.heappush(q, (cost,b))

while q:
  dist, now = heapq.heappop(q)
  if(distance[now] < dist):
    continue
  for i in graph[now]:
    cost = distance[now] + i[0]
    if(cost < distance[i[1]]):
      distance[i[1]] = cost
      heapq.heappush(q, (cost, i[1]))

print(distance[y])