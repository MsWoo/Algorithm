import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

participant = [x for x in input().split()]
completion = [x for x in input().split()]

print(solution(participant, completion))