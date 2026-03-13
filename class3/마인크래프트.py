import sys
input = sys.stdin.readline

n, m, b = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

result = int(1e9)
result_height = 0

for i in range(257):
  sec = 0
  take_block = 0
  use_block = 0

  for j in range(n):
    for k in range(m):
      if(graph[j][k] < i):
        use_block += i - graph[j][k]
      else:
        take_block += graph[j][k] - i
      
  if use_block > take_block + b:
    continue

  sec = take_block*2 + use_block

  result = min(result, sec)
  if(result == sec):
    result_height = i

print(result, result_height)