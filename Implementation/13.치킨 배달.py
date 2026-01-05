import sys
import itertools
input = sys.stdin.readline

n, m = map(int, input().split())

data = [[] for _ in range(n)]

for i in range(n):
  x = list(map(int , input().split()))
  for j in range(n):
    data[i].append(x[j])

chickens = []
for i in range(n):
  for j in range(n):
    if(data[i][j] == 2):
      chicken = []
      for x in range(n):
        for y in range(n):
          if(data[x][y] == 1):
            chicken.append(abs(i-x) + abs(j-y))
      chickens.append(chicken)

house_num = len(chickens[0])
min_count = int(1e9)

combinations = list(itertools.combinations(chickens, m))
for combination in combinations:
  min_list = []
  for k in range(house_num):
    num_list = []
    for chicken in combination:
      num_list.append(chicken[k])
    min_list.append(min(num_list))
  min_count = min(min_count, sum(min_list))

print(min_count)