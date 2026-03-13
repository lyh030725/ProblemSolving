n = int(input())

count = 0
num = 666

while True:
  if(str(num).find("666") == -1):
    num += 1
    continue
  count += 1
  if(count == n):
    print(num)
    break
  num += 1