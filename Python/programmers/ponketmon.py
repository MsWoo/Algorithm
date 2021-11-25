def solution(nums):
    answer = 0
    
    maxmon = len(nums) // 2
    temp = list(set(nums))
        
    for t in temp:
        if answer < maxmon:
            answer += 1
    
    return answer