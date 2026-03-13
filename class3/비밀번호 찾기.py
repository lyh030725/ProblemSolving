import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().split())

data = []

for i in range(n):
  site, password = map(str, input().strip().split())
  data.append((site, password))

data.sort()
 

for i in range(m):
  input_site = input().strip()
  print(data[bisect.bisect_left(data, input_site, key=lambda x:(x[0]))][1])