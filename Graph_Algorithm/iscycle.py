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

v, e = map(int , input().split())

parent = [0] * (v+1)

for i in range(1, v+1):
  parent[i] = i

iscycle = False

for i in range(e):
  a, b = map(int , input().split())
  if(find_parent(parent, a) == find_parent(parent,b)):
    iscycle = True
    break
  else:
    union_parent(parent, a, b)

if(iscycle):
  print("사이클이 발생했습니다")
else:
  print("사이클이 발생하지 않았습니다")
