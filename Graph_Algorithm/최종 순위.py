import sys
import copy
from collections import deque
input = sys.stdin.readline

result = []
for _ in range(int(input())):
  n = int(input())
  before_rank = list(map(int , input().split()))
  indegree = [0]*(n+1)

  for i in range(n):
    now = before_rank[i]
    indegree[now] = i
  copy_indegree = copy.deepcopy(indegree)

  m = int(input())
  for i in range(m):
    a, b = map(int, input().split())

    if(indegree[a] < indegree[b]):
      copy_indegree[b] -= 1
      copy_indegree[a] += 1
    else:
      copy_indegree[a] -= 1
      copy_indegree[b] += 1

  q = deque()

  for i in range(1, n+1):
    if(copy_indegree[i] == 0):
      q.append(i)
  value = []
  
  
  for i in range(1, n+1):
    if(len(q) > 1):
      value = ["?"]
      break
    elif(len(q) == 0):
      value = ["IMPOSSIBLE"]
      break
    now = q.popleft()
    value.append(now)
    for j in range(1, n+1):
      if(j != now):
        copy_indegree[j] -= 1
        if(copy_indegree[j] == 0):
          q.append(j)
  
  result.append(value)

for item in result:
  for i in item:
    print(i, end = " ")
  print()
