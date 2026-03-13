import sys
input = sys.stdin.readline

for t in range(int(input())):
  n = int(input())

  data = []
  for i in range(2):
    data.append(list(map(int, input().split())))

  dp = [[0]*n for _ in range(2)]

  dp[0][0] = data[0][0]
  dp[1][0] = data[1][0]

  if(n > 1):
    dp[0][1] = data[1][0]+data[0][1]
    dp[1][1] = data[0][0]+data[1][1]

  for i in range(2, n):
    val1 = dp[0][i-1]+data[1][i]
    val2 = dp[1][i-1]+data[0][i]
    val3 = dp[0][i-2]+data[1][i]
    val4 = dp[1][i-2]+data[0][i]
    dp[0][i] = max(val2, val4)
    dp[1][i] = max(val1, val3)

  
  print(max(dp[0][-1], dp[1][-1]))