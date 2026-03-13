import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(1,n+1):
  data.append(i)

cases = combinations_with_replacement(data, m)

for case in cases:
  for i in range(m):
    if(i == m-1):
      print(case[i])
      break
    print(case[i], end = " ")