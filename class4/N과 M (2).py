import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())

data = []
for i in range(1,n+1):
  data.append(i)

cases = combinations(data, m)

for case in cases:
  for i in range(m):
    if(i == m-1):
      print(case[i])
      break
    print(case[i], end = " ")