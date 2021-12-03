def solution(N, stages):
    answer = []
    playersCurStage = [0 for _ in range(N+2)]
    fails = [-1]
    players = len(stages)
    
    for i in range(1, len(stages)+1):
        playersCurStage[stages[i-1]] += 1

    for i in range(1, N+2):
        if playersCurStage[i] == 0:
            fails.append(0)
        else:
            fails.append(playersCurStage[i]/players)
            players -= playersCurStage[i]
            
    fails[-1] = -1
    
    for _ in range(N):
        idx = fails.index(max(fails))
        answer.append(idx)
        fails[idx] = -1
    
    return answer