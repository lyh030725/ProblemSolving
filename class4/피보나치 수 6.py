matrix = [[1,1],[1,0]]
n = int(input())-1
p = 1000000007

def matrix_product(a,b):
  new_matrix = [[0]*2 for _ in range(2)]
  for i in range(2):
    for j in range(2):
      for k in range(2):
        new_matrix[i][j] += a[i][k] * b[k][j]
        new_matrix[i][j] %= p
  return new_matrix

result = [[1]*2 for _ in range(2)]

while n > 0:
  if n % 2 == 1:
    result = matrix_product(result, matrix)
    n -= 1

  matrix = matrix_product(matrix, matrix)
  n //= 2

print(result[0][1]%1000000007)