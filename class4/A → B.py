from collections import deque

a, b = map(int, input().split())

q = deque()
q.append((a,1))

while q:
  now, count = q.popleft()

  next = now*2
  if(next == b):
    print(count+1)
    exit()

  if(next < b):
    q.append((next, count+1))

  next = now*10+1

  if(next == b):
    print(count+1)
    exit()

  if(next < b):
    q.append((next, count+1))
  
print(-1)