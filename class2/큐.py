from collections import deque

result = []
queue = deque()
for t in range(int(input())):
  command = list(map(str, input().split()))
  if(command[0] == "push"):
    queue.append(int(command[1])) 
  elif(command[0] == "front"):
    if(queue):
      result.append(queue[0])
    else:
      result.append(-1)
  elif(command[0] == "back"):
    if(queue):
      result.append(queue[-1])
    else:
      result.append(-1)
  elif(command[0] == "empty"):
    if(queue):
      result.append(0)
    else:
      result.append(1)
  elif(command[0] == "size"):
    result.append(len(queue))
  else:
    if(queue):
      result.append(queue.popleft())
    else:
      result.append(-1)

for res in result:
  print(res)