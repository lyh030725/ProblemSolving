n, m = map(int, input().split())

graph = []

for i in range(n):
  graph.append(list(map(int, input().split())))

destination = list(map(int , input().split()))

def find_parent(parent, x):
  if(x != parent[x]):
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union(parent, x, y):
  a = find_parent(parent,x)
  b = find_parent(parent,y)
  if(a < b):
    parent[b] = a
  else:
    parent[a] = b

parent = [0]*(n+1)

for i in range(1, n+1):
  parent[i] = i

for i in range(n):
  for j in range(n):
    if(graph[i][j] == 1):
      union(parent, i+1, j+1)

flag = True
res = find_parent(parent, destination[0])
for dest in destination:
  if(res != find_parent(parent, dest)):
    flag = False
    break

if(flag):
  print("YES")
else:
  print("NO")