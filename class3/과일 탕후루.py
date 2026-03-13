n = int(input())

data = list(map(int, input().split()))

left = 0
result = 0
count = {}

for right in range(n):
  now = data[right]
  if now in count:
    count[now] += 1
  else:
    count[now] = 1
  
  while len(count) > 2:
    remove = data[left]
    count[remove] -= 1
    if(count[remove] == 0):
      del count[remove]
    left += 1
  
  result = max(result, right-left+1)

print(result)