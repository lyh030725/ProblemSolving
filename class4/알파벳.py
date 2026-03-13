import sys

input = sys.stdin.readline

n,m = map(int, input().split())

graph = []

for i in range(n):
  data = input().rstrip()
  tmp = []
  for char in data:
    tmp.append(char)
  graph.append(tmp)

def dfs(start, dist):
  global result
  x, y = start
  result = max(result, dist)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if(0 <= nx < n and 0 <= ny < m):
      char = ord(graph[nx][ny]) - ord("A")
      if(visited[char] == 0):
        visited[char] = 1
        dfs((nx,ny), dist+1)
        visited[char] = 0
  
dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
visited = [0]*26

visited[ord(graph[0][0]) - ord("A")] = 1
dfs((0,0), 1)

print(result)