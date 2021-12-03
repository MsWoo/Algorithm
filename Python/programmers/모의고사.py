def solution(answers):
    answer = []
    
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    a = [0, 0, 0, 0]
    
    for i, x in enumerate(answers):
        if x == p1[i%5]:
            a[1]+=1
        if x == p2[i%8]:
            a[2]+=1
        if x == p3[i%10]:
            a[3]+=1
    
    maxp = max(a)
    for i in range(len(a)):
        if maxp == a[i]:
            answer.append(i)
            
    
    return answer