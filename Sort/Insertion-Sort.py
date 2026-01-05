import sys
input = sys.stdin.readline
n, t = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(1, t):
  for j in range(i, 0, -1):
    if(arr[j] < arr[j-1]):
      arr[j] , arr[j-1] = arr[j-1], arr[j]
    else:
      break

sys.stdout.write(' '.join(str(s) for s in arr))