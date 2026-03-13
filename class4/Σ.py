import sys
import math

input = sys.stdin.readline

n = int(input())

X = 1_000_000_007

def mul(num, exp):
  result = 1
  while exp > 0:
    if exp % 2 == 1:
      exp -= 1
      result *= num
    num *= num
    num %= X
    exp //= 2
  return result

def find_reverse(num):
  return mul(num, X-2)%X

sum = 0
for i in range(n):
  b,a = map(int, input().split())
  b,a = b//math.gcd(a,b), a//math.gcd(a,b)
  b_ = find_reverse(b)
  sum += a*b_%X

print(sum%X)