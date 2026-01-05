s = input()

result = 0

for i in range(len(s)):
  number = int(s[i])
  if(result <= 1):
    result += number
    continue
  if number == 0 or number == 1:
    result += number
  else:
    result *= number

print(result)
