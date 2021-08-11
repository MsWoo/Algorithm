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

def inRange(x, y):
    return 0<=x and x < n and 0<=y and y < m

def canGo(x, y):
    if not inRange(x, y):
        return False

#visited[x][y]는 0이 아닌 값 이라는 뜻(여기서는 false가 아니라는 뜻).
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True

def BFS():
    #상하좌우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for dx, dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy

            if canGo(nx, ny):
                queue.append((nx, ny))
                visited[nx][ny] = True 

queue = deque()
queue.append((0, 0))
visited[0][0] = True
BFS()

print(1 if visited[n-1][m-1] else 0)