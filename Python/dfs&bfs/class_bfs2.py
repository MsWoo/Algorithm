from collections import deque

n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(m)]
    for _ in range(n)
]

ans = -1

def inRange(x, y):
    return 0<=x and x < n and 0<=y and y < m

def canGo(x, y):
    if not inRange(x, y):
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

def BFS():
    #상하좌우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y, s = queue.popleft()

        for dx, dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy

            if nx == n-1 and ny == m-1:
                ans = s+1

            if canGo(nx, ny):
                queue.append((nx, ny, s+1))
                visited[nx][ny] = True
            


queue = deque()
queue.append((0, 0, 0))
visited[0][0] = True
BFS()

print(ans)