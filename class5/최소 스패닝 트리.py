import sys

input = sys.stdin.readline

sys.setrecursionlimit(100000)

def find_parent(x, parent):
  if x != parent[x]:
    parent[x] = find_parent(parent[x], parent)
  return parent[x]

def union(x,y, parent):
  a = find_parent(x, parent)
  b = find_parent(y, parent)
  if a < b :
    parent[b] = a
  else:
    parent[a] = b

v, e = map(int, input().split())
edges = []

for i in range(e):
  a,b,c = map(int, input().split())
  edges.append((c,a,b))

edges.sort()

parent = [0]*(v+1)

for i in range(1, v+1):
  parent[i] = i

res = 0

for edge in edges:
  c,a,b = edge
  if find_parent(a, parent) != find_parent(b, parent):
    union(a,b, parent)
    res += c

print(res)