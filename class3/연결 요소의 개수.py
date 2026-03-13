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

n, m = map(int, input().split())

parent = [0]*(n+1)

for i in range(1, n+1):
  parent[i] = i

for i in range(m):
  a, b = map(int, input().split())
  union(parent, a, b)

result = set()
for i in range(1, n+1):
  result.add(find_parent(parent, i))

print(len(result))