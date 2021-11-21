def solution(new_id):
    answer = ''

    newid = []
    temp = []
    
    for i in new_id:
        if i.isalnum() or i == "-" or i == "_" or i == ".":
            newid.append(i)           
    
    temp.append(newid[0])
    
    for i in range(1, len(newid)):
        if newid[i-1] == "." and newid[i-1] != newid[i]:
            temp.append(newid[i])
        if newid[i-1] != ".":
            temp.append(newid[i])
        
    newid = temp[:]
    temp.clear()


    if len(newid) > 0 and newid[-1] == ".":
        newid.pop(-1)
    if len(newid) > 0 and newid[0] == ".":
        newid.pop(0)
    
    if len(newid) == 0 :
        newid.append("a")
    
    if len(newid) > 15:
        newid = newid[:15]
        
    if len(newid) > 0 and newid[-1] == ".":
        newid.pop(-1)
        
    while len(newid) < 3:
        newid.append(newid[-1])
        
    
    answer = "".join(newid).lower()
    print(answer)
    
    return answer