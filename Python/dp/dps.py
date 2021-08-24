import sys

INT_MIN =  -sys.maxsize

n = int(input())
a = [
    0
    for _ in range(n + 1)
]

dp = [
    0
    for _ in range(n + 1)
]


def initialize():
    for i in range(1, n + 1):
        dp[i] = INT_MIN
    
    dp[1] = a[1]


given_seq = list(map(int, input().split()))
a[1:] = given_seq[:]

initialize()

for i in range(2, n + 1):
    dp[i] = max(dp[i - 1] + a[i], a[i])

ans = max(dp[1:n + 1])
print(ans)
