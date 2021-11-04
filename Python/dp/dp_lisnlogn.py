def LIS_DP(seq):
    dp = ['A']
    leng = 0

    for i in range(len(seq)):    
        if dp[0] == 'A' or ord(seq[i]) > ord(dp[-1]):
            dp.append(seq[i])
            leng += 1
            continue

        left = 0
        right = leng
        while(left < right):
            mid = (left + right) // 2

            if ord(seq[i]) < ord(dp[mid]):
                right = mid
            else:
                left = mid + 1
        
        dp[right] = seq[i]

    return leng
       

seq = input()  
lis = LIS_DP(seq)
print(lis)
