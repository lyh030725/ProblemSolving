import sys
input = sys.stdin.readline

m = int(input())

S = set()

for _ in range(m):
  command = list(map(str, input().split()))
  if(command[0] == "add"):
    data = int(command[1])
    S.add(data)
  elif(command[0] == "check"):
    data = int(command[1])
    if(data in S):
      print(1)
    else:
      print(0)
  elif(command[0] == "remove"):
    data = int(command[1])
    if(data in S):
      S.remove(data)
  elif(command[0] == "toggle"):
    data = int(command[1])
    if(data in S):
      S.remove(data)
    else:
      S.add(data)
  elif(command[0] == "all"):
    S = set(list(range(1,21)))
  else:
    S = set()
