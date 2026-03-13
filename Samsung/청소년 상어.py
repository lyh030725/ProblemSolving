import sys
input = sys.stdin.readline
from collections import deque
import copy

N = 4

graph = []

fishes = [0]*16
for i in range(16):
  fishes[i] = i+1

for i in range(N):
  data = list(map(int , input().split()))
  insert_data = []
  for j in range(0, 2*N, 2):
    if(i == 0 and j == 0):
      base_count = data[j]
      base_direct = data[j+1]
      fishes.remove(data[j])
    insert_data.append((data[j], data[j+1]))
  graph.append(insert_data)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(number):
  for i in range(N):
    for j in range(N):
      if(graph[i][j] == 0):
        continue
      if(graph[i][j][0] == number):
        return i, j
q = deque()

def move_shark(graph, fishes, x,y, direct, count):
  nx = x + dx[direct-1]
  ny = y + dy[direct-1]
  for i in range(3):
    copy_graph = copy.deepcopy(graph)
    copy_fish = copy.deepcopy(fishes)
    if(nx >= 0 and nx < N and ny >= 0 and ny < N):
      if(copy_graph[nx][ny] != 0):
        copy_graph[x][y] = 0
        copy_fish.remove(copy_graph[nx][ny][0])
        number = copy_graph[nx][ny][0]
        dir = copy_graph[nx][ny][1]
        copy_graph[nx][ny] = ("S", dir)
        q.append((copy_graph, (nx,ny), dir , copy_fish, count+number))
      nx += dx[direct-1]
      ny += dy[direct-1]
    else:
      break

def move_fish(graph, fishes):
  for fish in fishes:
    for i in range(8):
      x, y = find_fish(fish)
      dir = (graph[x][y][1]-1+i)%8
      nx = x + dx[dir]
      ny = y + dy[dir]
      if(nx >= 0 and nx < N and ny >= 0 and ny < N):
        if(graph[nx][ny] == 0):
          graph[x][y] = 0
          graph[nx][ny] = (fish, dir+1)
          break 
        if(graph[nx][ny][0] != "S"):
          graph[nx][ny], graph[x][y] = (fish, dir+1), graph[nx][ny]
          break
graph[0][0] = ("S", base_direct)
move_fish(graph, fishes)

move_shark(graph, fishes, 0, 0, base_direct, base_count)

result = 0

while q:
  graph, shark, direct, fishes, count = q.popleft()
  if(result < count):
    result = count
  move_fish(graph, fishes)
  move_shark(graph, fishes, shark[0], shark[1], direct, count)

print(result)