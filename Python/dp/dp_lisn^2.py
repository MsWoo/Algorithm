def LIS_DP(seq):
    dp = [1] * len(seq)

    for i in range(len(seq)):
        for j in range(i):
            if ord(seq[i]) > ord(seq[j]):
                dp[i] = max(dp[i], dp[j]+1)

    lis = max(dp)

    return lis
	
seq = input()  
lis = LIS_DP(seq)
print(lis)