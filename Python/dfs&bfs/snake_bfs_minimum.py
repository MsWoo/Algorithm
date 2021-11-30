from collections import deque

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def check(x, y):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    if grid[x][y] == 0:
        return False
    if visited[x][y] > 0:
        return False
    return True

def bfs():
    while q:
        x, y = q.popleft()
        dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]

        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy

            if check(nx, ny):
                q.append((nx,ny))
                visited[nx][ny] = visited[x][y] + 1


q = deque()

visited[0][0] = 0
q.append((0,0))

bfs()

if visited[n-1][m-1] == 0:
    print(-1)
else:
    print(visited[n-1][m-1])