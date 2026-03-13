from collections import deque

result = []

while True:
  stack = deque()
  phrase = input()
  if(phrase == "."):
    break
  
  yes_sign = True
  for char in phrase:
    if(char == "(" or char == "["):
      stack.append(char)
    elif(char == ")" or char == "]"):
      if(stack):
        data = stack.pop()
        if(char == ")"):
          if(data != "("):
            yes_sign = False
            break
        else:
          if(data != "["):
            yes_sign = False
            break
      else:
        yes_sign = False
        break

  if(yes_sign and len(stack) == 0):
    result.append("yes")
  else:
    result.append("no")

  

for res in result:
  print(res)