import sys
from collections import deque

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    q = deque()
    q.append((0, 0, 0))  # x, y, 벽부쉈는지(0/1)

    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = 1

    while q:
        x, y, wall = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:

                # 빈 칸
                if graph[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    q.append((nx, ny, wall))

                # 벽이고 아직 안 부쉈다면
                if graph[nx][ny] == 1 and wall == 0:
                    if visited[nx][ny][1] == 0:
                        visited[nx][ny][1] = visited[x][y][wall] + 1
                        q.append((nx, ny, 1))

    return -1

print(bfs())
