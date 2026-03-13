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

truth_data = list(map(int, input().split()))
truth_num = truth_data[0]
truth_parent = 0

if(truth_num > 0):
  truth_data = truth_data[1:]

for i in range(truth_num-1):
  union(parent, truth_data[i], truth_data[i+1])

data = []
for i in range(m):
  party = list(map(int, input().split()))
  party_num = party[0]
  party = party[1:]
  data.append(party)
  for j in range(party_num-1):
    union(parent, party[j], party[j+1])

if(truth_num > 0):
  truth_parent = find_parent(parent, truth_data[0])

count = 0
for party in data:
  flag = True
  for x in party:
    if(find_parent(parent, x) == truth_parent):
      flag = False
      break
  if(flag):
    count += 1

print(count)