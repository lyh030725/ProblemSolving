import sys

n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

dx = [[0,0,0], [1,0,1], [1,2,2], [1,1,2],[0,0,1]]
dy = [[1,2,3], [0,1,1], [0,0,1], [0,1,1],[1,2,1]]

def all_case(start):
  cases = []
  x,y = start 
  for i in range(5):
    tmp_list = [start]
    flag = True
    for j in range(3):
      nx = x + dx[i][j]
      ny = y + dy[i][j]
      if(nx < 0 or nx >= n or ny < 0 or ny >= m):
        flag = False
        break
      tmp_list.append((nx,ny))
    if(flag):
      cases.append(tmp_list)

    tmp_list = [start]
    flag = True
    for j in range(3):
      nx = x - dx[i][j]
      ny = y - dy[i][j]
      if(nx < 0 or nx >= n or ny < 0 or ny >= m):
        flag = False
        break
      tmp_list.append((nx,ny))
    if(flag):
      cases.append(tmp_list)

    tmp_list = [start]
    flag = True

    for j in range(3):
      nx = x - dx[i][j]
      ny = y + dy[i][j]
      if(nx < 0 or nx >= n or ny < 0 or ny >= m):
        flag = False
        break
      tmp_list.append((nx,ny))
    if(flag):
      cases.append(tmp_list)
    
    tmp_list = [start]
    flag = True
    
    for j in range(3):
      nx = x + dx[i][j]
      ny = y - dy[i][j]
      if(nx < 0 or nx >= n or ny < 0 or ny >= m):
        flag = False
        break
      tmp_list.append((nx,ny))
    if(flag):
      cases.append(tmp_list)

    tmp_list = [start]
    flag = True

    for j in range(3):
      nx = x + dy[i][j]
      ny = y + dx[i][j]
      if(nx < 0 or nx >= n or ny < 0 or ny >= m):
        flag = False
        break
      tmp_list.append((nx,ny))
    if(flag):
      cases.append(tmp_list)
    
    tmp_list = [start]
    flag = True
    
    for j in range(3):
      nx = x - dy[i][j]
      ny = y - dx[i][j]
      if(nx < 0 or nx >= n or ny < 0 or ny >= m):
        flag = False
        break
      tmp_list.append((nx,ny))
    if(flag):
      cases.append(tmp_list)
    
    tmp_list = [start]
    flag = True

    for j in range(3):
      nx = x - dy[i][j]
      ny = y + dx[i][j]
      if(nx < 0 or nx >= n or ny < 0 or ny >= m):
        flag = False
        break
      tmp_list.append((nx,ny))
    if(flag):
      cases.append(tmp_list)

    tmp_list = [start]
    flag = True
    
    for j in range(3):
      nx = x + dy[i][j]
      ny = y - dx[i][j]
      if(nx < 0 or nx >= n or ny < 0 or ny >= m):
        flag = False
        break
      tmp_list.append((nx,ny))
    if(flag):
      cases.append(tmp_list)

  return cases
  
result = 0
for i in range(n):
  for j in range(m):
    cases = all_case((i,j))
    for case in cases:
      count = 0
      for k in range(4):
        count += graph[case[k][0]][case[k][1]]
      result = max(result, count)

print(result)