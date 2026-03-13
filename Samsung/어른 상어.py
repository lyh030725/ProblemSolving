import sys
import copy
input = sys.stdin.readline

n, m, k = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

sharks = []

directs = list(map(int, input().split()))

for x in range(m):
  for i in range(n):
    for j in range(n):
      if(graph[i][j] == x+1):
        graph[i][j] = (x+1, k)
        sharks.append((i, j, directs[x]-1))

priority = []

for i in range(m):
  data = []
  for j in range(4):
    tmp = list(map(int, input().split()))
    for l in range(4):
      tmp[l] -= 1
    data.append(tmp)
  priority.append(data)

def pass_time():
  for i in range(n):
    for j in range(n):
      if(graph[i][j] != 0):
        graph[i][j] = (graph[i][j][0], graph[i][j][1]-1)
        if(graph[i][j][1] == 0):
          graph[i][j] = 0

def move_shark(graph):
  copy_graph = copy.deepcopy(graph)
  for i in range(m):
    flag = True
    if(sharks[i] == 0):
      continue
    x,y,dir = sharks[i]
    for choice in priority[i][dir]:
      nx = x + dx[choice]
      ny = y + dy[choice]
      if(nx >= 0 and nx < n and ny >= 0 and ny < n):
        if(graph[nx][ny] == 0):
          if(copy_graph[nx][ny] != 0):
            if(copy_graph[nx][ny][0] < i+1):
              sharks[i] = 0
              flag = False
              break
          copy_graph[nx][ny] = (i+1, k+1)
          sharks[i] = (nx, ny, choice)
          flag = False
          break
    if(flag == False):
      continue
    for choice in priority[i][dir]:
      nx = x + dx[choice]
      ny = y + dy[choice]
      if(nx >= 0 and nx < n and ny >= 0 and ny < n):
        if(graph[nx][ny] != 0):
          if(graph[nx][ny][0] == i+1):
              copy_graph[nx][ny] = (i+1, k+1)
              sharks[i] = (nx, ny, choice)
              break
  return copy_graph

def end_game():
  count = 0
  for shark in sharks:
    if(shark == 0):
      continue
    count += 1
  if(count == 1):
    return True
  return False

sec = 0
while True:
  if(sec > 1000):
    print(-1)
    break
  if(end_game()):
    print(sec)
    break

  graph = move_shark(graph)
  pass_time()
  sec += 1
