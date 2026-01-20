from collections import deque

def get_next_pos(pos, board):
    next_pos = []
    pos = list(pos)
    pos1_x, pos1_y, pos2_x, pos2_y = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1,1,0,0]
    dy= [0,0,-1,1]
    #상하좌우
    for i in range(4):
        next_pos1_x, next_pos1_y, next_pos2_x, next_pos2_y = pos1_x + dx[i], pos1_y + dy[i], pos2_x + dx[i], pos2_y + dy[i]
        if(board[next_pos1_x][next_pos1_y] == 0 and board[next_pos2_x][next_pos2_y]== 0):
            next_pos.append({(next_pos1_x, next_pos1_y), (next_pos2_x, next_pos2_y)})

    #가로로 놓인 경우, 회전
    if(pos1_x == pos2_x):
        for i in [-1,1]:
            if(board[pos1_x+i][pos1_y] == 0 and board[pos2_x+i][pos2_y] == 0):
                next_pos.append({(pos1_x, pos1_y), (pos1_x+i, pos1_y)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x+i, pos2_y)})
    
    #세로로 놓인 경우, 회전
    if(pos1_y == pos2_y):
        for i in [-1,1]:
            if(board[pos1_x][pos1_y+i] == 0 and board[pos2_x][pos2_y+i] == 0):
                next_pos.append({(pos1_x, pos1_y), (pos1_x, pos1_y+i)})
                next_pos.append({(pos2_x, pos2_y), (pos2_x, pos2_y+i)})

    return next_pos

def solution(board):
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    pos = {(1,1), (1,2)}
    q = deque([(pos, 0)])
    visit = [pos]
    while q:
        pos, cost = q.popleft()
        if (n,n) in pos:
            return cost
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visit:
                q.append((next_pos, cost+1))
                visit.append(next_pos)


    



print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))