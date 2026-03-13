import sys
import copy
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

n = int(input())

graph = []
for i in range(n):  
  graph.append(list(map(int, input().split())))

distance = [[INF]*n for _ in range(n)]

for i in range(n):
  for j in range(n):
    if(graph[i][j] == 1):
      distance[i][j] = 1

for k in range(n):
  for i in range(n):
    for j in range(n):
      distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

for i in range(n):
  for j in range(n):
    if(distance[i][j] != INF):
      print(1, end = " ")
    else:
      print(0, end = " ")
  print()