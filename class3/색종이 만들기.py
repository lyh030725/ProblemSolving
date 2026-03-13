import sys
input = sys.stdin.readline

n = int(input())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

white_count = 0
blue_count = 0

def check(graph):
  global white_count
  global blue_count
  
  m = len(graph)
  value = graph[0][0]
  flag = True
  for i in range(m):
    for j in range(m):
      if(graph[i][j] != value):
        flag = False
        break
    if(not flag):
      break

  if(flag and value == 1):
    blue_count += 1
    return
  elif(flag and value == 0):
    white_count += 1
    return
  else:
    tmp = []
    for i in range(m//2):
      tmp_list = []
      for j in range(m//2):
        tmp_list.append(graph[i][j])
      tmp.append(tmp_list)
    check(tmp)

    tmp = []
    for i in range(m//2):
      tmp_list = []
      for j in range(m//2, m):
        tmp_list.append(graph[i][j])
      tmp.append(tmp_list)
    check(tmp)

    tmp = []
    for i in range(m//2, m):
      tmp_list = []
      for j in range(m//2):
        tmp_list.append(graph[i][j])
      tmp.append(tmp_list)
    check(tmp)

    tmp = []
    for i in range(m//2, m):
      tmp_list = []
      for j in range(m//2, m):
        tmp_list.append(graph[i][j])
      tmp.append(tmp_list)
    check(tmp)



check(graph)

print(white_count)
print(blue_count)
