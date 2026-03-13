n = int(input())
data = input()

result = 0
for i in range(n):
  index = ((ord(data[i])-96)*(31**i))
  result += index

print(result%1234567891)
