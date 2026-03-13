import sys
import copy

input = sys.stdin.readline

r, c, t = map(int, input().split())

graph = []
air_fresher = []
spot = []

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

def air_fresh(pos):
  top = pos[0]
  buttom = pos[1]
  copy_graph = copy.deepcopy(graph)

  x = top[0]
  y = top[1]
  for i in [(0,1), (-1,0), (0,-1), (1,0)]:
    while 0 <= x < r and 0 <= y < c:
      nx = x + i[0]
      ny = y + i[1]
      if nx == top[0] and ny == top[1]:
        break

      if 0 <= nx < r and 0 <= ny < c:
        if copy_graph[nx][ny] != -1:
          if graph[x][y] != -1:
            copy_graph[nx][ny] = graph[x][y]
          else:
            copy_graph[nx][ny] = 0
      else:
        break
      x = nx
      y = ny
  
  x = buttom[0]
  y = buttom[1]
  for i in [(0,1), (1,0), (0,-1), (-1,0)]:
    while 0 <= x < r and 0 <= y < c:
      nx = x + i[0]
      ny = y + i[1]
      if nx == buttom[0] and ny == buttom[1]:
        break

      if 0 <= nx < r and 0 <= ny < c:
        if copy_graph[nx][ny] != -1:
          if graph[x][y] != -1:
            copy_graph[nx][ny] = graph[x][y]
          else:
            copy_graph[nx][ny] = 0
      else:
        break
      x = nx
      y = ny

  return copy_graph

def spread():
  copy_graph = copy.deepcopy(graph)

  for x in range(r):
    for y in range(c):
      value = copy_graph[x][y]//5

      if value > 0:
        for i in range(4):
          nx = x + dx[i]
          ny = y + dy[i]
          if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] > -1:
              graph[nx][ny] += value
              graph[x][y] -= value



for i in range(r):
  graph.append(list(map(int, input().split())))
  for j in range(c):
    if graph[i][j] == -1:
      air_fresher.append((i,j))

result = 0

for _ in range(t):
  spread()
  graph = air_fresh(air_fresher)

for i in range(r):
  for j in range(c):
    if graph[i][j] > 0:
      result += graph[i][j]

print(result)