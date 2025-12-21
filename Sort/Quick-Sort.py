arr = [9 ,2 , 5, 4 ,3 ,1 ,8 ,0 ,7, 6]

def quicksort(arr, start, end):
  if(start >= end):
    return
  pivot = start
  left = start + 1
  right = end
  while(left <= right):
    while left <= end and arr[left] <= arr[pivot]:
      left += 1
    while right > start and arr[right] >= arr[pivot]:
      right -= 1
    if(left > right):
      arr[pivot], arr[right] = arr[right], arr[pivot]
    else:
      arr[left], arr[right] = arr[right], arr[left]
  quicksort(arr, start, right-1)
  quicksort(arr, right+1, end)

quicksort(arr, 0, len(arr)-1)
print(arr)