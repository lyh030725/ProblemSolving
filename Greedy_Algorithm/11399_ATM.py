i = int(input())

line = list(map(int , input().split()))

sortedline = sorted(line)

result = 0
k = 0

for n in range(i):
  k += 1
  for m in range(k):
    result += sortedline[m]

print(result)