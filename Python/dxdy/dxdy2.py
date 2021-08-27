n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

cnt = 0
dxs = [1, -1, 0, 0]
dys = [0, 0, 1, -1]
ans = 0
for i in range(n):
    for j in range(n):
        for dir in range(4):
            nx = i + dxs[dir]
            ny = j + dys[dir]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            ans += 1
        cnt = 0
print(ans)