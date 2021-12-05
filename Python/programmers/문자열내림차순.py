def solution(s):
    answer = []
    for ele in s:
        answer.append(ele)
    answer.sort(reverse = True)
    return ''.join(answer)