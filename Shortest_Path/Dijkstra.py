#다익스트라 알고리즘(기본 버전)
#특정한 한 지점에서 다른 지점들까지 가는 최단 거리
#O(N^2)

import sys
input = sys.stdin.readline

INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b, c = map(int , input().split())
  graph[a].append((b,c))


visited = [False]*(n+1)
distance = [INF] * (n+1)

def get_shortest_node():
  min_distance = INF
  min_index = 0
  for i in range(1, n+1):
    if(distance[i] < min_distance and visited[i] == False):
        min_distance = distance[i]
        min_index = i
  return min_index

def dijkstra(start):
  visited[start] = True
  distance[start] = 0
  for i in graph[start]:
    distance[i[0]] = i[1]
    
  for i in range(n-1):
    now = get_shortest_node()
    visited[now] = True
    for j in graph[now]:
      cost = distance[now] + j[1]
      if cost < distance[j[0]]:
        distance[j[0]] = cost

dijkstra(start)

for i in range(1, n+1):
  if(distance[i] == INF):
    print("INFINITY")
  else:
    print(distance[i])






