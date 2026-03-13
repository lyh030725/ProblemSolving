import sys

input = sys.stdin.readline

C, N = map(int, input().split())

INF = int(1e9)
dp = [[INF]*1001 for _ in range(N)]

for i in range(N):
  dp[i][0] = 0

cost = []
gain = []

for i in range(N):
  c, g = map(int, input().split())
  cost.append(c)
  gain.append(g)

for c in range(1, 1001):
  tmp = c/gain[0]
  if tmp == c//gain[0]:
    dp[0][c] = int(tmp)*cost[0]
  else:
    dp[0][c] = (int(tmp)+1)*cost[0]

for i in range(N):
  for c in range(1, 1001):
    tmp = c/gain[i]
    if tmp == c//gain[i]:
      iter_num = int(tmp)
    else:
      iter_num = int(tmp)+1

    for j in range(1, iter_num+1):
      if c >= j*gain[i]:
        dp[i][c] = min(dp[i][c], dp[i-1][c], dp[i-1][c-j*gain[i]] + j*cost[i])
      else:
        dp[i][c] = min(dp[i][c], dp[i-1][c], j*cost[i])

print(dp[N-1][C])