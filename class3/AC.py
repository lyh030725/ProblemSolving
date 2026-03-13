import sys
from collections import deque

input = sys.stdin.readline

for t in range(int(input())):
  func = input().rstrip()
  n = int(input())
  tmp = input().rstrip()
  tmp = tmp[1:len(tmp)-1]

  data = deque()
  for value in tmp.split(","):
    if(value != ""):
      data.append(int(value))

  reverse_status = False

  flag = True

  for command in func:
    if(command == "R"):
      reverse_status = not reverse_status
    else:
      if(len(data) == 0):
        print("error")
        flag = False
        break
      if(reverse_status):
        data.pop()
      else:
        data.popleft()
  
  if(flag):
    print("[", end="")
    while data:
      if(reverse_status):
        tmp = data.pop()
      else:
        tmp = data.popleft()
      if(len(data) == 0):
        print(tmp, end="")
        break
      print(tmp, end=",")
    print("]")