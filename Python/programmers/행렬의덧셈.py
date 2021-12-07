def solution(arr1, arr2):
    answer = []
    temp = []
    
    for x, y in zip(arr1, arr2):
        temp.clear()
        for i in range(len(x)):
            temp.append(x[i] + y[i])
        answer.append(temp[:])
        
    return answer