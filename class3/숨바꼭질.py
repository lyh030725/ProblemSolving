from collections import deque

n, k = map(int, input().split())

q = deque()
visited = [0]*100001

q.append(n)

while q:
  now = q.popleft()

  if(now == k):
    print(visited[k])
    break

  for i in (now+1, now-1, 2*now):
    if(0 <= i <= 100000 and visited[i] == 0):
      visited[i] = visited[now] + 1
      q.append(i)