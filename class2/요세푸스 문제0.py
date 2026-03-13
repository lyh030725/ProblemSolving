circle = []
n, k = map(int, input().split())

result = []

for i in range(n):
  circle.append(i+1)

index = -1
while True:
  if(len(circle) == 0):
    break

  for _ in range(k):
    index += 1
    if(index >= len(circle)):
      index = 0

  result.append(circle[index])
  circle.remove(circle[index])
  index -= 1

  
print("<", end="")
for i in range(n):
  if(i == n-1):
    print(result[i], end=">")
    break
  print(result[i], end=", ")
