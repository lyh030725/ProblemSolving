import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = int(1e9)
res = 0
for i in range(n):
  for j in range(i+1, n):
    for k in range(j+1, n):
      data = cards[i] + cards[j] + cards[k]
      if(data <= m):
        result = min(result, m-data)
        if(result == m-data):
          res = data

print(res)