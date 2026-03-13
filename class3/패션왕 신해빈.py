from itertools import combinations
import sys
input = sys.stdin.readline

for t in range(int(input())):
  n = int(input())

  data = []
  kinds = set()
  for i in range(n):
    name, kind = map(str, input().split())
    data.append((name, kind))
    kinds.add(kind)

  category = []
  for kind in kinds:
    count = 0
    for j in range(n):
      if(kind == data[j][1]):
        count += 1
    category.append(count)

  length = len(kinds)

  result = 1
  for item in category:
    result *= item+1

  print(result-1)