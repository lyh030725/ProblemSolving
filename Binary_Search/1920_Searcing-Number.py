n = int(input())
arr1 = list(map(int , input().split()))
arr1.sort()
m = int(input())
arr2 = list(map(int , input().split()))

def binary_search(arr, target):
  start = 0
  end = n-1
  while(start <= end):
    mid = (start+end)//2
    if(arr[mid] == target):
      return mid
    elif(arr[mid] > target):
      end = mid - 1
    else:
      start = mid +1
  return None

for i in arr2:
  result = binary_search(arr1, i)
  if(result == None):
    print(0)
  else:
    print(1)