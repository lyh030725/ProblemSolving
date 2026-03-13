import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

node = {}
input_node = []

while True:
  try:
    n = int(input())
    input_node.append(n)
  except:
    break

root = input_node[0]

def insert_node(root, child):
  if(root not in node):
    if root > child:
      node[root] = [child, None]
    else:
      node[root] = [None, child]
    return

  if root > child:
    if(node[root][0] == None):
      node[root][0] = child
    else:
      insert_node(node[root][0], child)
  else:
    if(node[root][1] == None):
      node[root][1] = child
    else:
      insert_node(node[root][1], child)

for i in range(1, len(input_node)):
  insert_node(root, input_node[i])

def post_order(root):
  if(root in node):
    if(node[root][0] != None):
      post_order(node[root][0])
    if(node[root][1] != None):
      post_order(node[root][1])
  print(root)
  
post_order(root)