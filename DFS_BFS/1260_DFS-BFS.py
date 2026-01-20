from collections import deque
#n: 정점의 개수 , m: 간선의 개수, start: 시작점
n, m, start = map(int , input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m):
  a , b = map(int , input().split())
  graph[a][b] = 1
  graph[b][a] = 1

visited = [0] * (n+1)

def dfs(graph, visited, start):
  visited[start] = 1
  print(start, end=" ")
  for i in range(n+1):
    if(graph[start][i] == 1 and visited[i] == 0):
      dfs(graph, visited, i)

dfs(graph, visited, start)

print()
visited = [0] * (n+1)

def bfs(graph, visited, start):
  visited[start] = 1
  queue = deque([start])
  while queue:
    start = queue.popleft()
    print(start, end = " ")
    for i in range(n+1):
      if(graph[start][i] == 1 and visited[i] == 0):
        visited[i] = 1
        queue.append(i)

bfs(graph, visited, start)
