n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
cnt = 0
ans = 0
#Top, Bot, Fro, Bac, Lef, Rig
dice = [1, 6, 2, 5, 4, 3]
x, y = 0, 0
xys = set()

direction = 2

#동 서 남 북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y):
    global n, m
    if x < 0 or x > n-1 or y < 0 or y > n-1:
        return False
    return True

def sumnum(x, y):
    xys.add((x,y))
    for i in range(4):
        if check(x+dx[i], y+dy[i]):
            if grid[x][y] == grid[x+dx[i]][y+dy[i]]:
                if (x+dx[i], y+dy[i]) not in xys:
                    xys.add((x+dx[i],y+dy[i]))
                    sumnum(x+dx[i], y+dy[i])

def clock(d):
    if d == 2:
        return 4
    elif d == 4:
        return 1
    elif d == 1:
        return 3
    else:
        return 2
def counterclock(d):
    if d == 2:
        return 3
    elif d == 4:
        return 2
    elif d == 1:
        return 4
    else:
        return 1
def back(d):
    if d == 2:
        return 1
    elif d == 4:
        return 3
    elif d == 1:
        return 2
    else:
        return 4

#1 서, 2 동, 3 북, 4 남
def tumble(d):
    global x, y, cnt, xys, direction, ans

    xys.clear()
    cnt += 1
    new_d = 0

    Top = dice[0]
    Bot = dice[1]
    Fro = dice[2]
    Bac = dice[3]
    Lef = dice[4]
    Rig = dice[5]

    if d == 1:
        if check(x, y-1):
            y = y-1
            dice[0] = Rig
            dice[4] = Top
            dice[1] = Lef
            dice[5] = Bot
        else:
            cnt-=1
            return -1

    elif d == 2:
        if check(x, y+1):
            y = y+1
            dice[0] = Lef
            dice[4] = Bot
            dice[1] = Rig
            dice[5] = Top
        else:
            cnt-=1
            return -1

    elif d == 3:
        if check(x-1, y):
            x = x-1
            dice[0] = Fro
            dice[1] = Bac
            dice[2] = Bot
            dice[3] = Top
        else:
            cnt-=1
            return -1

    else:
        if check(x+1, y):
            x = x+1
            dice[0] = Bac
            dice[1] = Fro
            dice[2] = Top
            dice[3] = Bot
        else:
            cnt-=1
            return -1
    
    if dice[1] > grid[x][y]:
        new_d = clock(d)
    elif dice[1] < grid[x][y]:
        new_d = counterclock(d)
    else:
        new_d = d

    direction = new_d

    sumnum(x, y)
    templist = []
    templist.clear()
    templist = list(xys)
    ans += grid[templist[0][0]][templist[0][1]] * len(xys)

    return 0

ret = 0
while cnt < m:
    if ret == -1:
        ret = tumble(back(direction))
    else:
        ret = tumble(direction)

print(ans)