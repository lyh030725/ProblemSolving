import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

dictionary = []

for i in range(n):
  dictionary.append(input().strip())

result = []
for i in range(m):
  data = input().strip()
  if(data.isdigit()):
    data = int(data)
    print(dictionary[data-1])
  else:
    print(dictionary.index(data)+1)
