import sys

input = sys.stdin.readline
sys.setrecursionlimit(15000)

n,r,q = map(int, input().split())

connect = [[] for _ in range(n+1)]


for i in range(n-1):
  u,v = map(int, input().split())
  connect[u].append(v)
  connect[v].append(u)

query = []

for i in range(q):
  query.append(int(input()))

def make_tree(currentNode, parent):
  for node in connect[currentNode]:
    if node != parent:
      children[currentNode].append(node)
      make_tree(node, currentNode)

def count_subtree(currentNode):
  size[currentNode] = 1
  for child in children[currentNode]:
    count_subtree(child)
    size[currentNode] += size[child]

children = [[] for _ in range(n+1)]
size = [0]*(n+1)
make_tree(r, -1)
count_subtree(r)

for qry in query:
  print(size[qry])