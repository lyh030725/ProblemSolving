import sys

input = sys.stdin.readline

INF = int(1e9)

n, m, r = map(int, input().split())

distance = [[INF]*(n+1) for _ in range(n+1)]
item = [0] + list(map(int, input().split()))

for i in range(1, n+1):
  distance[i][i] = 0

for i in range(r):
  a,b,c = map(int, input().split())
  distance[a][b] = c
  distance[b][a] = c

for k in range(1, n+1):
  for i in range(1, n+1):
    for j in range(1, n+1):
      distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

result = 0
for i in range(1, n+1):
  sum = 0
  for j in range(1, n+1):
    if distance[i][j] <= m:
      sum += item[j]
  result = max(result, sum)

print(result)