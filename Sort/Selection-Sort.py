n, k = map(int, input().split())
arr = list(map(int , input().split()))

count = 0
a = 0
b = 0
for i in range(len(arr)-1, -1, -1):
  max_index = i
  for j in range(i-1, -1,-1):
    if(arr[j] > arr[max_index]):
      max_index = j
  arr[i], arr[max_index] = arr[max_index], arr[i]
  if(i != max_index):
    count += 1
    if(count == k):
      a = arr[max_index]
      b = arr[i]

if(count < k):
  print(-1)
else:
  print(a,b)