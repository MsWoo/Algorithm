#입력
n = int(input())
A = [
    list(map(int, input().split()))
    for _ in range(n)
]
dp = [
    [-1] * n
    for _ in range(n)
]

#초기조건
dp[0][0] = A[0][0]
for i in range(1, n):
    dp[i][0] = dp[i-1][0] + A[i][0]
for j in range(1, n):
    dp[0][j] = dp[0][j-1] + A[0][j]

#DP
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j] + A[i][j], dp[i][j-1] + A[i][j])

#결과출력
print(dp[n-1][n-1])