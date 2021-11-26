def solution(s):
    answer = False
    
    if len(s) == 4 or len(s) == 6:
        answer = True
        for ele in s:
            if ele.isalpha():
                answer = False
    
    return answer