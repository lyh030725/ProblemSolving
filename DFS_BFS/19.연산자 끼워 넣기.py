import sys
input = sys.stdin.readline
from itertools import permutations

n = int(input())

nums = list(map(int, input().split()))

operator_num = list(map(int, input().split()))
operators = []

for i in range(4):
  for _ in range(operator_num[i]):
    operators.append(i)

cases = set(permutations(operators, n-1))
max_value = -int(1e9)
min_value = int(1e9)

for case in cases:
  count = 1
  result = nums[0]
  for opt in case:
    if(opt == 0):
      result += nums[count]
    elif(opt == 1):
      result -= nums[count]
    elif(opt == 2):
      result *= nums[count]
    else:
      if(result < 0):
        result = -(-result//nums[count])
      else:
        result //= nums[count]
    count += 1
  min_value = min(min_value, result)
  max_value = max(max_value, result)

print(max_value)
print(min_value)
    


