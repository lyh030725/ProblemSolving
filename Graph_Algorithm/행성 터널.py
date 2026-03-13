import sys
input = sys.stdin.readline

def find_parent(parent, x):
  if(parent[x] != x):
    parent[x] = find_parent(parent, parent[x])
  return parent[x]

def union(parent, x, y):
  a = find_parent(parent, x)
  b = find_parent(parent, y)
  if(a < b):
    parent[b] = a
  else:
    parent[a] = b

n = int(input())

parent = [0]*(n+1)

for i in range(1,n+1):
  parent[i] = i

point_x = []
point_y = []
point_z = []

for i in range(1, n+1):
  x, y, z = map(int , input().split())
  point_x.append((x,i))
  point_y.append((y,i))
  point_z.append((z,i))

point_x.sort()
point_y.sort()
point_z.sort()

edges = []
for i in range(n-1):
  value = abs(point_x[i][0] - point_x[i+1][0])
  edges.append((value, point_x[i][1], point_x[i+1][1]))

  value = abs(point_y[i][0] - point_y[i+1][0])
  edges.append((value, point_y[i][1], point_y[i+1][1]))

  value = abs(point_z[i][0] - point_z[i+1][0])
  edges.append((value, point_z[i][1], point_z[i+1][1]))

edges.sort()

result = 0
for edge in edges:
  cost, x, y = edge
  if(find_parent(parent, x) != find_parent(parent, y)):
    union(parent, x, y)
    result += cost

print(result)




