import sys
input = sys.stdin.readline

n = int(input())
data = []

for i in range(n):
  a,b = map(int, input().split())
  data.append((a,b))
data.sort(key=lambda x:(x[1], x[0]))

index = 0
end = data[index][1]
count = 1

while True:
  index += 1
  if(index >= n):
    break
  if(end <= data[index][0]):
    count += 1
    end = data[index][1]

print(count)