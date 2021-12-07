def solution(x):
    num = str(x)
    sums = 0
    
    for s in num:
        sums += int(s)

    return True if x%sums == 0 else False