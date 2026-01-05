def find_parent(parent, x):
  if(parent[x] != x):
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, x, y):
  a = find_parent(parent, x)
  b = find_parent(parent, y)
  if(a < b):
    parent[b] = a
  else:
    parent[a] = b


v, e = map(int, input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

edges = []

for i in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()
result = 0

for edge in edges:
  cost, a, b = edge
  if(find_parent(parent, a) != find_parent(parent, b)):
    result += cost
    union_parent(parent, a, b)

print(result)

