n = int(input())

data = []
for i in range(n):
  data.append(list(map(int, input().split())))

result = []
for i in range(n):
  grade = 1
  for j in range(n):
    if(i != j):
      if(data[i][0] < data[j][0] and data[i][1] < data[j][1]):
        grade += 1
  result.append(grade)

for res in result:
  print(res, end=" ")