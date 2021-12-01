import math

def solution(progresses, speeds):
    answer = []
    temp = []
    
    for p, s in zip(progresses, speeds):
        temp.append(math.ceil((100-p)/s))
    
    while True:
        if len(temp) == 0:
            answer.append(cnt)
            break
            
        if len(temp) == 1:
            answer.append(1)
            break
            
        first = temp[0]
        cnt = 1
            
        for i in range(1, len(temp)):
            if first >= temp[i]:
                cnt+=1
            else:
                answer.append(cnt)
                break
        
        for i in range(cnt-1, -1, -1):
            temp.pop(i)
    
    return answer