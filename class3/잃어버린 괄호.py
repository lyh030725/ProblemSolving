expression = input()

data = expression.split("-")
result = []
for i in range(len(data)):
  if(data[i].find("+") == None):
    result.append(int(data[i]))
  else:
    tmp = 0
    tmp_list = data[i].split("+")
    for item in tmp_list:
      tmp += int(item)
    result.append(tmp)

count = result[0]

for i in range(1, len(result)):
  count -= result[i]

print(count)