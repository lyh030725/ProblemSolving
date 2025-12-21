from sys import stdin, stdout
n, t = map(int,stdin.readline().split())
arr = list(map(int,stdin.readline().split()))

for i in range(1, t):
  for j in range(i, 0, -1):
    if(arr[j] < arr[j-1]):
      arr[j] , arr[j-1] = arr[j-1], arr[j]
    else:
      break

stdout.write(' '.join(str(s) for s in arr))