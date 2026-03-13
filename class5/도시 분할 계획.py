import sys

input = sys.stdin.readline

n, m = map(int, input().split())

def find_parent(x, parent):
  if x != parent[x]:
    parent[x] = find_parent(parent[x],parent)
  return parent[x]

def union(x,y, parent):
  a = find_parent(x, parent)
  b = find_parent(y, parent)
  if a < b:
    parent[b] = a
  else:
    parent[a] = b

parent = [0]*(n+1)
for i in range(1, n+1):
  parent[i] = i

edges = []
for i in range(m):
  a,b,c = map(int, input().split())
  edges.append((c,a,b))

edges.sort()
last = 0
count = 0

for edge in edges:
  c,a,b = edge
  if find_parent(a, parent) != find_parent(b, parent):
    union(a,b,parent)
    last = c
    count += c
    
print(count-last)