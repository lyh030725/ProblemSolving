from collections import deque

n, k = map(int, input().split())

INF = int(1e9)
distance = [INF]*100001

q = deque()

q.append((n,0))
distance[n] = 0
result = []

while q:
  now, dist = q.popleft()

  tmp = now-1
  if(tmp >= 0):
    if(dist+1 < distance[tmp]):
      q.append((tmp, dist+1))
      distance[tmp] = dist+1
  
  tmp = now+1
  if(tmp <= 100000):
    if(dist+1 < distance[tmp]):
      q.append((tmp, dist+1))
      distance[tmp] = dist+1
  
  tmp = 2*now
  if(tmp <= 100000):
    if(dist < distance[tmp]):
      q.append((tmp, dist))
      distance[tmp] = dist

print(distance[k])