#input 
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
    return True

def dfs(x, y):
    dxs, dys = [0, 1], [1, 0]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy

        if check(nx, ny):
            visited[nx][ny] = 1
            dfs(nx, ny)

visited[0][0] = 1
dfs(0, 0)
print(visited[n-1][m-1])


