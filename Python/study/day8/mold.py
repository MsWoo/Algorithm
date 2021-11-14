#https://www.codetree.ai/frequent-problems/biology-lab-intern/description

n, m, k = map(int, input().split())

grid = [
    [ 0 for _ in range(m+1)]
    for _ in range(n+1)
]

xys = []
speed = []
direction = []
size = []


for _ in range(k):
    x, y, s, d, b = map(int, input().split())

    grid[x][y] = 1

    xys.append([x,y])
    speed.append(s)
    direction.append(d)
    size.append(b)

def check(x, y):
    if x < 1 or x > n or y < 1 or y > m:
        return False
    return True

def move():
    global k 

    #위 아래 오른쪽 왼쪽
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, 1, -1]

    #모든 곰팡이 move
    for i in range(k):
        grid[xys[i][0]][xys[i][1]] -= 1
        #곰팡이의 스피드만큼 1씩 이동한다.
        for _ in range(speed[i]):
            if check(xys[i][0] + dx[direction[i]], xys[i][1] + dy[direction[i]]):
                xys[i][0] = xys[i][0] + dx[direction[i]]
                xys[i][1] = xys[i][1] + dy[direction[i]]

            #벽에 부딪힌 경우
            else:
                if direction[i] == 1:
                    direction[i] = 2
                elif direction[i] == 2:
                    direction[i] = 1
                elif direction[i] == 3:
                    direction[i] = 4
                else:
                    direction[i] = 3

                xys[i][0] = xys[i][0] + dx[direction[i]]
                xys[i][1] = xys[i][1] + dy[direction[i]] 
        
        #곰팡이 한마리가 이동을 마쳤다.
        grid[xys[i][0]][xys[i][1]] += 1

def eat():
    global k 
    
    kill = []
    kill.clear()

    for i in range(k-1):
        sx, sy = xys[i][0], xys[i][1]
        for j in range(i+1, k):
            ex, ey = xys[j][0], xys[j][1]
            if sx == ex and sy == ey:
                if size[i] > size[j]:
                    print(i, j)
                    kill.append(j)
                else:
                    print(i, j)
                    kill.append(i)

    nkill = list(set(kill))

    print(kill)
    # print(nkill)

    for i in range(len(nkill)):
        k -= 1
        xys.pop(nkill[i])
        speed.pop(nkill[i])
        direction.pop(nkill[i])
        size.pop(nkill[i])





ans = 0

#인턴이 열을 탐색.
for i in range(1, m+1):

    #가장 처음만난 곰팡이 채취
    for j in range(1, n+1):
        if grid[j][i] != 0:

            idx = xys.index([j,i])

            ans += size[idx]
            k-=1
            
            xys.pop(idx)
            speed.pop(idx)
            direction.pop(idx)
            size.pop(idx)
            
            break

    #곰팡이 이동
    move()
    eat()

print(ans)
    