num = int(input())

INF = int(1e9)
dp = [INF]*(num+1)
dp[0] = 0
for i in range(1, num+1):
  for j in range(1, num+1):
    tmp = j*j
    if(tmp > i):
      break
    dp[i] = min(dp[i], dp[i-tmp]+1)

print(dp[-1])