A = list(map(int, input().split()))

dp = [1 for _ in range(len(A)+1)]

dp[0] = 0

startidx = 0
minuscnt = 0

for ele in A:
    if ele < 0:
        minuscnt+=1


for i in range(1, len(A)+1):
    for j in range(startidx, i):
        if A[j] == 0:
            startidx = j+1
            dp[i] = 0
        else :
            if A[j]< 0:
                dp[i] = max(dp[i], dp[i]*A[j]*-1)
            else:
                dp[i] = max(dp[i], dp[i]*A[j])

print(dp)