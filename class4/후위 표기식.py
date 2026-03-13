expression = input()
length = len(expression)
stack = []
result = []

for i in range(length):
  if "A" <= expression[i] <= "Z":
    if not stack:
      result.append(expression[i])
    else:
      if stack[-1] == "*" or stack[-1] == "/":
        result.append(expression[i])
        result.append(stack.pop())
      else :
        result.append(expression[i])
  elif expression[i] == ")":
    if stack:
      data = stack.pop()
      while data != "(":
        result.append(data)
        flag = True
        data = stack.pop()
      if stack:
        if stack[-1] == "*" or stack[-1] == "/":
          result.append(stack.pop())

  elif expression[i] == "+" or expression[i] == "-":
    if stack:
      if stack[-1] == "+" or stack[-1] == "-":
        data = stack.pop()
        while True:
          if data == "(":
            stack.append(data)
            break
          result.append(data)
          if not stack:
            break
          data = stack.pop()
    stack.append(expression[i])
  else:
    stack.append(expression[i])

while stack:
  result.append(stack.pop())

print("".join(result))