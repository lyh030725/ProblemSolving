import sys
from itertools import combinations_with_replacement
input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

cases = list(set(combinations_with_replacement(data, m)))
cases.sort()

for case in cases:
  for i in range(m):
    if(i == m-1):
      print(case[i])
      break
    print(case[i], end = " ")