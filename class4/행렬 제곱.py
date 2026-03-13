import sys
import copy

input = sys.stdin.readline

n, b = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(n):
    matrix[i][j] %= 1000

def multiply(a,b):
  c = [[0]*n for _ in range(n)]

  for i in range(n):
    for j in range(n):
      for k in range(n):
        c[i][j] += a[i][k] * b[k][j]
        c[i][j] %= 1000

  return c

result = copy.deepcopy(matrix)
b-= 1

while b > 0:
  if b % 2 == 1:
    result = multiply(result, matrix)
    b -= 1
  matrix = multiply(matrix, matrix)
  b //= 2

for i in range(n):
  for j in range(n):
    print(result[i][j], end = " ")
  print()