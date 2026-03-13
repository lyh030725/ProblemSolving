dp = [0]*(101)

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2 
for t in range(int(input())):
  n = int(input())
  if(n <= 5):
    print(dp[n])
  else:
    for i in range(6, n+1):
      dp[i] = dp[i-1] + dp[i-5]
    print(dp[n])