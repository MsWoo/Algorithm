n = int(input())
arr = list(map(int, input().split()))

dp = [-1 for _ in range(n+1)]

a = [0 for _ in range(n+1)]

a[1:] = arr[:]
dp[0] = 0

for i in range(1, n+1):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))