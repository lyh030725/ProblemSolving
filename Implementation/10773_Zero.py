n = int(input())

nums = list()
for i in range(n):
  current = int(input())
  if(current == 0):
    nums.pop()
    continue
  nums.append(current)

sum = 0
for num in nums:
  sum += num
print(sum)
