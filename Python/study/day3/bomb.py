n = int(input())
grid = [
    [0 for _ in range(n)]
    for _ in range(n)
]
for i in range(n):
    grid[i] = list(map(int, input().split()))
r, c = map(int, input().split())


nr, nc = r-1, c-1
if grid[nr][nc] == 1:
    grid[nr][nc] = 0
else:
    ran = grid[nr][nc] - 1
    grid[nr][nc] = 0
    for i in range(1, ran+1):
        if nr-i >= 0:
            grid[nr-i][nc] = 0
        if nr+i < n:
            grid[nr+i][nc] = 0
        if nc-i >= 0:
            grid[nr][nc-i] = 0
        if nc+i < n:
            grid[nr][nc+i] = 0

# print("---")
# for i in range(n):
#     for j in range(n):
#         print(grid[i][j], end=" ")
#     print()

for i in range(n-1,0,-1):
    for j in range(n):
        if grid[i][j] == 0:  
            k = 1
            if grid[i-k][j] == 0:
                while True:
                    if i-k < 0:
                        break
                    if grid[i-k][j] != 0:
                        grid[i][j], grid[i-k][j] = grid[i-k][j], grid[i][j]
                        break
                    k+=1
            if grid[i][j] == 0:
                grid[i][j], grid[i-1][j] = grid[i-1][j], grid[i][j]

# print("---")
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print()