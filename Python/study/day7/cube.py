def check(x, y):
    global n, m
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    return True

def tumble(s):
    global x, y, cube

    Top = cube['Top']
    Bot = cube['Bot']
    Front = cube['Front']
    Back = cube['Back']
    Left = cube['Left']
    Right = cube['Right']

    #동
    if s == 1:
        if check(x, y+1):
            y = y + 1
            cube['Bot'] = Right
            cube['Right'] = Top
            cube['Top'] = Left
            cube['Left'] = Bot
        else:
            return -1
    #서
    elif s == 2:
        if check(x, y-1):
            y = y - 1
            cube['Bot'] = Left
            cube['Left'] = Top
            cube['Top'] = Right
            cube['Right'] = Bot
        else:
            return -1
    #북
    elif s == 3:
        if check(x-1, y):
            x = x - 1
            cube['Back'] = Top
            cube['Top'] = Front
            cube['Front'] = Bot
            cube['Bot'] = Back
        else:
            return -1
    #남
    else:
        if check(x+1, y):
            x = x + 1
            cube['Back'] = Bot
            cube['Top'] = Back
            cube['Front'] = Top
            cube['Bot'] = Front
        else:
            return -1
    return 0

#Input
n, m, x, y, k = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
seq = list(map(int, input().split()))

#Cube dict definition
cube = {'Top' : 0, 'Bot' : 0, 'Front' : 0, 'Back' : 0, 'Left' : 0, 'Right' : 0}

#tumble dice
for s in seq:
    if tumble(s) == 0:
        if grid[x][y] == 0:
            grid[x][y] = cube['Bot']
        else:
            cube['Bot'] = grid[x][y]
            grid[x][y] = 0

        print(cube['Top'])