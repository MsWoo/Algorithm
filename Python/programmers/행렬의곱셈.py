def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = []
        for ar2 in range(len(arr2[0])):
            sum = 0
            for j in range(len(arr1[0])):
                sum += arr1[i][j] * arr2[j][ar2]   
            temp.append(sum)
        answer.append(temp)
    
    return answer