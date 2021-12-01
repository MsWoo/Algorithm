def solution(board, moves):
    answer = 0
    temp = []
    
    for m in moves:
        for i in range(len(board)):
            if board[i][m-1] != 0 :
                if len(temp) > 0 and temp[-1] == board[i][m-1]:
                    answer += 2
                    temp.pop()
                else:
                    temp.append(board[i][m-1])
                board[i][m-1] = 0
                break
    
    return answer