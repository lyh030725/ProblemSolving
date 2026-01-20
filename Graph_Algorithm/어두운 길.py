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

n, m = map(int, input().split())

parent = [0]*n

for i in range(n):
  parent[i] = i

edges = []
for i in range(m):
  x, y, cost = map(int, input().split())
  edges.append((cost, x, y))

edges.sort()
count = 0
for edge in edges:
  cost, x, y = edge
  if(find_parent(parent, x) != find_parent(parent,y)):
    union(parent, x, y)
  else:
    count += cost

print(count)
