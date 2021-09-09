n, m, q = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def wind(r,d):
    if r > n or r < 1:
        return

    i = r-1

    if d == "L":
        temp = grid[i][-1]
        for j in range(m-2, -1, -1):
            grid[i][j+1] = grid[i][j]
        grid[i][0] = temp
    elif d == "R":
        temp = grid[i][0]
        for j in range(1, m):
            grid[i][j-1] = grid[i][j]
        grid[i][m-1] = temp


for _ in range(q):
    r, d = input().split()
    r = int(r)
    
    wind(r,d)
    
    i = r-1

    i21 = i
    i22 = i-1
    nd = d
    f = 0

    while i22 >= 0:
        for idx in range(m):
            f=0
            if grid[i21][idx] == grid[i22][idx] :
                if nd == "L":
                    nd = "R"
                else :
                    nd = "L"
                f = 1
                wind(i22+1, nd)
                break
        if f == 0:
            break
        i21 -= 1
        i22 -= 1
    
    i31 = i
    i32 = i+1
    nd2 = d
    f = 0

    while i32 < n:
        for idx in range(m):
            f=0
            if grid[i31][idx] == grid[i32][idx] :
                if nd2 == "L":
                    nd2 = "R"
                else :
                    nd2 = "L"
                f = 1
                wind(i32+1, nd2)
                break
        if f == 0:
            break
        i31 += 1
        i32 += 1
                
for i in range(n):
    for j in range(m):
        print(grid[i][j], end=" ")
    print()   