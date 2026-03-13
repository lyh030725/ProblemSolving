import sys
from collections import deque

input = sys.stdin.readline

for t in range(int(input())):
  a, b = map(int, input().split())
  q = deque()
  q.append((a, ""))
  visited = [0]*10001
  visited[a] = 1

  while q:
    now, result = q.popleft()
    
    if(now == b):
      print(result)
      break

    tmp = (2*now)%10000
    if(visited[tmp] == 0):
      q.append((tmp, result+"D"))
      visited[tmp] = 1

    tmp = now-1
    if(tmp < 0):
      tmp = 9999
    if(visited[tmp] == 0):
      q.append((tmp, result+"S"))
      visited[tmp] = 1

    tmp = (now%1000*10)+(now//1000)
    if(visited[tmp] == 0):
      q.append((tmp, result+"L"))
      visited[tmp] = 1

    tmp = (now%10*1000)+(now//10)
    if(visited[tmp] == 0):
      q.append((tmp, result+"R"))
      visited[tmp] = 1