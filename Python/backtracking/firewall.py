#입력
n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
temp = [
    [0 for _ in range(m)]
    for _ in range(n)
]

fires = []
zeros = []

walls = []

answer = 0

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#그리드 범위 체크
def check(x, y):
    if x < 0 or x > n-1 or y < 0 or y > m-1:
        return False
    return True

#재귀함수로 불지르기
def fire(x, y):
    for i in range(len(dx)):
        nx = x+dx[i]
        ny = y+dy[i]
        if check(nx, ny):
            if grid[nx][ny] == 1:
                continue
            elif grid[nx][ny] == 0:
                grid[nx][ny] = 2
                fire(nx, ny)

#방화벽 설치 후 불지르기
def firewall():
    global answer, grid, temp

    if len(walls) == 3:
        #grid temp에 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = grid[i][j]


        #방화벽 설치
        for i in range(len(walls)):
            grid[walls[i][0]][walls[i][1]] = 1

        #불 지르기
        for i in range(len(fires)):
            fire(fires[i][0], fires[i][1])

        #0 count
        zerocnt = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    zerocnt += 1

        answer = max(answer, zerocnt)
        #grid 복구
        for i in range(n):
            for j in range(m):
                grid[i][j] = temp[i][j]

        return

    for i in range(len(zeros)):
        if [zeros[i][0], zeros[i][1]] in walls:
            continue

        walls.append([zeros[i][0], zeros[i][1]])

        firewall()

        walls.pop()

#초기 불 찾기, 0 찾기
for i in range(n):
    for j in range(m):
        if grid[i][j] == 2:
            fires.append([i,j])
        if grid[i][j] == 0:
            zeros.append([i,j])
 

firewall()
print(answer)