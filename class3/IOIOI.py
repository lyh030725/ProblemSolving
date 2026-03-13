n = int(input())
m = int(input())

data = input()

i = 0

count = 0
result = 0

while i+3 <= m:
  if(data[i:i+3] == "IOI"):
    count += 1
    i += 2
    if(count == n):
      result += 1
      count -= 1
  else:
    i += 1
    count = 0

print(result)