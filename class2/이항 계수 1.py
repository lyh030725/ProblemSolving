a,b = map(int, input().split())

def fact(n):
  count = 1
  for i in range(1, n+1):
    count *= i
  return count

print(fact(a)//(fact(b)*fact(a-b)))