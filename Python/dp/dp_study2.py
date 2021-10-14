A = input()
B = input()
lenA, lenB = len(A), len(B)

dp = [
    [0 for _ in range(lenB)]
    for _ in range(lenA)
]

dp[0][0] = int(A[0] == B[0])
for i in range(1, lenA):
    if A[i] == B[0]:
        dp[i][0] = 1
    else:
        dp[i][0] = dp[i-1][0]

for j in range(1, lenB):
    if A[0] == B[j]:
        dp[0][j] = 1
    else:
        dp[0][j] = dp[0][j-1]

for i in range(1, lenA):
    for j in range(1, lenB):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[lenA-1][lenB-1])