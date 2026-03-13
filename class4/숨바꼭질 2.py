from collections import deque

n, k = map(int, input().split())
INF = int(1e9)

q = deque()
q.append(n)

visited = [[INF,0] for _ in range(100001)]
visited[n] = [0,1]

while q:
  now = q.popleft()

  if now == k:
    print(visited[now][0])
    print(visited[now][1])
    break

  
  if(now-1 >= 0):
    if visited[now-1][0] > visited[now][0]:
      visited[now-1][0] = visited[now][0] + 1
      visited[now-1][1] += 1
      q.append(now-1)
  
  if(now+1 <= 100000):
    if visited[now+1][0] > visited[now][0]:
      visited[now+1][0] = visited[now][0] + 1
      visited[now+1][1] += 1
      q.append(now+1)

  if(2*now <= 100000):
    if visited[2*now][0] > visited[now][0]:
      visited[2*now][0] = visited[now][0] + 1
      visited[2*now][1] += 1
      q.append(2*now)
