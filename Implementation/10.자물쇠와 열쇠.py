import copy

def solution(key, lock):
  m = len(key)
  n = len(lock)
  rotate = [[] for _ in range(m)]

  for i in range(m):
    for j in range(m):
      rotate[i].append((j, m-i-1))

  
  #자물쇠의 홈 부분 추출
  min_row = n
  max_row = -1
  min_col = n
  max_col = -1
  for i in range(n):
    for j in range(n):
      if(lock[i][j] == 0):
        min_row = min(min_row, i)
        max_row = max(max_row, i)
        min_col = min(min_col, j)
        max_col = max(max_col, j)
  #자물쇠에 홈이 없는 경우
  if(max_row == -1):
    return False
  
  hole_lock = []
  row = max_row - min_row + 1
  col = max_col - min_col + 1
  for i in range(min_row, max_row+1):
    hole_lock.append([])
    for j in range(min_col, max_col+1):
      hole_lock[i-min_row].append(1 if lock[i][j] == 0 else 0)

  if(row > m or col > m):
    return False

  
  for i in range(4):
    partial_key = [[] for _ in range(row)]
    for j in range(row):
      partial_key[j] = key[j][:col]
    
    for j in range(m-row+1):
      for k in range(m-col+1):
        if(partial_key == hole_lock):
          return True
        for l in range(row):
          partial_key[l] = key[l+j][k:col+k]
        print(partial_key)

    # key를 시계 방향 회전
    rotated_key = [[0]*m for _ in range(m)]
    for i in range(m):
      for j in range(m):
        rotated_key[rotate[i][j][0]][rotate[i][j][1]] = key[i][j]
    key = copy.deepcopy(rotated_key)

  return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 0], [1, 0, 0], [1, 1, 0]]

print(solution(key, lock))