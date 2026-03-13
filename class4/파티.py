import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, m, x = map(int, input().split())

distance = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1):
  distance[i][i] = 0

graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((c,b))

def shortest_path(start):
  q = []
  heapq.heappush(q, (0,start))

  while q:
    dist, now = heapq.heappop(q)
    if(distance[start][now] < dist):
      continue
    for i in graph[now]:
      cost = i[0] + distance[start][now]
      if(cost < distance[start][i[1]]):
        distance[start][i[1]] = cost
        heapq.heappush(q, (cost, i[1]))

for i in range(1, n+1):
  shortest_path(i)

result = [INF]*n

for i in range(1, n+1):
  result[i-1] = distance[i][x] + distance[x][i]

print(max(result))