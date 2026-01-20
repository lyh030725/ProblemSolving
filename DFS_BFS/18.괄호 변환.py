def solution(p):
    if(len(p) == 0):
        return ""
    left_count = 0
    right_count = 0
    for data in p:
        if(data == "("):
          left_count += 1
        else:
          right_count += 1
        if(left_count == right_count):
          break
    u = p[:left_count+right_count]
    v = p[left_count+right_count:]
    if(u[0] == "("):
      return u + solution(v)
    else:
      tmp = "(" + solution(v) + ")"
      u = list(u)
      u = u[1:len(u)-1]
      for i in range(len(u)):
        if u[i] == "(":
          u[i] = ")"
        else:
          u[i] = "("
      return tmp + ''.join(u)

print(solution("()))((()"))
    