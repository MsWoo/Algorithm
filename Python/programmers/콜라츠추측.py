def solution(num):
    temp = num
    cnt = 0
    
    while True:
        if temp == 1:
            break
        if cnt >= 500:
            cnt = -1
            break
            
        if temp % 2 == 0:
            temp //= 2
        else:
            temp = temp*3+1
        cnt += 1

    return cnt