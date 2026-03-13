n = int(input())

data = list(map(int, input().split()))

left = 0
right = n-1
result_left = 0
result_right = n-1
optimal_val = int(1e10)

while True:
  mid = data[left]+data[right]
  if left >= right:
    print(data[result_left], data[result_right])
    break
  if mid == 0:
    print(data[left], data[right])
    break

  if abs(optimal_val) > abs(mid):
    optimal_val = mid
    result_left = left
    result_right = right

  if mid < 0:
    left += 1
  else:
    right -= 1
