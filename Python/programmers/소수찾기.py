from itertools import permutations

def solution(numbers):

    def prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                return False
        return True
    
    temp = set()
    
    for i in range(1, len(numbers)+1):
        for j in permutations(numbers, i):
            if prime(int("".join(j))):
                temp.add(int("".join(j)))
    
    return len(temp)