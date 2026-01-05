def binary_search_recur(arr, target, start, end):
  if(start > end):
    return None
  mid = (start+end)//2
  if(arr[mid] == target):
    return mid
  elif(arr[mid] > target):
    return binary_search_recur(arr, target, start, mid -1)
  else:
    return binary_search_recur(arr, target, mid+1, end)
  
def binary_search_iter(arr, target):
  start = 0
  end = len(arr)-1
  while(start <= end):
    mid = (start+end)//2
    if(arr[mid] == target):
      return mid
    elif(arr[mid] > target):
      end = mid-1
    else:
      start = mid+1
  return None

arr= [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
target = 7

result = binary_search_iter(arr, target)
if(result == None):
  print("값이 없습니다.")
else:
  print(result+1)