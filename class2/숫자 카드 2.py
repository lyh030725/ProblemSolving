import bisect

n = int(input())

data = list(map(int, input().split()))

data.sort()
m = int(input())
result = []

data2 = list(map(int, input().split()))
for i in range(m):
  num = data2[i]
  result.append(bisect.bisect_right(data, num) - bisect.bisect_left(data, num))

for res in result:
  print(res, end = " ")
