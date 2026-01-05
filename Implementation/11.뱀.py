n = int(input())
k = int(input())

apples = []
for i in range(k):
  x,y = map(int , input().split())
  apples.append((x,y))

moves = []
l = int(input())
for i in range(l):
  x, c = input().split()
  x = int(x)
  moves.append((x,c))

displacment = {
  "Left": (0, -1),
  "Right": (0, 1),
  "Up": (-1, 0),
  "Down": (1, 0)
}

def get_direction(direction, trans):
  if(direction == "Right"):
    if(trans == "L"):
      return "Up"
    else:
      return "Down"
  elif(direction == "Left"):
    if(trans == "L"):
      return "Down"
    else:
      return "Up"
  elif(direction == "Up"):
    if(trans == "L"):
      return "Left"
    else:
      return "Right"
  else:
    if(trans == "L"):
      return "Right"
    else:
      return "Left"


sec = 0
snake = [(1,1)]
direction = "Right"
trans_count = 0
snake_length = 1
flag = True

while(flag):
  sec += 1
  prev = snake[snake_length-1]
  #머리만 이동
  head = tuple((snake[0][0]+displacment[direction][0], snake[0][1]+displacment[direction][1]))

  #벽에 충돌
  if(head[0] > n or head[0] <= 0 or head[1] > n or head[1] <= 0):
      flag = False
      break
  #몸에 충돌
  for j in range(1, snake_length):
    if(head == snake[j]):
      flag = False
      break

  #나머지 부분 이동
  snake = [head] + snake[0:snake_length-1]

  #사과를 만난 경우
  for apple in apples:
    if(snake[0] == apple):
      apples.remove(apple)
      snake.append(prev)
      snake_length += 1

  #방향 전환
  if(trans_count <= l-1 and sec == moves[trans_count][0]):
    direction = get_direction(direction, moves[trans_count][1])
    trans_count += 1  
  
print(sec)

    