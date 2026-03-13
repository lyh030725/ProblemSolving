a = input()
b = input()

length1 = len(a)
length2 = len(b)

dp = [[0]*length1 for _ in range(length2)]

if(a[0] == b[0]):
  dp[0][0] = 1

for i in range(1, length1):
  if(b[0] == a[i]):
    dp[0][i] = 1
  else:
    dp[0][i] = dp[0][i-1]

for i in range(1, length2):
  if(a[0] == b[i]):
    dp[i][0] = 1
  else:
    dp[i][0] = dp[i-1][0]


for i in range(1, length2):
  for j in range(1, length1):
    if(a[j] == b[i]):
      dp[i][j] = dp[i-1][j-1]+1
    else:
      dp[i][j] = max(dp[i-1][j], dp[i][j-1])
      
print(dp[length2-1][length1-1])