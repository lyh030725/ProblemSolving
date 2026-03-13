from collections import deque

result = []
for t in range(int(input())):
  n , m = map(int, input().split())
  data = list(map(int, input().split()))
  q = deque()
  for i in range(n):
    data[i] = (data[i], i)
    q.append(data[i])
  
  count = 0
  while q:
    max_value = max(q)[0]
    important, index = q.popleft()
    if(important < max_value):
      q.append((important, index))
      continue
    count += 1
    if(index == m):
      result.append(count)
      break

for res in result:
  print(res)