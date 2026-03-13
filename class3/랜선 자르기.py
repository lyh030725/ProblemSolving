import sys
import copy
input = sys.stdin.readline

k, n = map(int, input().split())

data = []

for i in range(k):
  data.append(int(input()))

start = 1
end = max(data)
result = 0

while True:
  if(start > end):
    print(result)
    break

  mid = (start+end)//2

  copy_data = copy.deepcopy(data)

  for j in range(k):
    copy_data[j] //= mid

  tmp = sum(copy_data)

  if tmp >= n:
    result = mid
    start = mid+1
  else:
    end = mid-1