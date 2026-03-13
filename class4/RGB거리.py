import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
data = []
INF = int(1e9)

for i in range(n):
  r,g,b = map(int, input().split())
  data.append(r)
  data.append(g)
  data.append(b)

dp = [INF]*3*n
dp[0] = data[0]
dp[1] = data[1]
dp[2] = data[2]

for i in range(3,3*n):
  if(i % 3 == 0):
    dp[i] = min(dp[i-2]+data[i], dp[i-1]+data[i])
  elif(i % 3 == 1):
    dp[i] = min(dp[i-4]+data[i], dp[i-2]+data[i])
  else:
    dp[i] = min(dp[i-5]+data[i], dp[i-4]+data[i])

print(min(dp[-1], dp[-2], dp[-3]))