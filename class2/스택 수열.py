from collections import deque
import sys
import copy

input = sys.stdin.readline

n = int(input())
stack = deque()

data = []
for i in range(n):
  data.append(int(input()))

result = []
max_num = 0
flag = True

for num in data:
  if(max_num > num):
    poped = stack.pop()
    if(poped != num):
      flag = False
      break
    result.append("-")
  else:
    for i in range(max_num+1, num+1):
      stack.append(i)
      result.append("+")
    max_num = num
    stack.pop()
    result.append("-")

if(flag):
  for res in result:
    print(res)
else:
  print("NO")