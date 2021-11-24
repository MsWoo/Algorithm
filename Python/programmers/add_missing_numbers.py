def solution(numbers):
    answer = -1
    sums = 0
    
    for i in range(1, 10):
        if i not in numbers:
            sums += i
    
    answer = sums
    
    return answer