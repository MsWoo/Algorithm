N, M = map(int, input().split())
coin = list(map(int, input().split()))

dp = [10001 for _ in range(M+1)]

dp[0] = 0

for i in range(1, M+1):
    for j in range(N):
        if i >= coin[j]:
            dp[i] = min(dp[i], dp[i-coin[j]]+1)

print(dp[M])