n, m = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

ans = 0
curval = 0
curval2 = 0
cnt = 1
cnt2 = []

arr = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        arr[i][j] = grid[j][i]

for i in range(n):
    cnt = 1
    cnt2.append(cnt)
    for j in range(n-1):
        curval = grid[i][j]
        if curval == grid[i][j+1] :
            cnt += 1
        else:
            cnt2.append(cnt)
            cnt = 1
    cnt2.append(cnt)
    if max(cnt2) >= m:
        ans += 1
    cnt2.clear()

    cnt = 1
    cnt2.append(cnt)
    for j in range(n-1):
        curval2 = arr[i][j]
        if curval2 == arr[i][j+1] :
            cnt += 1
        else:
            cnt2.append(cnt)
            cnt = 1
    cnt2.append(cnt)
    if max(cnt2) >= m:
        ans += 1 
    cnt2.clear()
    
print(ans)
