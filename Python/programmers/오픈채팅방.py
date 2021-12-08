def solution(record):
    answer = []
    temp = dict()
    
    for r in record:
        s = r.split()
        if s[0] == "Enter":
            temp[s[1]] = s[2]  
        elif s[0] == "Change":
            temp[s[1]] = s[2]
            
    for r in record:
        s = r.split()
        if s[0] == "Enter":
            answer.append(f"{temp[s[1]]}님이 들어왔습니다.")    
        elif s[0] == "Leave":
            answer.append(f"{temp[s[1]]}님이 나갔습니다.")

    return answer