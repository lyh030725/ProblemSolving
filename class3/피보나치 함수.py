import sys

input = sys.stdin.readline

fibo = [-1]*(41)
fibo[0] = (1,0)
fibo[1] = (0,1)

def fibonacci(n):
  if(fibo[n] != -1):
    return fibo[n]
  fibo[n] = (fibonacci(n-1)[0] + fibonacci(n-2)[0], fibonacci(n-1)[1] + fibonacci(n-2)[1])
  return fibo[n]


for t in range(int(input())):
  num = int(input())
  zero, one = fibonacci(num)
  print(zero, one)