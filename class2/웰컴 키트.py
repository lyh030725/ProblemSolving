n = int(input())

sizes = list(map(int, input().split()))

t, p = map(int, input().split())

count = 0
for size in sizes:
  while size > 0:
    size -= t
    count += 1

print(count)

print(n//p, n%p)