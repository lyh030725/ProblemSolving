import sys
input = sys.stdin.readline

for t in range(int(input())):
  num = int(input())
  dp = [0]*(num+1)
  if(num == 1 or num == 2):
    print(num)
    continue
  elif(num == 3):
    print(4)
    continue
  dp[1] = 1
  dp[2] = 2
  dp[3] = 4

  for i in range(4, num+1):
    dp[i] = dp[i-3]+dp[i-2]+dp[i-1]

  print(dp[-1])