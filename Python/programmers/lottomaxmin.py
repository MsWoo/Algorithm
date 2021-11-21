def solution(lottos, win_nums):
    answer = []
    
    zerocnt = 0
    cnt = 0
    
    for i in lottos:
        if i == 0:
            zerocnt += 1
        if i in win_nums:
            cnt += 1
    
    usezero = zerocnt + cnt
    
    if usezero == 0:
        answer.append(6)
    else:
        answer.append(7-usezero)
    if cnt == 0:
        answer.append(6)
    else:
        answer.append(7-cnt)

    
    return answer