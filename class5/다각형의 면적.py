import sys
import math

input = sys.stdin.readline

n = int(input())

points = []

for i in range(n):
  x,y = map(int, input().split())
  points.append((x,y))

cuml = 0
for i in range(n):
  if i == n-1:
    cuml += points[i][0]*points[0][1] - points[i][1]*points[0][0]
    break
  cuml += points[i][0]*points[i+1][1] - points[i][1]*points[i+1][0]

result = abs(cuml)/2

print(f"{result:.1f}")