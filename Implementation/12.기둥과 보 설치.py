def possible(answer):
  for i in answer:
    x, y, stuff = i
    if(stuff == 0):
      if(y==0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer):
        continue
      return False
    else:
      if([x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer)):
        continue
      return False
  return True

def solution(n, build_frame):
  answer = []
  for frame in build_frame:
    x, y, stuff, operation = frame
    if(operation == 0):
      answer.remove([x,y,stuff])
      if(not possible(answer)):
        answer.append([x,y,stuff])
    else:
      answer.append([x,y,stuff])
      if(not possible(answer)):
        answer.remove([x,y,stuff])

  return sorted(answer)