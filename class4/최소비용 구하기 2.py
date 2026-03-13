import sys
import copy
import heapq

input = sys.stdin.readline

INF = int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b,c))

start, end = map(int, input().split())

distance = [[INF,[start]] for _ in range(n+1)]
distance[start][0] = 0

def shortest(start):
  q = []
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)
    if distance[now][0] < dist:
      continue
    for i in graph[now]:
      cost = i[1] + dist
      if cost < distance[i[0]][0]:
        distance[i[0]][0] = cost
        route = copy.deepcopy(distance[now][1] + [i[0]])
        distance[i[0]][1] = route
        heapq.heappush(q, (cost, i[0]))

shortest(start)
print(distance[end][0])
print(len(distance[end][1]))
for i in distance[end][1]:
  print(i, end = " ")
