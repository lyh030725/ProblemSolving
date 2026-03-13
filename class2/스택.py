result = []
stack = []
for t in range(int(input())):
  command = list(map(str, input().split()))
  if(command[0] == "push"):
    stack.append(int(command[1])) 
  elif(command[0] == "top"):
    if(stack):
      result.append(stack[-1])
    else:
      result.append(-1)
  elif(command[0] == "empty"):
    if(stack):
      result.append(0)
    else:
      result.append(1)
  elif(command[0] == "size"):
    result.append(len(stack))
  else:
    if(stack):
      result.append(stack.pop())
    else:
      result.append(-1)

for res in result:
  print(res)