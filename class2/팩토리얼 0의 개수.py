n = int(input())

if(n != 0):
  fact = 1
  for i in range(1,n+1):
    fact *= i

  count = 0
  while fact > 0:
    if(fact % 10 == 0):
      count += 1
    else:
      break
    fact //= 10
  print(count)
else:
  print(0)