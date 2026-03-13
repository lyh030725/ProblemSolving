n, s = map(int, input().split())

data = list(map(int, input().split()))

INF = int(1e9)

left = 0
right = 0
answer = INF
partial_sum = [0]*(n+1)
partial_sum[1] = data[0]

for i in range(2, n+1):
  partial_sum[i] = data[i-1] + partial_sum[i-1]

while(left < n and right < n):
  tmp = partial_sum[right+1] - partial_sum[left]
  if tmp >= s:
    answer = min(answer, right-left+1)
    left += 1
  else:
    right += 1

if answer == INF:
  print(0)
else:
  print(answer)