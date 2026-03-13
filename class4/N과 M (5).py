import sys
from itertools import permutations
input = sys.stdin.readline

n, m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

cases = permutations(data, m)

for case in cases:
  for i in range(m):
    if(i == m-1):
      print(case[i])
      break
    print(case[i], end = " ")