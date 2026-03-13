import sys

input = sys.stdin.readline

n, k = map(int, input().split())

unit = []

for i in range(n):
  unit.append(int(input()))

count = 0

for i in range(n-1, -1, -1):
  if(k//unit[i] > 0):
    count += k//unit[i]
    k %= unit[i]

print(count)