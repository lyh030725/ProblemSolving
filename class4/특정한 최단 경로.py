import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((c,b))
  graph[b].append((c,a))

def dijkstra(start):
  q = []
  distance[start] = 0
  for c,b in graph[start]:
    heapq.heappush(q, (c,b))
    distance[b] = c 
  
  while q:
    dist, now = heapq.heappop(q)
    if(distance[now] < dist):   
      continue
    for i in graph[now]:
      cost = distance[now] + i[0]
      if(cost < distance[i[1]]):
        distance[i[1]] = cost
        heapq.heappush(q, (cost, i[1]))


result1 = 0
result2 = 0

v1, v2 = map(int, input().split())

distance = [INF]*(n+1)
dijkstra(1)
result1 += distance[v1]
result2 += distance[v2]

distance = [INF]*(n+1)
dijkstra(v1)
result1 += distance[v2]
result2 += distance[n]

distance = [INF]*(n+1)
dijkstra(v2)
result1 += distance[n]
result2 += distance[v1]


if(result1 >= INF and result2 >= INF):
  print(-1)
  exit()

print(min(result1, result2))