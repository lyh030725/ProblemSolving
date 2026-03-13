n = int(input())

m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

visited = [0]*(n+1)
result = []

def dfs(graph, start):
  visited[start] = 1
  result.append(start)
  for now in graph[start]:
    if(visited[now] == 0):
      dfs(graph, now)

dfs(graph, 1)

print(len(result)-1)