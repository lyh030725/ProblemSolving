data = []

while True:
  num = input()
  if(num == '0'):
    break
  data.append(num)

result = []
for num in data:
  reversed_ver = ""
  num = list(num)
  for i in range(len(num)-1,-1,-1):
    reversed_ver += num[i]
  num = "".join(num)
  if(reversed_ver == num):
    result.append("yes")
  else:
    result.append("no")

for res in result:
  print(res)