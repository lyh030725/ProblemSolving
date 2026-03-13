import sys

input = sys.stdin.readline

n = int(input())

graph = dict()

for i in range(n):
  key, left, right = input().split()
  graph[key] = (left,right)

def preorder(start):
  if(start != "."):
    print(start, end = "")
    preorder(graph[start][0])
    preorder(graph[start][1])

def inorder(start):
  if(start != "."):
    inorder(graph[start][0])
    print(start, end="")
    inorder(graph[start][1])

def postorder(start):
  if(start != "."):
    postorder(graph[start][0])
    postorder(graph[start][1])
    print(start, end="")

preorder("A")
print()
inorder("A")
print()
postorder("A")