n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
grid2 = [
    [0 for _ in range(n)]
    for _ in range(n)
]
temp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

NUM_MOVES = 5
ans = 0

move_dirs = [0 for _ in range(NUM_MOVES)]


def get_maxnum():
    return max([
        grid[i][j]
        for i in range(n)
        for j in range(n)
    ])

def rotate():
    for i in range(n):
        for j in range(n):
            grid2[i][j] = 0

    for i in range(n):
        for j in range(n):
            grid2[i][j] = grid[n-j-1][i]

    for i in range(n):
        for j in range(n):
            grid[i][j] = grid2[i][j]

def drop():
    for i in range(n):
        for j in range(n):
            grid2[i][j] = 0

    for i in range(n):
        keep, next_row = None, n - 1
        for j in range(n-1, -1, -1):
            if not grid[j][i]:
                continue

            if keep == None:
                keep = grid[j][i]

            elif keep == grid[j][i]:
                grid2[next_row][i] = keep * 2
                keep = None
                next_row -= 1

            else:
                grid2[next_row][i] = keep
                keep = grid[j][i]
                next_row -= 1
        
        if keep != None:
            grid2[next_row][i] = keep
            next_row -= 1


    for i in range(n):
        for j in range(n):
            grid[i][j] = grid2[i][j]

def tilt(move_dir):
    for _ in range(move_dir):
        rotate()

    drop()

    for _ in range(4-move_dir):
        rotate()

def simulate():
    global ans

    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[i][j]

    for move_dir in move_dirs:
        tilt(move_dir)

    ans = max(ans, get_maxnum())

    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]

def start(cnt):
    if cnt == NUM_MOVES:
        simulate()
        return
    
    for i in range(4):
        move_dirs[cnt] = i
        start(cnt + 1)


start(0)
print(ans)