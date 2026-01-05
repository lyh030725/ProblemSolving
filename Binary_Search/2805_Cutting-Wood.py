n, m = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
def search_height():
  global result
  start = 0
  end = max(arr)
  while start <= end:
    count = 0
    mid = (start+end)//2
    for i in arr:
      if(i>mid):
        count += i-mid
    if(count == m):
      result = mid
      break
    elif(count > m):
      result = mid
      start = mid + 1
    else:
      end = mid -1


search_height()
print(result)

