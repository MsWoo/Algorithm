n, m = map(int, input().split())

graph = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [0 for _ in range(m)]
    for _ in range(n)
]

def inRange(x, y):
    return 0<=x and x < n and 0<=y and y < m

def canGo(x, y):
    if not inRange(x, y):
        return False

#visited[x][y]는 0이 아닌 값 이라는 뜻(여기서는 false가 아니라는 뜻).
    if visited[x][y] or graph[x][y] == 0:
        return False
    
    return True

def DFS(x, y):
    #right, down
    dxs, dys = [1, 0], [0, 1]

    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy

        if canGo(nx, ny):
            visited[nx][ny] = 1
            DFS(nx, ny)


visited[0][0] = 1
DFS(0, 0)
print(visited[n-1][m-1])