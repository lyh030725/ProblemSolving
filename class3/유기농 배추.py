import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, cabbage):
  y, x = cabbage
  visited[y][x] = 1

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if(nx >= 0 and nx < m and ny >= 0 and ny < n):
      if(graph[ny][nx] == 1 and visited[ny][nx] == 0):
        dfs(graph, (ny,nx))

for t in range(int(input())):
  m, n, k = map(int, input().split())

  graph = [[0]*m for _ in range(n)]
  visited = [[0]*m for _ in range(n)]
  
  cabbages = []
  count = 0

  for i in range(k):
    x, y = map(int, input().split())
    cabbages.append((y,x))
    graph[y][x] = 1

  for cabbage in cabbages:
    y,x = cabbage
    if(visited[y][x] == 0):
      dfs(graph, cabbage)
      count += 1

  print(count)


  
