dp = [0]*41

n = int(input())

arr = []
for i in range(n):
  arr.append(int(input()))

zero_count = 0
one_count = 0
def fibonacci(n):
  global zero_count
  global one_count
  if(n == 0):
    zero_count += 1
    return 0
  if(n == 1):
    one_count += 1
    return 1
  if(dp[n] != 0):
    return dp[n]
  dp[n] = fibonacci(n-1)+ fibonacci(n-2)
  return dp[n]

for n in arr:
  zero_count = 0
  one_count = 0
  fibonacci(n)
  print(zero_count, one_count)