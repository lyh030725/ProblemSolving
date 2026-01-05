#다익스트라 알고리즘(힙[우선순위 큐] 버전, 향상된 버전)
#O(ElogV)

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
for i in range(m):
  a,b,c = map(int , input().split())
  graph[a].append((b,c))

distance = [INF]*(n+1)

def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0,start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for j in graph[now]:
      cost = distance[now] + j[1]
      if(cost < distance[j[0]]):
        distance[j[0]] = cost
        heapq.heappush(q, (cost, j[0]))

dijkstra(start)

for i in range(1, n+1):
  if(distance[i] == INF):
    print("INFINITY")
  else:
    print(distance[i])
