def solution(s):
    answer = 0
    
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    
    for n in nums:
        s = s.replace(n, str(nums.index(n)))
    
    answer = int(s)
    
    return answer