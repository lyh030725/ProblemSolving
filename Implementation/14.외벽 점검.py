import itertools

def solution(n, weak, dist):
  answer = len(dist) + 1
  length = len(weak)
  for i in range(length):
    weak.append(weak[i] + n)
    
  for friends in itertools.permutations(dist, len(dist)):
    for start in range(length):
      count = 1
      position = friends[count-1] + weak[start]
      for index in range(start, start+length):
        if(position < weak[index]):
          count += 1
          if(count > len(dist)):
            break
          position = friends[count-1] + weak[index]
      answer = min(answer, count)
  if(answer > len(dist)):
    answer = -1


  return answer

print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))