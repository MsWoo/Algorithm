def solution(s):
    answer = []
    
    subS = s.split(' ')
    
    for ele in subS:
        ele = ele.capitalize()
        answer.append(ele)
    
    return ' '.join(answer)