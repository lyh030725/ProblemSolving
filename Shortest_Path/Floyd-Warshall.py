#플로이드 워셜 알고리즘
#모든 지점에서 다른 모든 지점까지의 최단 거리
#O(N^3): 노드 개수 100이하인 경우

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

distance = [[INF]*(n+1) for _ in range(n+1)]

for a in range(1, n+1):
  for b in range(1, n+1):
    if(a==b):
      distance[a][b] = 0

for i in range(m):
  a, b, c = map(int , input().split())
  distance[a][b] = c



for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(1, n+1):
  for j in range(1, n+1):
    if(distance[i][j] == INF):
      print("INFINITY")
    else:
      print(distance[i][j], end=" ")
  print()