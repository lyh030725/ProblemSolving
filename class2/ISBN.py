data = list(input())

check = int(data.pop())
n = len(data)

for case in range(10):
  count = 0
  for i in range(n):
    if(i % 2 == 0):
      if("0" <= data[i] <= "9"):
        count += int(data[i])
      else:
        count += case
    else:
      if("0" <= data[i] <= "9"):
        count += 3*int(data[i])
      else:
        count += 3*case
  result = 10-count%10
  if(count%10 == 0):
    result = 0

  if(check == result):
    print(case)
    break