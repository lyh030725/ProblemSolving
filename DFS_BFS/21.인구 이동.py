import sys
import copy
from collections import deque
input = sys.stdin.readline

n, l, r = map(int,input().split())
population = []
country = []
q = deque([])

for i in range(n):
  population.append(list(map(int, input().split())))
  for j in range(n):
    country.append((i,j))



count = 0

dx = [-1,0,1,0]
dy = [0,-1,0,1]
while True:
  copy_country = copy.deepcopy(country)
  alliances = []
  while len(copy_country) > 0:
    alliance = set()
    x, y = copy_country.pop()
    q = deque([(population[x][y], x, y)])
    while q:
      popul, row, col = q.popleft()
      for i in range(4):
        nx = row + dx[i]
        ny = col + dy[i]
        if(nx < n and nx >= 0 and ny < n and ny >=0):
          if(l <= abs(popul-population[nx][ny]) <= r and (nx,ny) in copy_country):
            alliance.add((row,col))
            alliance.add((nx,ny))
            copy_country.remove((nx,ny))
            q.append((population[nx][ny], nx, ny))
    if(len(alliance) == 0):
      continue
    alliances.append(alliance)
    popul_sum = 0
    for point in alliance:
      x, y = point
      popul_sum += population[x][y]

    result = int(popul_sum/len(alliance))

    for point in alliance:
      x, y = point
      population[x][y] = result

  if(len(alliances) == 0):
    break

  count += 1
  
print(count)



    



