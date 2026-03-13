import sys
input = sys.stdin.readline

n = int(input())

data = list(map(int, input().split()))

dp = [1]*n

for i in range(1, n):
  for j in range(i-1, -1, -1):
    if(data[j] < data[i]):
      dp[i] = max(dp[i], dp[j]+1)

print(max(dp))