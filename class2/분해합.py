n = int(input())


flag = False
for m in range(1, 1000000):
  result = 0
  copy_m = m
  result += copy_m
  while copy_m > 0:
    result += copy_m%10
    copy_m //= 10
  if(n == result):
    print(m)
    flag= True
    break

if(flag == False):
  print(0)
