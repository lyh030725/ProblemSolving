from collections import deque

result = []

for t in range(int(input())):
  stack = deque()
  data = input()
  flag = True
  for char in data:
    if(char == "("):
      stack.append(char)
    if(char == ")"):
      if(stack):
        stack.pop()
      else:
        flag = False
  
  if(stack):
    flag = False
  
  if(flag):
    result.append("YES")
  else:
    result.append("NO")

for res in result:
  print(res)