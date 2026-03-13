n = int(input())

graph = [[" ", " ", "*", " ", " "], [" ", "*", " ", "*", " "], ["*", "*", "*", "*", "*"]]
after = []

def star(n_, before):
  global n
  global after
  width = len(before[0])
  after = [[" "]*(2*width+1) for _ in range(2*n_)]
  for i in range(n_):
    for j in range(n_, n_+width):
      after[i][j] = before[i][j-n_]

  for i in range(n_, 2*n_):
    after[i][:width] = before[i-n_]
    after[i][width+1:] = before[i-n_]

  if(2*n_ == n):
    return

  star(2*n_, after)


if (n==3):
  result = graph
else:
  star(3, graph)
  result = after

for i in range(n):
  print("".join(result[i]))
